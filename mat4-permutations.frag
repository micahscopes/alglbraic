#version 130
#define providesInside
#define providesInit

#info Geometric Algebra G([-1,-1,-1,-1])
#include "Brute-Raytracer.frag"
#group Geometric Algebraic

// Remaining Constant
uniform vec3 frame; slider[(1,1,1),(1,2,3),(16,16,16)]
uniform float position1; slider[-2,0,2]
uniform float position2; slider[-2,0,2]
uniform float position3; slider[-2,0,2]
uniform float position4; slider[-2,0,2]
uniform float position5; slider[-2,0,2]
uniform float position6; slider[-2,0,2]
uniform float position7; slider[-2,0,2]
uniform float position8; slider[-2,0,2]
uniform float position9; slider[-2,0,2]
uniform float position10; slider[-2,0,2]
uniform float position11; slider[-2,0,2]
uniform float position12; slider[-2,0,2]
uniform float position13; slider[-2,0,2]
uniform float position14; slider[-2,0,2]
uniform float position15; slider[-2,0,2]
uniform float position16; slider[-2,0,2]

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
uniform float JuliaG9; slider[-2,0,2]
uniform float JuliaG10; slider[-2,0,2]
uniform float JuliaG11; slider[-2,0,2]
uniform float JuliaG12; slider[-2,0,2]
uniform float JuliaG13; slider[-2,0,2]
uniform float JuliaG14; slider[-2,0,2]
uniform float JuliaG15; slider[-2,0,2]
uniform float JuliaG16; slider[-2,0,2]

mat4 set(mat4 a, int i, float x){

    switch(i) {
      case 0 : a[0][0]=x; break;
      case 1 : a[0][1]=x; break;
      case 2 : a[0][2]=x; break;
      case 3 : a[0][3]=x; break;
      case 4 : a[1][0]=x; break;
      case 5 : a[1][1]=x; break;
      case 6 : a[1][2]=x; break;
      case 7 : a[1][3]=x; break;
      case 8 : a[2][0]=x; break;
      case 9 : a[2][1]=x; break;
      case 10 : a[2][2]=x; break;
      case 11 : a[2][3]=x; break;
      case 12 : a[3][0]=x; break;
      case 13 : a[3][1]=x; break;
      case 14 : a[3][2]=x; break;
      case 15 : a[3][3]=x; break;
    }
    return a;
}

float get(mat4 a, int i){
  switch(i) {
    case 0 : return a[0][0]; break;
    case 1 : return a[0][1]; break;
    case 2 : return a[0][2]; break;
    case 3 : return a[0][3]; break;
    case 4 : return a[1][0]; break;
    case 5 : return a[1][1]; break;
    case 6 : return a[1][2]; break;
    case 7 : return a[1][3]; break;
    case 8 : return a[2][0]; break;
    case 9 : return a[2][1]; break;
    case 10 : return a[2][2]; break;
    case 11 : return a[2][3]; break;
    case 12 : return a[3][0]; break;
    case 13 : return a[3][1]; break;
    case 14 : return a[3][2]; break;
    case 15 : return a[3][3]; break;
    }
}

float getPosition(int i){
    switch(i){
      case 0 : return position1; break;
      case 1 : return position2; break;
      case 2 : return position3; break;
      case 3 : return position4; break;
      case 4 : return position5; break;
      case 5 : return position6; break;
      case 6 : return position7; break;
      case 7 : return position8; break;
      case 8 : return position9; break;
      case 9 : return position10; break;
      case 10 : return position11; break;
      case 11 : return position12; break;
      case 12 : return position13; break;
      case 13 : return position14; break;
      case 14 : return position15; break;
      case 15 : return position16; break;}
}
    mat4 addFrame(mat4 g, vec3 p){

    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return g; //error, please set frame indices to be different
    }
    for(int i = 0; i<16; i++) {
        if (i == frame.x-1) { g = set(g,i,p.x); }
        else if (i == frame.y-1) { g = set(g,i,p.y); }
        else if (i == frame.z-1) { g = set(g,i,p.z); }
        }
return g;
}

mat4 loadPositions(mat4 g) {
  for(int i = 0; i<16; i++) {
        g = set(g,i,getPosition(i));
    }
    return g;
}

mat4 iter(mat4 z, mat4 z0) {
mat4 tz = transpose(z);
	return z*z*tz;
}



float norm(mat4 a){
float n = 0;
for (int i=0; i<4;i++) {
	for (int j=0;j<4;j++) {
	n += pow(a[i][j],2.0);
	}
   }
return sqrt(n);
}


mat4 O = mat4(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
void init(){
    // 'a is for ..., ..., 'O' is for origin, ...'
    O = loadPositions(O);
}
bool inside(vec3 pt) {
    mat4 z = addFrame(O,pt);
    mat4 z0 = z;
	float r;
	int i=0;
	r=abs(norm(z));
mat4 JuliaGeo = mat4(JuliaG1,JuliaG2,JuliaG3,JuliaG4,JuliaG5,JuliaG6,JuliaG7,JuliaG8,JuliaG9,JuliaG10,JuliaG11,JuliaG12,JuliaG13,JuliaG14,JuliaG15,JuliaG16);
  while(r<Bailout && (i<Iterations)) {
		z = iter(z,z0);
		z = Julia ? z+JuliaGeo : z+z0;
		r=norm(z);
		i++;
	}
	return (r<Bailout);
}



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

#preset recenter
position1 = 0.0
position2 = 0.0
position3 = 0.0
position4 = 0.0
position5 = 0.0
position6 = 0.0
position7 = 0.0
position8 = 0.0
position9 = 0.0
position10 = 0.0
position11 = 0.0
position12 = 0.0
position13 = 0.0
position14 = 0.0
position15 = 0.0
position16 = 0.0
#endpreset
