#!/usr/bin/env python
from __future__ import print_function
from sympy import symbols, sin, cos, simplify, Symbol


def loadVector(coefs):
    s = "float[N](" + ", ".join(map(lambda i: str(i),coefs))+");"
    return s;

### write the glsl shader pieces
computeRange = "[-2,0,2]"
frameDimRange = ("[(1,1,1),(1,2,3),"+str((bases,)*3)+"]").decode('unicode_escape').encode('ascii','ignore')
nHidden = bases-3
header = """#version 130
#define providesInside
#define providesInit

#info Algebra G("""+metric+""")
#include "Brute-Raytracer.frag"
#group Geometric Algebraic

// Remaining Constant
"""
gl += "uniform vec3 frame; slider[(1,1,1),(1,2,3),("+str(bases)+","+str(bases)+","+str(bases)+")]\n"
for i in range(bases):
    gl += "uniform float position"+str(i+1)+"; slider"+computeRange+'\n'
gl += """
uniform int Permutation; slider[0,0,"""+str(math.factorial(bases))+"""]
uniform int Iterations; slider[0,16,100]
uniform float Bailout; slider[0,5,30]

uniform bool Julia; checkbox[false]
uniform bool usePrevious; checkbox[false]
const int N = """+str(bases)+""";
int P[N];
"""

for i in range(bases):
    gl += "uniform float JuliaG"+str(i+1)+"; slider"+computeRange+'\n'

gl += ("struct Vect{\n" )
for i in range(baseQuads):
    gl += ("vec4 q"+str(i)+";\n")
gl += ("\n};\n\n" )


gl += ("Vect Vect0(){\n")
gl += ("return ")
gl += loadVect(MV(0))
gl += ("\n}\n\n")

gl += """

    const Vect I = """+loadVect(I)+"""

"""
gl += ("Vect g(Vect a, Vect b){\n")
gl += ("return ")
gl += loadVect(AgB)
gl += ("\n}\n\n")

gl += ("Vect set(Vect a, int i, float x){\n")
gl += """
    switch(i) {"""
for i in range(bases):
    gl += "     case "+str(i)+" : a"+getter(i)+"=x; break;"
gl +=  """
    }
    return a;
}
"""
gl += """
float get(Vect a, int i){
    switch(i){"""
for i in range(bases):
    gl += "     case "+str(i)+" : return a"+getter(i)+"; break;"
gl +=  """}
}
"""

gl += """
float getPosition(int i){
    switch(i){"""
for i in range(bases):
    gl += "     case "+str(i)+" : return position"+str(i+1)+"; break;"
gl += """}
}
"""


gl += """
float[N] loadPositions(float u[N]){
    for(int i = 0; i<N; i++) {
        u[i] = getPosition(i);
    }
    return u;
}
    """

gl += """
Vect addFrame(Vect g, vec3 p){
    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return g; //error, please set frame indices to be different
    }
    for(int i = 0; i<N; i++) {
        if (i == frame.x-1) { g = set(g,i,p.x); }
        else if (i == frame.y-1) { g = set(g,i,p.y); }
        else if (i == frame.z-1) { g = set(g,i,p.z); }
        }
return g;
}
"""


gl += """

int[N] permutation(int i)
{
   int j, k = 0;
   int fact[N];
   int perm[N];

   // compute factorial numbers
   fact[k] = 1;
   while (++k < N)
      fact[k] = fact[k - 1] * k;

   // compute factorial code
   for (k = 0; k < N; ++k)
   {
      perm[k] = i / fact[N - 1 - k];
      i = i % fact[N - 1 - k];
   }

   // readjust values to obtain the permutation
   // start from the end and check if preceding values are lower
   for (k = N - 1; k > 0; --k)
      for (j = k - 1; j >= 0; --j)
         if (perm[j] <= perm[k])
            perm[k]++;

    return perm;
}

Vect permutate(Vect A,bool conj) {
    Vect permutated = Vect0();
    for(int i = 0; i < N; i++) {
        if(!conj) {
            permutated = set(permutated,i,get(A,P[i]));
        } else {
            permutated = set(permutated,P[i],get(A,i));
        }
    }
    return permutated;
}

"""

gl += ("Vect aVect(float a, Vect b){\n") #scalar a multipled into multivector B
gl += ("return "+loadVect(Symbol("a")*B))
gl += ("\n}\n\n")

gl += ("Vect rev(Vect a){\n")
gl += ("return "+loadVect(A.rev()))
gl += ("\n}\n\n")

gl += ("Vect invo(Vect a){\n")
gl += ("return aVect(pow(-1,"+str(bases)+"),a);")
gl += ("\n}\n\n")

gl += ("Vect cong(Vect a){\n")
gl += ("return invo(rev(a));")
gl += ("\n}\n\n")

gl += """

Vect g3(Vect a,Vect b, Vect c) {
	return g(a,g(b,c));
}

float[N] mulpwr(float a[N],int n) {
	float r[N] = a;
	for (int i=0;i<n-1;i++){
	   r = mul(r,a);
    }
    return r;
}

Vect add(Vect a, Vect b) {
    return Vect("""
for d in range(baseQuads):
	gl += "a.q"+str(d)+" + b.q"+str(d)+("," if d<baseQuads-1 else ");\n}")

#normExpr = str((A.rev()|A).scalar()).replace("**2",",2)").replace("a.q","pow(a.q")
gl += ("float geoNorm(Vect a){\n")
gl += ("return get(inner(a,rev(a)),0);\n")
gl += ("}\n\n")


gl += """
Vect O = Vect0();
void init(){
    // 'a is for ..., ..., 'O' is for origin, ...'
    O = loadPositions(O);
}
"""

gl +="""

Vect dual(Vect a) {
	return g(I,a);
}

"""
gl +="""

Vect iter(Vect z) {
	return g(z,permutate(z,true));
}

"""
gl += ""
# gl += "Vect R = "+loadVectCoefs(map(lambda i: "rot"+str(i+1),range(bases)))
# def symb(name,i): return Symbol(name+"["+str(i)+"]");
# ptsVect = loadVect(reduce(add,map(lambda i: symb("pt",i)*gMVs[i+1],[0,1,2])))
gl += """
bool inside(vec3 pt) {
    P = permutation(Permutation);
    Vect z = addFrame(O,pt);
    Vect z0 = z;
	float r;
	int i=0;
	r=abs(geoNorm(z));"""
gl += "\nVect JuliaVect = "
gl += loadVectCoefs(map(lambda i: "JuliaG"+str(i+1),range(bases)))
gl +="""

        while(r<Bailout && (i<Iterations)) {
        Vect zprev;
        if (usePrevious) { zprev = z; } else { zprev = z0; }
		z = iter(z);
		z = add(z,(Julia ? JuliaVect : zprev));
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
for i in range(bases):
    gl+= "position"+str(i+1)+" = 0.0\n"
gl += "#endpreset"


output = open(sys.argv[2], "w")
output.write(gl)
output.close
