#version 130
#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 20

#info 6 real-dimensional algebra of 3 dimensional finite field over the complex numbers
#include "Brute-Raytracer.frag"
#group Algebraic
    
const int N = 6;
uniform float RotateFrom1; slider[-2,0,2]
uniform float RotateFrom2; slider[-2,0,2]
uniform float RotateFrom3; slider[-2,0,2]
uniform float RotateFrom4; slider[-2,0,2]
uniform float RotateFrom5; slider[-2,0,2]
uniform float RotateFrom6; slider[-2,0,2]

uniform float RotateTo1; slider[-2,0,2]
uniform float RotateTo2; slider[-2,0,2]
uniform float RotateTo3; slider[-2,0,2]
uniform float RotateTo4; slider[-2,0,2]
uniform float RotateTo5; slider[-2,0,2]
uniform float RotateTo6; slider[-2,0,2]

uniform float rotationAngle; slider[-1,0,1]
uniform bool enableRotation; checkbox[false]
uniform float rotationRate; slider[-0.2,0,0.2]

uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]
uniform float JuliaVect5; slider[-2,0,2]
uniform float JuliaVect6; slider[-2,0,2]

uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]
uniform float Position5; slider[-2,0,2]
uniform float Position6; slider[-2,0,2]

uniform int FrameX; slider[1,1,6]
uniform int FrameY; slider[1,2,6]
uniform int FrameZ; slider[1,3,6]

// sign involutions
uniform int flipperA; slider[0,0,64]
uniform int flipperB; slider[0,0,64]
uniform int flipperC; slider[0,0,64]



uniform float time;

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
    

float[N] zeroN() {
  float zero[N];
  for(int i=0; i<N; ++i){zero[i] = 0;}
  return zero;
}

float[N] unitN(int i) {
  float[N] unit = zeroN();
  unit[i] = 1;
  return unit;
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



float pNormSq(float u[N], float p) {
    float normSq = 0;
    for(int i=0; i<N; i++){
        normSq = normSq + pow(abs(u[i]),p);
    }
    return normSq;
}

float pNorm(float u[N], float p) {
    return pow(pNormSq(u,p),1.0/p);
}

float norm(float u[N]) {
    return pNorm(u,2.0);
}

float[N] normalize(inout float u[N]) {
    float nrm = norm(u);
    for(int i=0; i<N; i++){
        u[i] = u[i]/nrm;
    }
    return u;
}


float[N] mul(float u[N], float v[N]) {
    return float[N](u[0]*v[0] + u[0]*v[2] + u[0]*v[4] - u[1]*v[1] - u[1]*v[3] - u[1]*v[5] + u[2]*v[0] - u[3]*v[1] + u[4]*v[0] - u[5]*v[1], u[0]*v[1] + u[0]*v[3] + u[0]*v[5] + u[1]*v[0] + u[1]*v[2] + u[1]*v[4] + u[2]*v[1] + u[3]*v[0] + u[4]*v[1] + u[5]*v[0], u[2]*v[2] - u[3]*v[3] + u[4]*v[4] - u[5]*v[5], u[2]*v[3] + u[3]*v[2] + u[4]*v[5] + u[5]*v[4], u[2]*v[4] - u[3]*v[5] + u[4]*v[2] - u[5]*v[3], u[2]*v[5] + u[3]*v[4] + u[4]*v[3] + u[5]*v[2]);
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

float[N] pwr(float a[N],int n) {
  // multiple a by itself n times: a -> a**n
	float r[N] = a;
	for (int i=0;i<n-1;i++){
	   r = mul(r,a);
    }
    return r;
}

float[N] mul3(float a[N], float b[N], float c[N]) {
  return mul(mul(a,b),c);
}

float[N] loadParamsRotateFrom(out float u[N]){
    u[0] = RotateFrom1; u[1] = RotateFrom2; u[2] = RotateFrom3; u[3] = RotateFrom4; u[4] = RotateFrom5; u[5] = RotateFrom6; 
    return u;
}


float[N] loadParamsRotateTo(out float u[N]){
    u[0] = RotateTo1; u[1] = RotateTo2; u[2] = RotateTo3; u[3] = RotateTo4; u[4] = RotateTo5; u[5] = RotateTo6; 
    return u;
}

float[N] RotateFrom;
float[N] RotateTo;


float[N] rotate(float v[N], float fr[N], float to[N], float angle) {
  float sin_th = sin(angle*2*PI);
  float cos_th = cos(angle*2*PI);
  
  return float[N]((v[0]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(4*fr[0]*fr[1]*to[0]*to[1] + 4*fr[0]*fr[2]*to[0]*to[2] + 4*fr[0]*fr[3]*to[0]*to[3] + 4*fr[0]*fr[4]*to[0]*to[4] + 4*fr[0]*fr[5]*to[0]*to[5] + pow(to[0], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)) - pow(to[1], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)) - pow(to[2], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)) - pow(to[3], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)) - pow(to[4], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)) - pow(to[5], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)))) - 2*v[1]*(cos_th*sin_th*(-fr[0]*to[1] + fr[1]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[1]*pow(to[0], 2.0) - fr[0]*fr[1]*pow(to[1], 2.0) + fr[0]*fr[1]*pow(to[2], 2.0) + fr[0]*fr[1]*pow(to[3], 2.0) + fr[0]*fr[1]*pow(to[4], 2.0) + fr[0]*fr[1]*pow(to[5], 2.0) - 2*fr[0]*fr[2]*to[1]*to[2] - 2*fr[0]*fr[3]*to[1]*to[3] - 2*fr[0]*fr[4]*to[1]*to[4] - 2*fr[0]*fr[5]*to[1]*to[5] - to[0]*to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0)))) - 2*v[2]*(cos_th*sin_th*(-fr[0]*to[2] + fr[2]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[2]*pow(to[0], 2.0) + fr[0]*fr[2]*pow(to[1], 2.0) - fr[0]*fr[2]*pow(to[2], 2.0) + fr[0]*fr[2]*pow(to[3], 2.0) + fr[0]*fr[2]*pow(to[4], 2.0) + fr[0]*fr[2]*pow(to[5], 2.0) - 2*fr[0]*fr[3]*to[2]*to[3] - 2*fr[0]*fr[4]*to[2]*to[4] - 2*fr[0]*fr[5]*to[2]*to[5] - to[2]*(2*fr[0]*fr[1]*to[1] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0))))) - 2*v[3]*(cos_th*sin_th*(-fr[0]*to[3] + fr[3]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[3]*pow(to[0], 2.0) + fr[0]*fr[3]*pow(to[1], 2.0) + fr[0]*fr[3]*pow(to[2], 2.0) - fr[0]*fr[3]*pow(to[3], 2.0) + fr[0]*fr[3]*pow(to[4], 2.0) + fr[0]*fr[3]*pow(to[5], 2.0) - 2*fr[0]*fr[4]*to[3]*to[4] - 2*fr[0]*fr[5]*to[3]*to[5] - to[3]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0))))) - 2*v[4]*(cos_th*sin_th*(-fr[0]*to[4] + fr[4]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[4]*pow(to[0], 2.0) + fr[0]*fr[4]*pow(to[1], 2.0) + fr[0]*fr[4]*pow(to[2], 2.0) + fr[0]*fr[4]*pow(to[3], 2.0) - fr[0]*fr[4]*pow(to[4], 2.0) + fr[0]*fr[4]*pow(to[5], 2.0) - 2*fr[0]*fr[5]*to[4]*to[5] - to[4]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + 2*fr[0]*fr[3]*to[3] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[0]*to[5] + fr[5]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[5]*pow(to[0], 2.0) + fr[0]*fr[5]*pow(to[1], 2.0) + fr[0]*fr[5]*pow(to[2], 2.0) + fr[0]*fr[5]*pow(to[3], 2.0) + fr[0]*fr[5]*pow(to[4], 2.0) - fr[0]*fr[5]*pow(to[5], 2.0) - to[5]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + 2*fr[0]*fr[3]*to[3] + 2*fr[0]*fr[4]*to[4] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[1] + fr[1]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[1]*pow(to[0], 2.0) - fr[0]*fr[1]*pow(to[1], 2.0) - fr[0]*fr[1]*pow(to[2], 2.0) - fr[0]*fr[1]*pow(to[3], 2.0) - fr[0]*fr[1]*pow(to[4], 2.0) - fr[0]*fr[1]*pow(to[5], 2.0) + 2*fr[1]*fr[2]*to[0]*to[2] + 2*fr[1]*fr[3]*to[0]*to[3] + 2*fr[1]*fr[4]*to[0]*to[4] + 2*fr[1]*fr[5]*to[0]*to[5] - to[0]*to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + v[1]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(4*fr[0]*fr[1]*to[0]*to[1] + 4*fr[1]*fr[2]*to[1]*to[2] + 4*fr[1]*fr[3]*to[1]*to[3] + 4*fr[1]*fr[4]*to[1]*to[4] + 4*fr[1]*fr[5]*to[1]*to[5] + pow(to[0], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) - pow(to[1], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) - 2*v[2]*(cos_th*sin_th*(-fr[1]*to[2] + fr[2]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[2]*pow(to[0], 2.0) + fr[1]*fr[2]*pow(to[1], 2.0) - fr[1]*fr[2]*pow(to[2], 2.0) + fr[1]*fr[2]*pow(to[3], 2.0) + fr[1]*fr[2]*pow(to[4], 2.0) + fr[1]*fr[2]*pow(to[5], 2.0) - 2*fr[1]*fr[3]*to[2]*to[3] - 2*fr[1]*fr[4]*to[2]*to[4] - 2*fr[1]*fr[5]*to[2]*to[5] - to[2]*(2*fr[0]*fr[1]*to[0] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))) - 2*v[3]*(cos_th*sin_th*(-fr[1]*to[3] + fr[3]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[3]*pow(to[0], 2.0) + fr[1]*fr[3]*pow(to[1], 2.0) + fr[1]*fr[3]*pow(to[2], 2.0) - fr[1]*fr[3]*pow(to[3], 2.0) + fr[1]*fr[3]*pow(to[4], 2.0) + fr[1]*fr[3]*pow(to[5], 2.0) - 2*fr[1]*fr[4]*to[3]*to[4] - 2*fr[1]*fr[5]*to[3]*to[5] - to[3]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))) - 2*v[4]*(cos_th*sin_th*(-fr[1]*to[4] + fr[4]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[4]*pow(to[0], 2.0) + fr[1]*fr[4]*pow(to[1], 2.0) + fr[1]*fr[4]*pow(to[2], 2.0) + fr[1]*fr[4]*pow(to[3], 2.0) - fr[1]*fr[4]*pow(to[4], 2.0) + fr[1]*fr[4]*pow(to[5], 2.0) - 2*fr[1]*fr[5]*to[4]*to[5] - to[4]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] + 2*fr[1]*fr[3]*to[3] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[1]*to[5] + fr[5]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[5]*pow(to[0], 2.0) + fr[1]*fr[5]*pow(to[1], 2.0) + fr[1]*fr[5]*pow(to[2], 2.0) + fr[1]*fr[5]*pow(to[3], 2.0) + fr[1]*fr[5]*pow(to[4], 2.0) - fr[1]*fr[5]*pow(to[5], 2.0) - to[5]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] + 2*fr[1]*fr[3]*to[3] + 2*fr[1]*fr[4]*to[4] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[2] + fr[2]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[2]*pow(to[0], 2.0) - fr[0]*fr[2]*pow(to[1], 2.0) - fr[0]*fr[2]*pow(to[2], 2.0) - fr[0]*fr[2]*pow(to[3], 2.0) - fr[0]*fr[2]*pow(to[4], 2.0) - fr[0]*fr[2]*pow(to[5], 2.0) + 2*fr[1]*fr[2]*to[0]*to[1] + 2*fr[2]*fr[3]*to[0]*to[3] + 2*fr[2]*fr[4]*to[0]*to[4] + 2*fr[2]*fr[5]*to[0]*to[5] - to[0]*to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[2] + fr[2]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[2]*to[0]*to[1] + fr[1]*fr[2]*pow(to[0], 2.0) - fr[1]*fr[2]*pow(to[1], 2.0) + fr[1]*fr[2]*pow(to[2], 2.0) + fr[1]*fr[2]*pow(to[3], 2.0) + fr[1]*fr[2]*pow(to[4], 2.0) + fr[1]*fr[2]*pow(to[5], 2.0) - 2*fr[2]*fr[3]*to[1]*to[3] - 2*fr[2]*fr[4]*to[1]*to[4] - 2*fr[2]*fr[5]*to[1]*to[5] + to[1]*to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + v[2]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(4*fr[2]*fr[3]*to[2]*to[3] + 4*fr[2]*fr[4]*to[2]*to[4] + 4*fr[2]*fr[5]*to[2]*to[5] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) - pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + 4*to[2]*(fr[0]*fr[2]*to[0] + fr[1]*fr[2]*to[1]) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) - 2*v[3]*(cos_th*sin_th*(-fr[2]*to[3] + fr[3]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[3]*pow(to[0], 2.0) + fr[2]*fr[3]*pow(to[1], 2.0) + fr[2]*fr[3]*pow(to[2], 2.0) - fr[2]*fr[3]*pow(to[3], 2.0) + fr[2]*fr[3]*pow(to[4], 2.0) + fr[2]*fr[3]*pow(to[5], 2.0) - 2*fr[2]*fr[4]*to[3]*to[4] - 2*fr[2]*fr[5]*to[3]*to[5] - to[3]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))) - 2*v[4]*(cos_th*sin_th*(-fr[2]*to[4] + fr[4]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[4]*pow(to[0], 2.0) + fr[2]*fr[4]*pow(to[1], 2.0) + fr[2]*fr[4]*pow(to[2], 2.0) + fr[2]*fr[4]*pow(to[3], 2.0) - fr[2]*fr[4]*pow(to[4], 2.0) + fr[2]*fr[4]*pow(to[5], 2.0) - 2*fr[2]*fr[5]*to[4]*to[5] - to[4]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] + 2*fr[2]*fr[3]*to[3] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[2]*to[5] + fr[5]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[5]*pow(to[0], 2.0) + fr[2]*fr[5]*pow(to[1], 2.0) + fr[2]*fr[5]*pow(to[2], 2.0) + fr[2]*fr[5]*pow(to[3], 2.0) + fr[2]*fr[5]*pow(to[4], 2.0) - fr[2]*fr[5]*pow(to[5], 2.0) - to[5]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] + 2*fr[2]*fr[3]*to[3] + 2*fr[2]*fr[4]*to[4] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[3] + fr[3]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[3]*pow(to[0], 2.0) - fr[0]*fr[3]*pow(to[1], 2.0) - fr[0]*fr[3]*pow(to[2], 2.0) - fr[0]*fr[3]*pow(to[3], 2.0) - fr[0]*fr[3]*pow(to[4], 2.0) - fr[0]*fr[3]*pow(to[5], 2.0) + 2*fr[1]*fr[3]*to[0]*to[1] + 2*fr[2]*fr[3]*to[0]*to[2] + 2*fr[3]*fr[4]*to[0]*to[4] + 2*fr[3]*fr[5]*to[0]*to[5] - to[0]*to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[3] + fr[3]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[3]*to[0]*to[1] + fr[1]*fr[3]*pow(to[0], 2.0) - fr[1]*fr[3]*pow(to[1], 2.0) + fr[1]*fr[3]*pow(to[2], 2.0) + fr[1]*fr[3]*pow(to[3], 2.0) + fr[1]*fr[3]*pow(to[4], 2.0) + fr[1]*fr[3]*pow(to[5], 2.0) - 2*fr[2]*fr[3]*to[1]*to[2] - 2*fr[3]*fr[4]*to[1]*to[4] - 2*fr[3]*fr[5]*to[1]*to[5] + to[1]*to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[3] + fr[3]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[3]*pow(to[0], 2.0) + fr[2]*fr[3]*pow(to[1], 2.0) - fr[2]*fr[3]*pow(to[2], 2.0) + fr[2]*fr[3]*pow(to[3], 2.0) + fr[2]*fr[3]*pow(to[4], 2.0) + fr[2]*fr[3]*pow(to[5], 2.0) - 2*fr[3]*fr[4]*to[2]*to[4] - 2*fr[3]*fr[5]*to[2]*to[5] + to[2]*to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) - 2*to[2]*(fr[0]*fr[3]*to[0] + fr[1]*fr[3]*to[1]))) + v[3]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(4*fr[3]*fr[4]*to[3]*to[4] + 4*fr[3]*fr[5]*to[3]*to[5] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) - pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + 4*to[3]*(fr[0]*fr[3]*to[0] + fr[1]*fr[3]*to[1] + fr[2]*fr[3]*to[2]) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))) - 2*v[4]*(cos_th*sin_th*(-fr[3]*to[4] + fr[4]*to[3]) + pow(sin_th, 2.0)*(fr[3]*fr[4]*pow(to[0], 2.0) + fr[3]*fr[4]*pow(to[1], 2.0) + fr[3]*fr[4]*pow(to[2], 2.0) + fr[3]*fr[4]*pow(to[3], 2.0) - fr[3]*fr[4]*pow(to[4], 2.0) + fr[3]*fr[4]*pow(to[5], 2.0) - 2*fr[3]*fr[5]*to[4]*to[5] - to[4]*(2*fr[0]*fr[3]*to[0] + 2*fr[1]*fr[3]*to[1] + 2*fr[2]*fr[3]*to[2] - to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[3]*to[5] + fr[5]*to[3]) + pow(sin_th, 2.0)*(fr[3]*fr[5]*pow(to[0], 2.0) + fr[3]*fr[5]*pow(to[1], 2.0) + fr[3]*fr[5]*pow(to[2], 2.0) + fr[3]*fr[5]*pow(to[3], 2.0) + fr[3]*fr[5]*pow(to[4], 2.0) - fr[3]*fr[5]*pow(to[5], 2.0) - to[5]*(2*fr[0]*fr[3]*to[0] + 2*fr[1]*fr[3]*to[1] + 2*fr[2]*fr[3]*to[2] + 2*fr[3]*fr[4]*to[4] - to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[4] + fr[4]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[4]*pow(to[0], 2.0) - fr[0]*fr[4]*pow(to[1], 2.0) - fr[0]*fr[4]*pow(to[2], 2.0) - fr[0]*fr[4]*pow(to[3], 2.0) - fr[0]*fr[4]*pow(to[4], 2.0) - fr[0]*fr[4]*pow(to[5], 2.0) + 2*fr[1]*fr[4]*to[0]*to[1] + 2*fr[2]*fr[4]*to[0]*to[2] + 2*fr[3]*fr[4]*to[0]*to[3] + 2*fr[4]*fr[5]*to[0]*to[5] - to[0]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[4] + fr[4]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[4]*to[0]*to[1] + fr[1]*fr[4]*pow(to[0], 2.0) - fr[1]*fr[4]*pow(to[1], 2.0) + fr[1]*fr[4]*pow(to[2], 2.0) + fr[1]*fr[4]*pow(to[3], 2.0) + fr[1]*fr[4]*pow(to[4], 2.0) + fr[1]*fr[4]*pow(to[5], 2.0) - 2*fr[2]*fr[4]*to[1]*to[2] - 2*fr[3]*fr[4]*to[1]*to[3] - 2*fr[4]*fr[5]*to[1]*to[5] + to[1]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[4] + fr[4]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[4]*pow(to[0], 2.0) + fr[2]*fr[4]*pow(to[1], 2.0) - fr[2]*fr[4]*pow(to[2], 2.0) + fr[2]*fr[4]*pow(to[3], 2.0) + fr[2]*fr[4]*pow(to[4], 2.0) + fr[2]*fr[4]*pow(to[5], 2.0) - 2*fr[3]*fr[4]*to[2]*to[3] - 2*fr[4]*fr[5]*to[2]*to[5] + to[2]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) - 2*to[2]*(fr[0]*fr[4]*to[0] + fr[1]*fr[4]*to[1]))) + 2*v[3]*(cos_th*sin_th*(-fr[3]*to[4] + fr[4]*to[3]) - pow(sin_th, 2.0)*(fr[3]*fr[4]*pow(to[0], 2.0) + fr[3]*fr[4]*pow(to[1], 2.0) + fr[3]*fr[4]*pow(to[2], 2.0) - fr[3]*fr[4]*pow(to[3], 2.0) + fr[3]*fr[4]*pow(to[4], 2.0) + fr[3]*fr[4]*pow(to[5], 2.0) - 2*fr[4]*fr[5]*to[3]*to[5] + to[3]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) - 2*to[3]*(fr[0]*fr[4]*to[0] + fr[1]*fr[4]*to[1] + fr[2]*fr[4]*to[2]))) + v[4]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(4*fr[4]*fr[5]*to[4]*to[5] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) - pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)) + 4*to[4]*(fr[0]*fr[4]*to[0] + fr[1]*fr[4]*to[1] + fr[2]*fr[4]*to[2] + fr[3]*fr[4]*to[3]) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0)))) - 2*v[5]*(cos_th*sin_th*(-fr[4]*to[5] + fr[5]*to[4]) + pow(sin_th, 2.0)*(fr[4]*fr[5]*pow(to[0], 2.0) + fr[4]*fr[5]*pow(to[1], 2.0) + fr[4]*fr[5]*pow(to[2], 2.0) + fr[4]*fr[5]*pow(to[3], 2.0) + fr[4]*fr[5]*pow(to[4], 2.0) - fr[4]*fr[5]*pow(to[5], 2.0) - to[5]*(2*fr[0]*fr[4]*to[0] + 2*fr[1]*fr[4]*to[1] + 2*fr[2]*fr[4]*to[2] + 2*fr[3]*fr[4]*to[3] - to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[5] + fr[5]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[5]*pow(to[0], 2.0) - fr[0]*fr[5]*pow(to[1], 2.0) - fr[0]*fr[5]*pow(to[2], 2.0) - fr[0]*fr[5]*pow(to[3], 2.0) - fr[0]*fr[5]*pow(to[4], 2.0) - fr[0]*fr[5]*pow(to[5], 2.0) + 2*fr[1]*fr[5]*to[0]*to[1] + 2*fr[2]*fr[5]*to[0]*to[2] + 2*fr[3]*fr[5]*to[0]*to[3] + 2*fr[4]*fr[5]*to[0]*to[4] - to[0]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[5] + fr[5]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[5]*to[0]*to[1] + fr[1]*fr[5]*pow(to[0], 2.0) - fr[1]*fr[5]*pow(to[1], 2.0) + fr[1]*fr[5]*pow(to[2], 2.0) + fr[1]*fr[5]*pow(to[3], 2.0) + fr[1]*fr[5]*pow(to[4], 2.0) + fr[1]*fr[5]*pow(to[5], 2.0) - 2*fr[2]*fr[5]*to[1]*to[2] - 2*fr[3]*fr[5]*to[1]*to[3] - 2*fr[4]*fr[5]*to[1]*to[4] + to[1]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[5] + fr[5]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[5]*pow(to[0], 2.0) + fr[2]*fr[5]*pow(to[1], 2.0) - fr[2]*fr[5]*pow(to[2], 2.0) + fr[2]*fr[5]*pow(to[3], 2.0) + fr[2]*fr[5]*pow(to[4], 2.0) + fr[2]*fr[5]*pow(to[5], 2.0) - 2*fr[3]*fr[5]*to[2]*to[3] - 2*fr[4]*fr[5]*to[2]*to[4] + to[2]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) - 2*to[2]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1]))) + 2*v[3]*(cos_th*sin_th*(-fr[3]*to[5] + fr[5]*to[3]) - pow(sin_th, 2.0)*(fr[3]*fr[5]*pow(to[0], 2.0) + fr[3]*fr[5]*pow(to[1], 2.0) + fr[3]*fr[5]*pow(to[2], 2.0) - fr[3]*fr[5]*pow(to[3], 2.0) + fr[3]*fr[5]*pow(to[4], 2.0) + fr[3]*fr[5]*pow(to[5], 2.0) - 2*fr[4]*fr[5]*to[3]*to[4] + to[3]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) - 2*to[3]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1] + fr[2]*fr[5]*to[2]))) + 2*v[4]*(cos_th*sin_th*(-fr[4]*to[5] + fr[5]*to[4]) - pow(sin_th, 2.0)*(fr[4]*fr[5]*pow(to[0], 2.0) + fr[4]*fr[5]*pow(to[1], 2.0) + fr[4]*fr[5]*pow(to[2], 2.0) + fr[4]*fr[5]*pow(to[3], 2.0) - fr[4]*fr[5]*pow(to[4], 2.0) + fr[4]*fr[5]*pow(to[5], 2.0) + to[4]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) - 2*to[4]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1] + fr[2]*fr[5]*to[2] + fr[3]*fr[5]*to[3]))) + v[5]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) - pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0)) + 4*to[5]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1] + fr[2]*fr[5]*to[2] + fr[3]*fr[5]*to[3] + fr[4]*fr[5]*to[4]))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0)))));
}


float[N] loadParamsJuliaVect(out float u[N]){
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; u[5] = JuliaVect6; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; u[5] = Position6; 
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
    
    if(enableRotation){v = rotate(v,RotateFrom,RotateTo,rotationAngle+time*rotationRate);};

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
    
    loadParamsRotateFrom(RotateFrom);
    normalize(RotateFrom);
    loadParamsRotateTo(RotateTo);
    normalize(RotateTo);

    loadParamsPosition(O);
    loadParamsJuliaVect(JuliaVect);
    
}

void iter(inout float z[N]) {
    
    z = mul(
        pwr(flipA(z),pow1),
        pwr(flipB(z),pow2)
    );
    //z = mul3(
    //    pwr(flipA(z),pow1),
    //    pwr(flipB(z),pow2),
    //    pwr(flipC(z),pow3)
    //);
    
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
Far = 10
#endpreset
