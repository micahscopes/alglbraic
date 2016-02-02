#version 130
#define providesInside
#define providesInit

#info Geometric Algebra G([-1,-1,-1,-1])
#include "Brute-Raytracer.frag"
#group Geometric Algebraic

// Remaining Constant
uniform vec3 frame; slider[(1,1,1),(1,2,3),(9,9,9)]
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

const int N = 9;
uniform int Permutation1; slider[0,0,362880]
uniform int Permutation2; slider[0,0,362880]
uniform int Permutation3; slider[0,0,362880]
uniform int Permutation4; slider[0,0,362880]
int P1[N];
int P2[N];
int P3[N];
int P4[N];
uniform int Iterations; slider[0,16,100]
uniform float Bailout; slider[0,5,30]

uniform bool Julia; checkbox[false]
uniform bool usePrevious; checkbox[false]

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

mat3 set(mat3 a, int i, float x){

    switch(i) {
      case 0 : a[0][0]=x; break;
      case 1 : a[0][1]=x; break;
      case 2 : a[0][2]=x; break;
      case 3 : a[1][0]=x; break;
      case 4 : a[1][1]=x; break;
      case 5 : a[1][2]=x; break;
      case 6 : a[2][0]=x; break;
      case 7 : a[2][1]=x; break;
      case 8 : a[2][2]=x; break;
    }
    return a;
}

float get(mat3 a, int i){
  switch(i) {
    case 0 : return a[0][0]; break;
    case 1 : return a[0][1]; break;
    case 2 : return a[0][2]; break;
    case 3 : return a[1][0]; break;
    case 4 : return a[1][1]; break;
    case 5 : return a[1][2]; break;
    case 6 : return a[2][0]; break;
    case 7 : return a[2][1]; break;
    case 8 : return a[2][2]; break;

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
    mat3 addFrame(mat3 g, vec3 p){

    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return g; //error, please set frame indices to be different
    }
    for(int i = 0; i<9; i++) {
        if (i == frame.x-1) { g = set(g,i,p.x); }
        else if (i == frame.y-1) { g = set(g,i,p.y); }
        else if (i == frame.z-1) { g = set(g,i,p.z); }
        }
return g;
}

mat3 loadPositions(mat3 g) {
  for(int i = 0; i<9; i++) {
        g = set(g,i,getPosition(i));
    }
    return g;
}


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

mat3 mutate(mat3 A,int[N] perm,bool inv) {
    mat3 permutated = mat3(0.0);
    for(int i = 0; i < N; i++) {
        if(!inv) {
            permutated = set(permutated,i,get(A,perm[i]));
        } else {
            permutated = set(permutated,perm[i],get(A,i));
        }
    }
    return permutated;
}


float norm(mat3 a){
float n = 0;
for (int i=0; i<3;i++) {
	for (int j=0;j<3;j++) {
	n += pow(a[i][j],2.0);
	}
   }
return sqrt(n);
}

mat3 iter(mat3 z, mat3 z0) {
  //mat3 tz = transpose(z);
  return mutate(z,P1,false) * mutate(z,P2,false) * mutate(z,P2,false);
}

mat3 O = mat3(0,0,0,0,0,0,0,0,0);
void init(){
    // 'a is for ..., ..., 'O' is for origin, ...'
    O = loadPositions(O);
}
bool inside(vec3 pt) {
    mat3 z = addFrame(O,pt);
    mat3 z0 = z;
    mat3 zprev;
	float r;
	int i=0;
	r=abs(norm(z));
mat3 JuliaGeo = mat3(JuliaG1,JuliaG2,JuliaG3,JuliaG4,JuliaG5,JuliaG6,JuliaG7,JuliaG8,JuliaG9);
  while(r<Bailout && (i<Iterations)) {
    if (usePrevious) { zprev = z; } else { zprev = z0; }
		z = iter(z,zprev);
		z = Julia ? z+JuliaGeo : z+zprev;
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
