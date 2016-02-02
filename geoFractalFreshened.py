#!/usr/bin/env python
from __future__ import print_function
from sympy import symbols, sin, cos, simplify, Symbol
from sympy.galgebra.ga import MV
from sympy.galgebra.printing import enhance_print
from GLSLPrinter import *
import argparse

metric=sys.argv[1]
print(metric)
e = MV.setup(" ".join(map(lambda i: "e"+str(i+1), range(len(metric.split(","))))),metric)
VDIM = len(e[0].blades_flat1)
def getter(i):
    return "["+str(i)+"]"
def loadGeoCoefs(coefs):
    s = "Geo(\n"
    for i in range(VDIM):
        for j in range(4):
            coef = str(coefs[i*4+j%4])
            #substitute sympy **n power operator with pow(exp,n)
            rule = r"(a(?:(?!a).)*\*\*2)"
            s += re.sub(r"\*\*", r",", re.sub(rule,r"pow(\1)",coef))
            if (j<3): s += (",")
        s += (")")
        if (i<baseQuads-1): s += (",\n")
    else: s += ("\n);")
    return s
def loadGeo(mv):
    return loadGeoCoefs(map(lambda i: mv.coef(gMVs[i]),range(VDIM)))

g = map(lambda i: e[0].blades_flat1[i],range(VDIM))
gMVs = map(lambda i: MV(g[i]),range(VDIM))
a = map(lambda i: Symbol('a'+getter(i)), xrange(VDIM))
b = map(lambda i: Symbol('b'+getter(i)), xrange(VDIM))

As = map(lambda i: a[i]*g[i],range(VDIM))
Bs = map(lambda i: b[i]*g[i],range(VDIM))

add = lambda b,r: b+r
A = MV(reduce(add,As))
B = MV(reduce(add,Bs))
G = MV(reduce(add,g))
I = MV(g[VDIM-1])

#Gram Schmidt process as described by http://vixra.org/pdf/1306.0176v1.pdf
def orthogonalize(v):
    outer = lambda b,r: b^r
    V = map(lambda j: reduce(outer,map(lambda i: v.grade(i),range(j))),range(1,len(v.blades_flat1)+1))
    return reduce(add,map(lambda k: V[k].rev()*V[k+1],range(len(V)-1)))
OrthoA = orthogonalize(A)


### write the glsl shader pieces
computeRange = "[-2,0,2]"
frameDimRange = ("[(1,1,1),(1,2,3),"+str((VDIM,)*3)+"]").decode('unicode_escape').encode('ascii','ignore')
nHidden = VDIM-3
gl = """#version 130
#define providesInside
#define providesInit

#info Geometric Algebra G("""+metric+""")
#include "Brute-Raytracer.frag"
#group Geometric Algebraic

// Remaining Constant
"""
gl += "uniform vec3 frame; slider[(1,1,1),(1,2,3),("+str(VDIM)+","+str(VDIM)+","+str(VDIM)+")]\n"
for i in range(VDIM):
    gl += "uniform float position"+str(i+1)+"; slider"+computeRange+'\n'
gl += """
uniform int Iterations; slider[0,16,100]
uniform float Bailout; slider[0,5,30]

uniform bool Julia; checkbox[false]
uniform bool usePrevious; checkbox[false]

"""

for i in range(VDIM):
    gl += "uniform float JuliaG"+str(i+1)+"; slider"+computeRange+'\n'

gl += ("struct Geo{\n" )
for i in range(baseQuads):
    gl += ("vec4 q"+str(i)+";\n")
gl += ("\n};\n\n" )

gl += """

    Geo I = """+loadGeo(I)+"""

"""

AinB = A|B
gl += ("Geo inner(Geo a, Geo b){\n")
gl += ("return ")
gl += loadGeo(AinB)
gl += ("\n}\n\n")

AoutB = A^B
gl += ("Geo outer(Geo a, Geo b){\n")
gl += ("return ")
gl += loadGeo(AoutB)
gl += ("\n}\n\n")

AgB = AinB + AoutB # reusing these computations
gl += ("Geo g(Geo a, Geo b){\n")
gl += ("return ")
gl += loadGeo(AgB)
gl += ("\n}\n\n")

gl += ("Geo Geo0(){\n")
gl += ("return ")
gl += loadGeo(MV(0))
gl += ("\n}\n\n")

gl += ("Geo set(Geo a, int i, float x){\n")
gl += """
    switch(i) {"""
for i in range(VDIM):
    gl += "     case "+str(i)+" : a"+getter(i)+"=x; break;"
gl +=  """
    }
    return a;
}
"""
gl += """
float get(Geo a, int i){
    switch(i){"""
for i in range(VDIM):
    gl += "     case "+str(i)+" : return a"+getter(i)+"; break;"
gl +=  """}
}
"""

gl += """
float getPosition(int i){
    switch(i){"""
for i in range(VDIM):
    gl += "     case "+str(i)+" : return position"+str(i+1)+"; break;"
gl += """}
}
"""

gl += ("Geo loadPositions(Geo g){\n")
gl += """
    for(int i = 0; i<"""+str(VDIM)+"""; i++) {
        g = set(g,i,getPosition(i));
    }
    return g;
}
    """

gl += ("Geo addFrame(Geo g, vec3 p){\n")
gl += """
    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return g; //error, please set frame indices to be different
    }
    for(int i = 0; i<"""+str(VDIM)+"""; i++) {
        if (i == frame.x-1) { g = set(g,i,p.x); }
        else if (i == frame.y-1) { g = set(g,i,p.y); }
        else if (i == frame.z-1) { g = set(g,i,p.z); }
        }
return g;
}
"""

gl += ("Geo aGeo(float a, Geo b){\n") #scalar a multipled into multivector B
gl += ("return "+loadGeo(Symbol("a")*B))
gl += ("\n}\n\n")

gl += ("Geo rev(Geo a){\n")
gl += ("return "+loadGeo(A.rev()))
gl += ("\n}\n\n")

gl += ("Geo invo(Geo a){\n")
gl += ("return aGeo(pow(-1,"+str(VDIM)+"),a);")
gl += ("\n}\n\n")

gl += ("Geo cong(Geo a){\n")
gl += ("return invo(rev(a));")
gl += ("\n}\n\n")

gl += """

Geo g3(Geo a,Geo b, Geo c) {
	return g(a,g(b,c));
}

Geo gpwr(Geo a,int n) {
	Geo r = a;
	for (int i=0;i<n-1;i++){
	r = g(r,a);
}
return r;
}

Geo add(Geo a, Geo b) {
    return Geo("""
for d in range(baseQuads):
	gl += "a.q"+str(d)+" + b.q"+str(d)+("," if d<baseQuads-1 else ");\n}")

# gl +="""
# Geo grade1(Geo a) {
# 	return """+loadGeo(A.grade(1))+"""
# }
#
# """
#
# gl +="""
# Geo grade2(Geo a) {
# 	return """+loadGeo(A.grade(2))+"""
# }
#
# """

#normExpr = str((A.rev()|A).scalar()).replace("**2",",2)").replace("a.q","pow(a.q")
gl += ("float geoNorm(Geo a){\n")
gl += ("return get(inner(a,rev(a)),0);\n")
gl += ("}\n\n")


gl += """
Geo O = Geo0();
void init(){
    // 'a is for ..., ..., 'O' is for origin, ...'
    O = loadPositions(O);
}
"""

gl +="""

Geo dual(Geo a) {
	return g(I,a);
}

"""
gl +="""

Geo iter(Geo z) {
	return g(gpwr(z,2),rev(gpwr(z,1)));
}

"""
gl += "bool inside(vec3 pt) {"
# gl += "Geo R = "+loadGeoCoefs(map(lambda i: "rot"+str(i+1),range(VDIM)))
# def symb(name,i): return Symbol(name+"["+str(i)+"]");
# ptsGeo = loadGeo(reduce(add,map(lambda i: symb("pt",i)*gMVs[i+1],[0,1,2])))
gl += """
    Geo z = addFrame(O,pt);
    Geo z0 = z;
	float r;
	int i=0;
	r=abs(geoNorm(z));"""
gl += "\nGeo JuliaGeo = "
gl += loadGeoCoefs(map(lambda i: "JuliaG"+str(i+1),range(VDIM)))
gl +="""

        while(r<Bailout && (i<Iterations)) {
        Geo zprev;
        if (usePrevious) { zprev = z; } else { zprev = z0; }
		z = iter(z);
		z = add(z,(Julia ? JuliaGeo : zprev));
		r=geoNorm(z);
		i++;
	}
	return (r<Bailout);
}

"""
gl += """

#preset Init
FOV = 0.4
Eye = -0.821733,-1.82625,2.23376
Target = 2.11612,4.20274,-5.18381
Up = -0.902532,-0.0745699,-0.424118
EquiRectangular = false
Gamma = 2.17595
ToneMapping = 3
Exposure = 0.3261
Brightness = 1
Contrast = 1
Saturation = 1
Specular = 1.5
SpecularExp = 16
SpotLight = 1,1,1,0.38043
SpotLightDir = 0.1,0.1
CamLight = 1,1,1,1
CamLightMin = 0
Glow = 1,1,1,0.16667
Fog = 0
BaseColor = 1,1,1
OrbitStrength = 0.8
X = 0.5,0.6,0.6,0.7
Y = 1,0.6,0,0.4
Z = 0.8,0.78,1,0.5
R = 0.4,0.7,1,0.12
BackgroundColor = 0.2,0.1,0.7
GradientBackground = 2
CycleColors = false
Cycles = 1.1
#endpreset

"""

gl += "#preset recenter\n"
for i in range(VDIM):
    gl+= "position"+str(i+1)+" = 0.0\n"
gl += "#endpreset"


output = open(sys.argv[2], "w")
output.write(gl)
output.close
