#version 130
#define providesInside
#define providesInit

#info Geometric Algebra G([-1,-1,-1])
#include "Brute-Raytracer.frag"
#group Geometric Algebraic

// Remaining Constant
uniform vec3 frame; slider[(1,1,1),(1,2,3),(8,8,8)]
uniform float position1; slider[-2,0,2]
uniform float position2; slider[-2,0,2]
uniform float position3; slider[-2,0,2]
uniform float position4; slider[-2,0,2]
uniform float position5; slider[-2,0,2]
uniform float position6; slider[-2,0,2]
uniform float position7; slider[-2,0,2]
uniform float position8; slider[-2,0,2]

uniform int Iterations; slider[0,16,100]
uniform float Bailout; slider[0,5,30]

uniform bool Julia; checkbox[false]

uniform float JuliaG1; slider[-2,0,2]
uniform float JuliaG2; slider[-2,0,2]
uniform float JuliaG3; slider[-2,0,2]
uniform float JuliaG4; slider[-2,0,2]
uniform float JuliaG5; slider[-2,0,2]
uniform float JuliaG6; slider[-2,0,2]
uniform float JuliaG7; slider[-2,0,2]
uniform float JuliaG8; slider[-2,0,2]
struct Geo{
vec4 q0;
vec4 q1;
};

Geo g(Geo a, Geo b){
return Geo(
vec4(a.q0[0]*b.q0[0] - a.q0[1]*b.q0[1] - a.q0[2]*b.q0[2] - a.q0[3]*b.q0[3] - a.q1[0]*b.q1[0] - a.q1[1]*b.q1[1] - a.q1[2]*b.q1[2] + a.q1[3]*b.q1[3],
a.q0[0]*b.q0[1] + a.q0[1]*b.q0[0] + a.q0[2]*b.q1[0] + a.q0[3]*b.q1[1] - a.q1[0]*b.q0[2] - a.q1[1]*b.q0[3] - a.q1[2]*b.q1[3] - a.q1[3]*b.q1[2],
a.q0[0]*b.q0[2] - a.q0[1]*b.q1[0] + a.q0[2]*b.q0[0] + a.q0[3]*b.q1[2] + a.q1[0]*b.q0[1] + a.q1[1]*b.q1[3] - a.q1[2]*b.q0[3] + a.q1[3]*b.q1[1],
a.q0[0]*b.q0[3] - a.q0[1]*b.q1[1] - a.q0[2]*b.q1[2] + a.q0[3]*b.q0[0] - a.q1[0]*b.q1[3] + a.q1[1]*b.q0[1] + a.q1[2]*b.q0[2] - a.q1[3]*b.q1[0])
,
vec4(a.q0[0]*b.q1[0] + a.q0[1]*b.q0[2] - a.q0[2]*b.q0[1] - a.q0[3]*b.q1[3] + a.q1[0]*b.q0[0] + a.q1[1]*b.q1[2] - a.q1[2]*b.q1[1] - a.q1[3]*b.q0[3],
a.q0[0]*b.q1[1] + a.q0[1]*b.q0[3] + a.q0[2]*b.q1[3] - a.q0[3]*b.q0[1] - a.q1[0]*b.q1[2] + a.q1[1]*b.q0[0] + a.q1[2]*b.q1[0] + a.q1[3]*b.q0[2],
a.q0[0]*b.q1[2] - a.q0[1]*b.q1[3] + a.q0[2]*b.q0[3] - a.q0[3]*b.q0[2] + a.q1[0]*b.q1[1] - a.q1[1]*b.q1[0] + a.q1[2]*b.q0[0] - a.q1[3]*b.q0[1],
a.q0[0]*b.q1[3] + a.q0[1]*b.q1[2] - a.q0[2]*b.q1[1] + a.q0[3]*b.q1[0] + a.q1[0]*b.q0[3] - a.q1[1]*b.q0[2] + a.q1[2]*b.q0[1] + a.q1[3]*b.q0[0])
);}

Geo Geo0(){
return Geo(
vec4(0,
0,
0,
0)
,
vec4(0,
0,
0,
0)
);}

Geo set(Geo a, int i, float x){

    switch(i) {     case 0 : a.q0[0]=x; break;     case 1 : a.q0[1]=x; break;     case 2 : a.q0[2]=x; break;     case 3 : a.q0[3]=x; break;     case 4 : a.q1[0]=x; break;     case 5 : a.q1[1]=x; break;     case 6 : a.q1[2]=x; break;     case 7 : a.q1[3]=x; break;
    }
    return a;
}

float get(Geo a, int i){
    switch(i){     case 0 : return a.q0[0]; break;     case 1 : return a.q0[1]; break;     case 2 : return a.q0[2]; break;     case 3 : return a.q0[3]; break;     case 4 : return a.q1[0]; break;     case 5 : return a.q1[1]; break;     case 6 : return a.q1[2]; break;     case 7 : return a.q1[3]; break;}
}

float getPosition(int i){
    switch(i){     case 0 : return position1; break;     case 1 : return position2; break;     case 2 : return position3; break;     case 3 : return position4; break;     case 4 : return position5; break;     case 5 : return position6; break;     case 6 : return position7; break;     case 7 : return position8; break;}
}
Geo loadPositions(Geo g){

    for(int i = 0; i<8; i++) {
        g = set(g,i,getPosition(i));
    }
    return g;
}
    Geo addFrame(Geo g, vec3 p){

    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return g; //error, please set frame indices to be different
    }
    for(int i = 0; i<8; i++) {
        if (i == frame.x-1) { g = set(g,i,p.x); }
        else if (i == frame.y-1) { g = set(g,i,p.y); }
        else if (i == frame.z-1) { g = set(g,i,p.z); }
        }
return g;
}
Geo inner(Geo a, Geo b){
return Geo(
vec4(-a.q0[1]*b.q0[1] - a.q0[2]*b.q0[2] - a.q0[3]*b.q0[3] - a.q1[0]*b.q1[0] - a.q1[1]*b.q1[1] - a.q1[2]*b.q1[2] + a.q1[3]*b.q1[3],
a.q0[2]*b.q1[0] + a.q0[3]*b.q1[1] - a.q1[0]*b.q0[2] - a.q1[1]*b.q0[3] - a.q1[2]*b.q1[3] - a.q1[3]*b.q1[2],
-a.q0[1]*b.q1[0] + a.q0[3]*b.q1[2] + a.q1[0]*b.q0[1] + a.q1[1]*b.q1[3] - a.q1[2]*b.q0[3] + a.q1[3]*b.q1[1],
-a.q0[1]*b.q1[1] - a.q0[2]*b.q1[2] - a.q1[0]*b.q1[3] + a.q1[1]*b.q0[1] + a.q1[2]*b.q0[2] - a.q1[3]*b.q1[0])
,
vec4(-a.q0[3]*b.q1[3] - a.q1[3]*b.q0[3],
a.q0[2]*b.q1[3] + a.q1[3]*b.q0[2],
-a.q0[1]*b.q1[3] - a.q1[3]*b.q0[1],
0)
);}

Geo outer(Geo a, Geo b){
return Geo(
vec4(a.q0[0]*b.q0[0],
a.q0[0]*b.q0[1] + a.q0[1]*b.q0[0],
a.q0[0]*b.q0[2] + a.q0[2]*b.q0[0],
a.q0[0]*b.q0[3] + a.q0[3]*b.q0[0])
,
vec4(a.q0[0]*b.q1[0] + a.q0[1]*b.q0[2] - a.q0[2]*b.q0[1] + a.q1[0]*b.q0[0],
a.q0[0]*b.q1[1] + a.q0[1]*b.q0[3] - a.q0[3]*b.q0[1] + a.q1[1]*b.q0[0],
a.q0[0]*b.q1[2] + a.q0[2]*b.q0[3] - a.q0[3]*b.q0[2] + a.q1[2]*b.q0[0],
a.q0[0]*b.q1[3] + a.q0[1]*b.q1[2] - a.q0[2]*b.q1[1] + a.q0[3]*b.q1[0] + a.q1[0]*b.q0[3] - a.q1[1]*b.q0[2] + a.q1[2]*b.q0[1] + a.q1[3]*b.q0[0])
);}

float geoNorm(Geo a){
return -pow(a.q0[1],2) - pow(a.q0[2],2) - pow(a.q0[3],2) + pow(a.q1[0],2) + pow(a.q1[1],2) + pow(a.q1[2],2) - pow(a.q1[3],2);
}

Geo aGeo(float a, Geo b){
return Geo(
vec4(a*b.q0[0],
a*b.q0[1],
a*b.q0[2],
a*b.q0[3])
,
vec4(a*b.q1[0],
a*b.q1[1],
a*b.q1[2],
a*b.q1[3])
);}Geo rev(Geo a){
return Geo(
vec4(a.q0[0],
a.q0[1],
a.q0[2],
a.q0[3])
,
vec4(-a.q1[0],
-a.q1[1],
-a.q1[2],
-a.q1[3])
);}
Geo add(Geo a, Geo b) {
    return Geo(a.q0 + b.q0,a.q1 + b.q1);
}
Geo dual(Geo a) {
    Geo invI = Geo(
vec4(0,
0,
0,
0)
,
vec4(0,
0,
0,
1)
);
    return g(a,invI);}
Geo ortho(Geo a) {return Geo(
vec4(0,
pow(a.q0[0],2)*a.q0[1],
pow(a.q0[0],2)*a.q0[2],
pow(a.q0[0],2)*a.q0[3])
,
vec4(-pow(a.q0[0],2)*a.q0[1]*a.q0[3]*a.q1[2] + pow(a.q0[0],2)*a.q0[2]*a.q0[3]*a.q1[1] - pow(a.q0[0],2)*pow(a.q0[3],2)*a.q1[0],
pow(a.q0[0],2)*a.q0[1]*a.q0[2]*a.q1[2] - pow(a.q0[0],2)*pow(a.q0[2],2)*a.q1[1] + pow(a.q0[0],2)*a.q0[2]*a.q0[3]*a.q1[0],
-pow(a.q0[0],2)*pow(a.q0[1],2)*a.q1[2] + pow(a.q0[0],2)*a.q0[1]*a.q0[2]*a.q1[1] - pow(a.q0[0],2)*a.q0[1]*a.q0[3]*a.q1[0],
0)
);
}

Geo iter(Geo z, Geo z0) {
	return add(g(g(z,z),z),z0);
}


Geo grade1(Geo a) {
	return Geo(
vec4(0,
a.q0[1],
a.q0[2],
a.q0[3])
,
vec4(0,
0,
0,
0)
);
}

Geo grade2(Geo a) {
	return Geo(
vec4(0,
0,
0,
0)
,
vec4(a.q1[0],
a.q1[1],
a.q1[2],
0)
);
}

Geo O = Geo0();
void init(){
    // 'a is for ..., ..., 'O' is for origin, ...'
    O = loadPositions(O);
}
bool inside(vec3 pt) {
    Geo z = addFrame(O,pt);
    Geo z0 = z;
	float r;
	int i=0;
	r=abs(geoNorm(z));
Geo JuliaGeo = Geo(
vec4(JuliaG1,
JuliaG2,
JuliaG3,
JuliaG4)
,
vec4(JuliaG5,
JuliaG6,
JuliaG7,
JuliaG8)
);

        while(r<Bailout && (i<Iterations)) {
		z = iter(z,z0);
		z = add(z,(Julia ? JuliaGeo : z0));
		r=geoNorm(z);
		i++;
	}
	return (r<Bailout);
}




#preset Default
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
