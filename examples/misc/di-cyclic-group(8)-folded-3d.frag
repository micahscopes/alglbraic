#version 130
#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 4

#info 16 dimensional fractal quest on Free module generated by {(1,9)(2,10)(3,11)(4,12)(5,13)(6,14)(7,15)(8,16)(17,25)(18,26)(19,27)(20,28)(21,29)(22,30)(23,31)(24,32), (1,8,15,6,13,4,11,2,9,16,7,14,5,12,3,10)(17,24,31,22,29,20,27,18,25,32,23,30,21,28,19,26), (1,25,9,17)(2,24,10,32)(3,23,11,31)(4,22,12,30)(5,21,13,29)(6,20,14,28)(7,19,15,27)(8,18,16,26), (1,24,9,32)(2,23,10,31)(3,22,11,30)(4,21,12,29)(5,20,13,28)(6,19,14,27)(7,18,15,26)(8,17,16,25), (1,7,13,3,9,15,5,11)(2,8,14,4,10,16,6,12)(17,23,29,19,25,31,21,27)(18,24,30,20,26,32,22,28), (1,26,9,18)(2,25,10,17)(3,24,11,32)(4,23,12,31)(5,22,13,30)(6,21,14,29)(7,20,15,28)(8,19,16,27), (1,27,9,19)(2,26,10,18)(3,25,11,17)(4,24,12,32)(5,23,13,31)(6,22,14,30)(7,21,15,29)(8,20,16,28), (1,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2)(17,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18), (1,21,9,29)(2,20,10,28)(3,19,11,27)(4,18,12,26)(5,17,13,25)(6,32,14,24)(7,31,15,23)(8,30,16,22), (1,12,7,2,13,8,3,14,9,4,15,10,5,16,11,6)(17,28,23,18,29,24,19,30,25,20,31,26,21,32,27,22), (1,23,9,31)(2,22,10,30)(3,21,11,29)(4,20,12,28)(5,19,13,27)(6,18,14,26)(7,17,15,25)(8,32,16,24), (1,28,9,20)(2,27,10,19)(3,26,11,18)(4,25,12,17)(5,24,13,32)(6,23,14,31)(7,22,15,30)(8,21,16,29), (1,13,9,5)(2,14,10,6)(3,15,11,7)(4,16,12,8)(17,29,25,21)(18,30,26,22)(19,31,27,23)(20,32,28,24), (1,15,13,11,9,7,5,3)(2,16,14,12,10,8,6,4)(17,31,29,27,25,23,21,19)(18,32,30,28,26,24,22,20), (1,22,9,30)(2,21,10,29)(3,20,11,28)(4,19,12,27)(5,18,13,26)(6,17,14,25)(7,32,15,24)(8,31,16,23), (1,14,11,8,5,2,15,12,9,6,3,16,13,10,7,4)(17,30,27,24,21,18,31,28,25,22,19,32,29,26,23,20)} over Symbolic Ring
#include "Brute-Raytracer.frag"
#group Algebraic
    
const int N = 16;
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]
uniform float JuliaVect5; slider[-2,0,2]
uniform float JuliaVect6; slider[-2,0,2]
uniform float JuliaVect7; slider[-2,0,2]
uniform float JuliaVect8; slider[-2,0,2]
uniform float JuliaVect9; slider[-2,0,2]
uniform float JuliaVect10; slider[-2,0,2]
uniform float JuliaVect11; slider[-2,0,2]
uniform float JuliaVect12; slider[-2,0,2]
uniform float JuliaVect13; slider[-2,0,2]
uniform float JuliaVect14; slider[-2,0,2]
uniform float JuliaVect15; slider[-2,0,2]
uniform float JuliaVect16; slider[-2,0,2]

uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]
uniform float Position5; slider[-2,0,2]
uniform float Position6; slider[-2,0,2]
uniform float Position7; slider[-2,0,2]
uniform float Position8; slider[-2,0,2]
uniform float Position9; slider[-2,0,2]
uniform float Position10; slider[-2,0,2]
uniform float Position11; slider[-2,0,2]
uniform float Position12; slider[-2,0,2]
uniform float Position13; slider[-2,0,2]
uniform float Position14; slider[-2,0,2]
uniform float Position15; slider[-2,0,2]
uniform float Position16; slider[-2,0,2]

uniform int FrameX; slider[1,1,16]
uniform int FrameY; slider[1,2,16]
uniform int FrameZ; slider[1,3,16]

// sign involutions
uniform int flipperA; slider[0,0,65536]
uniform int flipperB; slider[0,0,65536]
uniform int flipperC; slider[0,0,65536]



// extra parameters to play with (useful as weights)
uniform float auxA; slider[-2,1,2]
uniform float auxB; slider[-2,1,2]
uniform float auxC; slider[-2,1,2]
uniform float auxD; slider[-2,1,2]

// powers for multiplication, if need be
uniform int pow1; slider[0,1,24]
uniform int pow2; slider[0,1,24]
uniform int pow3; slider[0,1,24]
uniform int pow4; slider[0,1,24]

// ordinary fractal stuff
uniform int Iterations; slider[0,16,264]
uniform float Bailout; slider[0,2,4]
uniform float Bailin; slider[-4,-4,0]
uniform bool BailInvert; checkbox[false]
uniform bool Julia; checkbox[false]

// instead of adding the Julia point or z(0), use z(i-1) (the last point)
uniform bool usePrevious; checkbox[false]
    

float[N] product(float u[N], float v[N]) {
    return float[N](-u[10]*v[12] + u[10]*v[8] - u[11]*v[13] + u[11]*v[9] + u[12]*v[10] - u[12]*v[14] + u[13]*v[11] - u[13]*v[15] + u[14]*v[12] + u[15]*v[13] + u[1]*v[7] + u[2]*v[6] + u[3]*v[3] - u[3]*v[7] - u[4]*v[6] - u[5]*v[5] + u[6]*v[2] - u[6]*v[4] + u[7]*v[1] - u[7]*v[3] - u[8]*v[10] - u[9]*v[11], -u[10]*v[11] + u[10]*v[9] + u[11]*v[10] - u[11]*v[12] + u[12]*v[11] - u[12]*v[13] + u[13]*v[12] - u[13]*v[14] + u[14]*v[13] - u[14]*v[15] + u[15]*v[14] + u[2]*v[7] + u[3]*v[4] - u[3]*v[6] + u[4]*v[3] - u[4]*v[5] - u[5]*v[4] - u[6]*v[3] + u[7]*v[2] - u[8]*v[9] - u[9]*v[10] + u[9]*v[8], u[10]*v[10] + u[11]*v[11] + u[12]*v[12] + u[13]*v[13] + u[14]*v[14] + u[15]*v[15] - u[2]*v[2] + u[3]*v[5] + u[4]*v[4] + u[5]*v[3] + u[8]*v[8] + u[9]*v[9], -u[0]*v[7] + u[10]*v[13] + u[11]*v[14] - u[11]*v[8] + u[12]*v[15] - u[12]*v[9] - u[13]*v[10] - u[14]*v[11] - u[15]*v[12] - u[1]*v[6] - u[2]*v[5] + u[4]*v[7] - u[5]*v[2] + u[5]*v[6] - u[6]*v[1] + u[6]*v[5] - u[7]*v[0] + u[7]*v[4] + u[8]*v[11] + u[9]*v[12], u[0]*v[0] - u[0]*v[6] + u[10]*v[14] + u[11]*v[15] - u[12]*v[8] - u[13]*v[9] - u[14]*v[10] - u[15]*v[11] - u[1]*v[5] - u[2]*v[4] - u[4]*v[2] - u[5]*v[1] + u[5]*v[7] - u[6]*v[0] + u[6]*v[6] + u[7]*v[5] + u[8]*v[12] + u[9]*v[13], u[0]*v[1] - u[0]*v[5] + u[10]*v[15] - u[13]*v[8] - u[14]*v[9] - u[15]*v[10] + u[1]*v[0] - u[1]*v[4] - u[2]*v[3] - u[3]*v[2] - u[4]*v[1] - u[5]*v[0] + u[6]*v[7] + u[7]*v[6] + u[8]*v[13] + u[9]*v[14], u[0]*v[2] - u[0]*v[4] - u[14]*v[8] - u[15]*v[9] + u[1]*v[1] - u[1]*v[3] + u[2]*v[0] - u[3]*v[1] - u[4]*v[0] + u[7]*v[7] + u[8]*v[14] + u[9]*v[15], -u[0]*v[3] - u[15]*v[8] + u[1]*v[2] + u[2]*v[1] - u[3]*v[0] + u[8]*v[15], u[0]*v[14] - u[10]*v[0] + u[10]*v[6] + u[11]*v[5] + u[12]*v[4] + u[13]*v[3] + u[1]*v[15] - u[2]*v[8] - u[3]*v[11] - u[4]*v[12] - u[5]*v[13] - u[6]*v[14] - u[7]*v[15] - u[8]*v[2] - u[9]*v[1] + u[9]*v[7], u[0]*v[15] - u[10]*v[1] + u[10]*v[7] - u[11]*v[0] + u[11]*v[6] + u[12]*v[5] + u[13]*v[4] + u[14]*v[3] - u[1]*v[8] - u[2]*v[9] - u[3]*v[12] - u[4]*v[13] - u[5]*v[14] - u[6]*v[15] + u[7]*v[8] - u[9]*v[2], -u[0]*v[8] - u[10]*v[2] - u[11]*v[1] + u[11]*v[7] - u[12]*v[0] + u[12]*v[6] + u[13]*v[5] + u[14]*v[4] + u[15]*v[3] - u[1]*v[9] - u[2]*v[10] - u[3]*v[13] - u[4]*v[14] - u[5]*v[15] + u[6]*v[8] + u[7]*v[9], -u[0]*v[9] - u[11]*v[2] - u[12]*v[1] + u[12]*v[7] - u[13]*v[0] + u[13]*v[6] + u[14]*v[5] + u[15]*v[4] - u[1]*v[10] - u[2]*v[11] - u[3]*v[14] - u[4]*v[15] + u[5]*v[8] + u[6]*v[9] + u[7]*v[10] - u[8]*v[3], -u[0]*v[10] - u[12]*v[2] - u[13]*v[1] + u[13]*v[7] - u[14]*v[0] + u[14]*v[6] + u[15]*v[5] - u[1]*v[11] - u[2]*v[12] - u[3]*v[15] + u[4]*v[8] + u[5]*v[9] + u[6]*v[10] + u[7]*v[11] - u[8]*v[4] - u[9]*v[3], -u[0]*v[11] - u[10]*v[3] - u[13]*v[2] - u[14]*v[1] + u[14]*v[7] - u[15]*v[0] + u[15]*v[6] - u[1]*v[12] - u[2]*v[13] + u[3]*v[8] + u[4]*v[9] + u[5]*v[10] + u[6]*v[11] + u[7]*v[12] - u[8]*v[5] - u[9]*v[4], -u[0]*v[12] - u[10]*v[4] - u[11]*v[3] - u[14]*v[2] - u[15]*v[1] + u[15]*v[7] - u[1]*v[13] - u[2]*v[14] + u[3]*v[9] + u[4]*v[10] + u[5]*v[11] + u[6]*v[12] + u[7]*v[13] + u[8]*v[0] - u[8]*v[6] - u[9]*v[5], -u[0]*v[13] - u[10]*v[5] - u[11]*v[4] - u[12]*v[3] - u[15]*v[2] - u[1]*v[14] - u[2]*v[15] + u[3]*v[10] + u[4]*v[11] + u[5]*v[12] + u[6]*v[13] + u[7]*v[14] + u[8]*v[1] - u[8]*v[7] + u[9]*v[0] - u[9]*v[6]);
}


float norm(float u[N]) {
    return pow(pow(abs(u[0]), 2.0) + pow(abs(u[10]), 2.0) + pow(abs(u[11]), 2.0) + pow(abs(u[12]), 2.0) + pow(abs(u[13]), 2.0) + pow(abs(u[14]), 2.0) + pow(abs(u[15]), 2.0) + pow(abs(u[1]), 2.0) + pow(abs(u[2]), 2.0) + pow(abs(u[3]), 2.0) + pow(abs(u[4]), 2.0) + pow(abs(u[5]), 2.0) + pow(abs(u[6]), 2.0) + pow(abs(u[7]), 2.0) + pow(abs(u[8]), 2.0) + pow(abs(u[9]), 2.0), 0.5);
}

float[N] zero() {
  float zero[N];
  for(int i=0; i<N; ++i){zero[i] = 0;}
  return zero;
}

float[N] mul(float u[N], float v[N]) {
  return product(u,v);
}

float[N] mul(float a, float b[N]){
  float result[N];
  for (int i = 0; i < N; ++i){
    result[i] = a*b[i];
  }
  return result;
}

float[N] mul(float b[N], float a) {
  return mul(a,b);
}

float[N] mul(int a, float b[N]) {
  return mul(float(a),b);
}

float[N] mul(float b[N], int a) {
  return mul(float(a),b);
}

float[N] mul3(float a[N], float b[N], float c[N]) {
  return mul(mul(a,b),c);
}

float[N] pwr(float a[N],int n) {
  // multiple a by itself n times: a -> a**n
	float r[N] = a;
	for (int i=0;i<n-1;i++){
	   r = mul(r,a);
    }
    return r;
}

float[N] add(float a[N], float b[N]) {
  float c[N];
  for (int i = 0; i < N; ++i){
    c[i] = a[i]+b[i];
  }
  return c;
}

float[N] sub(float a[N], float b[N]) {
  float c[N];
  for (int i = 0; i < N; ++i){
    c[i] = a[i]-b[i];
  }
  return c;
}


float[N] loadParamsJuliaVect(out float u[N]){
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; u[5] = JuliaVect6; u[6] = JuliaVect7; u[7] = JuliaVect8; u[8] = JuliaVect9; u[9] = JuliaVect10; u[10] = JuliaVect11; u[11] = JuliaVect12; u[12] = JuliaVect13; u[13] = JuliaVect14; u[14] = JuliaVect15; u[15] = JuliaVect16; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; u[5] = Position6; u[6] = Position7; u[7] = Position8; u[8] = Position9; u[9] = Position10; u[10] = Position11; u[11] = Position12; u[12] = Position13; u[13] = Position14; u[14] = Position15; u[15] = Position16; 
    return u;
}


float[N] frame(float v[N], vec3 p){
    // "Frame" a "window" through which to view vector v, via a "subvector" p.

    // Points p form a linear subspace of the N dimensional Euclidean space,
    // but not necessarily of the vector space we are looking at.  They are
    // really just "slices" of larger vectors.

    if(FrameX == FrameY || FrameX == FrameZ || FrameY == FrameZ) {
        return v; //error, please set frame indices to be different
    }
    for(int i = 0; i<N; i++) {
       if (i == FrameX-1) { v[i] = p[0]; }
        if (i == FrameY-1) { v[i] = p[1]; }
        if (i == FrameZ-1) { v[i] = p[2]; }
    }
return v;
}


float[N] flip(in float A[N], int flipper) {
  for (int i=0; i< N; i++) {
    float p = pow(2.0,float(i));
    int place = int(p);
    int sgn = 1-2*((flipper & place) >> i);
    A[i] = sgn*A[i];
  }
    return A;
}

float[N] flipA(float z[N]) {
  return flip(z,flipperA);
}
float[N] flipB(float z[N]) {
  return flip(z,flipperB);
}
float[N] flipC(float z[N]) {
  return flip(z,flipperC);
}
    

float O[N];
float JuliaVect[N];

void init(){
    loadParamsPosition(O);
    loadParamsJuliaVect(JuliaVect);
    
}

void iter(inout float z[N]) {
    
    z = mul(
        pwr(flipA(z),pow1),
        pwr(flipB(z),pow2)
    );
    
}
    
bool inside(vec3 pt) {
    float z[N] = frame(O,pt);
    float z0[N] = z;
  	float r;
  	int i=0;
  	r=abs(norm(z));

    while(r<Bailout && (i<Iterations)) {
      float zprev[N];
      if (usePrevious) { zprev = z; } else { zprev = z0; }
  		iter(z);
  		z = add(z,(Julia ? JuliaVect : zprev));
  		r=norm(z);
  		i++;
  	}
	return ((r < Bailout && r > Bailin) || BailInvert);
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
