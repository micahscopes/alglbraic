#version 130
#define providesInside
#define providesInit
#define providesColor
#define SubframeMax 9
#define IterationsBetweenRedraws 30

#info Clifford Algebra with signature [-1,-1,-1]
#include "Brute-Raytracer.frag"
#group Fractal
    
const int <alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8> = 8;
#group Rotation
uniform float RotateFrom1; slider[-2,0,2]
uniform float RotateFrom2; slider[-2,0,2]
uniform float RotateFrom3; slider[-2,0,2]
uniform float RotateFrom4; slider[-2,0,2]
uniform float RotateFrom5; slider[-2,0,2]
uniform float RotateFrom6; slider[-2,0,2]
uniform float RotateFrom7; slider[-2,0,2]
uniform float RotateFrom8; slider[-2,0,2]

uniform float RotateTo1; slider[-2,0,2]
uniform float RotateTo2; slider[-2,0,2]
uniform float RotateTo3; slider[-2,0,2]
uniform float RotateTo4; slider[-2,0,2]
uniform float RotateTo5; slider[-2,0,2]
uniform float RotateTo6; slider[-2,0,2]
uniform float RotateTo7; slider[-2,0,2]
uniform float RotateTo8; slider[-2,0,2]

uniform float rotationAngle; slider[-1,0,1]
uniform bool enableRotation; checkbox[false]
uniform float rotationRate; slider[-0.2,0,0.2]

#group Fractal

#group Julia
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]
uniform float JuliaVect5; slider[-2,0,2]
uniform float JuliaVect6; slider[-2,0,2]
uniform float JuliaVect7; slider[-2,0,2]
uniform float JuliaVect8; slider[-2,0,2]

#group Fractal


#group Window
uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]
uniform float Position5; slider[-2,0,2]
uniform float Position6; slider[-2,0,2]
uniform float Position7; slider[-2,0,2]
uniform float Position8; slider[-2,0,2]

#group Fractal


#group Window
uniform int FrameX; slider[1,1,8]
uniform int FrameY; slider[1,2,8]
uniform int FrameZ; slider[1,3,8]
#group Fractal


// sign involutions
uniform int flipperA; slider[0,0,256]
uniform int flipperB; slider[0,0,256]
uniform int flipperC; slider[0,0,256]



uniform float time;

// powers for multiplication, if need be
uniform int pow1; slider[0,1,24]
uniform int pow2; slider[0,1,24]
uniform int pow3; slider[0,1,24]
uniform int pow4; slider[0,1,24]

// ordinary fractal stuff
uniform int Iterations; slider[0,16,264]
uniform int ColorIterations; slider[0,16,264]
uniform float Bailout; slider[0,2,4]
uniform float Bailin; slider[-4,-4,0]
uniform bool BailInvert; checkbox[false]
uniform bool Julia; checkbox[false]

// instead of adding the Julia point or z(0), use z(i-1) (the last point)
uniform bool addInitial; checkbox[true]
uniform bool addPrevious; checkbox[false]
uniform bool addJulia; checkbox[false]
    

float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] zero<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>() {
  float zero[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>];
  for(int i=0; i<<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>; ++i){zero[i] = 0;}
  return zero;
}

float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] unit<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>(int i) {
  float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] unit = zero<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>();
  unit[i] = 1;
  return unit;
}

float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] add(float a[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float b[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>]) {
  float c[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>];
  for (int i = 0; i < <alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>; ++i){
    c[i] = a[i]+b[i];
  }
  return c;
}

float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] sub(float a[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float b[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>]) {
  float c[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>];
  for (int i = 0; i < <alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>; ++i){
    c[i] = a[i]-b[i];
  }
  return c;
}



float pNormSq(float u[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float p) {
    float normSq = 0;
    for(int i=0; i<<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>; i++){
        normSq = normSq + pow(abs(u[i]),p);
    }
    return normSq;
}

float pNorm(float u[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float p) {
    return pow(pNormSq(u,p),1.0/p);
}

float norm(float u[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>]) {
    return pNorm(u,2.0);
}

float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] normalize(inout float u[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>]) {
    float nrm = norm(u);
    for(int i=0; i<<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>; i++){
        u[i] = u[i]/nrm;
    }
    return u;
}


float[N] product(float u[N], float v[N]) {
    return float[N](u[0]*v[0] - 1.0*u[1]*v[1] - 1.0*u[2]*v[2] + u[3]*v[3] - 1.0*u[4]*v[4] - 1.0*u[5]*v[5] - 1.0*u[6]*v[6] - 1.0*u[7]*v[7], u[0]*v[1] + u[1]*v[0] - 1.0*u[2]*v[5] - 1.0*u[3]*v[6] - 1.0*u[4]*v[7] + u[5]*v[2] - 1.0*u[6]*v[3] + u[7]*v[4], u[0]*v[2] + u[1]*v[5] + u[2]*v[0] - 1.0*u[3]*v[7] + u[4]*v[6] - u[5]*v[1] - u[6]*v[4] - 1.0*u[7]*v[3], u[0]*v[3] + u[1]*v[6] + u[2]*v[7] + u[3]*v[0] - u[4]*v[5] - u[5]*v[4] + u[6]*v[1] + u[7]*v[2], u[0]*v[4] + u[1]*v[7] - 1.0*u[2]*v[6] + u[3]*v[5] + u[4]*v[0] + u[5]*v[3] + u[6]*v[2] - u[7]*v[1], u[0]*v[5] - 1.0*u[1]*v[2] + u[2]*v[1] + u[3]*v[4] + u[4]*v[3] + u[5]*v[0] - 1.0*u[6]*v[7] + u[7]*v[6], u[0]*v[6] - 1.0*u[1]*v[3] + u[2]*v[4] - 1.0*u[3]*v[1] - 1.0*u[4]*v[2] + u[5]*v[7] + u[6]*v[0] - u[7]*v[5], u[0]*v[7] - 1.0*u[1]*v[4] - 1.0*u[2]*v[3] - 1.0*u[3]*v[2] + u[4]*v[1] - 1.0*u[5]*v[6] + u[6]*v[5] + u[7]*v[0]);
}


float[N] loadParamsRotateFrom(out float u[N]){
    u[0] = RotateFrom1; u[1] = RotateFrom2; u[2] = RotateFrom3; u[3] = RotateFrom4; u[4] = RotateFrom5; u[5] = RotateFrom6; u[6] = RotateFrom7; u[7] = RotateFrom8; 
    return u;
}


float[N] loadParamsRotateTo(out float u[N]){
    u[0] = RotateTo1; u[1] = RotateTo2; u[2] = RotateTo3; u[3] = RotateTo4; u[4] = RotateTo5; u[5] = RotateTo6; u[6] = RotateTo7; u[7] = RotateTo8; 
    return u;
}

float[N] RotateFrom;
float[N] RotateTo;


float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>] rotate(float v[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float fr[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float to[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>], float angle) {
  float sin_th = sin(angle*2*PI);
  float cos_th = cos(angle*2*PI);
  
  return float[<alglbraic.VectorOperation.VectorOperation instance at 0x7f86f90d1ea8>]((v[0]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[0]*fr[1]*to[0]*to[1] + 4*fr[0]*fr[2]*to[0]*to[2] + 4*fr[0]*fr[3]*to[0]*to[3] + 4*fr[0]*fr[4]*to[0]*to[4] + 4*fr[0]*fr[5]*to[0]*to[5] + 4*fr[0]*fr[6]*to[0]*to[6] + 4*fr[0]*fr[7]*to[0]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[1], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[2], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[3], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[4], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[5], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[6], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[7], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)))) - 2*v[1]*(cos_th*sin_th*(-fr[0]*to[1] + fr[1]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[1]*pow(to[0], 2.0) - fr[0]*fr[1]*pow(to[1], 2.0) + fr[0]*fr[1]*pow(to[2], 2.0) + fr[0]*fr[1]*pow(to[3], 2.0) + fr[0]*fr[1]*pow(to[4], 2.0) + fr[0]*fr[1]*pow(to[5], 2.0) + fr[0]*fr[1]*pow(to[6], 2.0) + fr[0]*fr[1]*pow(to[7], 2.0) - 2*fr[0]*fr[2]*to[1]*to[2] - 2*fr[0]*fr[3]*to[1]*to[3] - 2*fr[0]*fr[4]*to[1]*to[4] - 2*fr[0]*fr[5]*to[1]*to[5] - 2*fr[0]*fr[6]*to[1]*to[6] - 2*fr[0]*fr[7]*to[1]*to[7] - to[0]*to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0)))) - 2*v[2]*(cos_th*sin_th*(-fr[0]*to[2] + fr[2]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[2]*pow(to[0], 2.0) + fr[0]*fr[2]*pow(to[1], 2.0) - fr[0]*fr[2]*pow(to[2], 2.0) + fr[0]*fr[2]*pow(to[3], 2.0) + fr[0]*fr[2]*pow(to[4], 2.0) + fr[0]*fr[2]*pow(to[5], 2.0) + fr[0]*fr[2]*pow(to[6], 2.0) + fr[0]*fr[2]*pow(to[7], 2.0) - 2*fr[0]*fr[3]*to[2]*to[3] - 2*fr[0]*fr[4]*to[2]*to[4] - 2*fr[0]*fr[5]*to[2]*to[5] - 2*fr[0]*fr[6]*to[2]*to[6] - 2*fr[0]*fr[7]*to[2]*to[7] - to[2]*(2*fr[0]*fr[1]*to[1] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0))))) - 2*v[3]*(cos_th*sin_th*(-fr[0]*to[3] + fr[3]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[3]*pow(to[0], 2.0) + fr[0]*fr[3]*pow(to[1], 2.0) + fr[0]*fr[3]*pow(to[2], 2.0) - fr[0]*fr[3]*pow(to[3], 2.0) + fr[0]*fr[3]*pow(to[4], 2.0) + fr[0]*fr[3]*pow(to[5], 2.0) + fr[0]*fr[3]*pow(to[6], 2.0) + fr[0]*fr[3]*pow(to[7], 2.0) - 2*fr[0]*fr[4]*to[3]*to[4] - 2*fr[0]*fr[5]*to[3]*to[5] - 2*fr[0]*fr[6]*to[3]*to[6] - 2*fr[0]*fr[7]*to[3]*to[7] - to[3]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0))))) - 2*v[4]*(cos_th*sin_th*(-fr[0]*to[4] + fr[4]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[4]*pow(to[0], 2.0) + fr[0]*fr[4]*pow(to[1], 2.0) + fr[0]*fr[4]*pow(to[2], 2.0) + fr[0]*fr[4]*pow(to[3], 2.0) - fr[0]*fr[4]*pow(to[4], 2.0) + fr[0]*fr[4]*pow(to[5], 2.0) + fr[0]*fr[4]*pow(to[6], 2.0) + fr[0]*fr[4]*pow(to[7], 2.0) - 2*fr[0]*fr[5]*to[4]*to[5] - 2*fr[0]*fr[6]*to[4]*to[6] - 2*fr[0]*fr[7]*to[4]*to[7] - to[4]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + 2*fr[0]*fr[3]*to[3] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[0]*to[5] + fr[5]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[5]*pow(to[0], 2.0) + fr[0]*fr[5]*pow(to[1], 2.0) + fr[0]*fr[5]*pow(to[2], 2.0) + fr[0]*fr[5]*pow(to[3], 2.0) + fr[0]*fr[5]*pow(to[4], 2.0) - fr[0]*fr[5]*pow(to[5], 2.0) + fr[0]*fr[5]*pow(to[6], 2.0) + fr[0]*fr[5]*pow(to[7], 2.0) - 2*fr[0]*fr[6]*to[5]*to[6] - 2*fr[0]*fr[7]*to[5]*to[7] - to[5]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + 2*fr[0]*fr[3]*to[3] + 2*fr[0]*fr[4]*to[4] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0))))) - 2*v[6]*(cos_th*sin_th*(-fr[0]*to[6] + fr[6]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[6]*pow(to[0], 2.0) + fr[0]*fr[6]*pow(to[1], 2.0) + fr[0]*fr[6]*pow(to[2], 2.0) + fr[0]*fr[6]*pow(to[3], 2.0) + fr[0]*fr[6]*pow(to[4], 2.0) + fr[0]*fr[6]*pow(to[5], 2.0) - fr[0]*fr[6]*pow(to[6], 2.0) + fr[0]*fr[6]*pow(to[7], 2.0) - 2*fr[0]*fr[7]*to[6]*to[7] - to[6]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + 2*fr[0]*fr[3]*to[3] + 2*fr[0]*fr[4]*to[4] + 2*fr[0]*fr[5]*to[5] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0))))) - 2*v[7]*(cos_th*sin_th*(-fr[0]*to[7] + fr[7]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[7]*pow(to[0], 2.0) + fr[0]*fr[7]*pow(to[1], 2.0) + fr[0]*fr[7]*pow(to[2], 2.0) + fr[0]*fr[7]*pow(to[3], 2.0) + fr[0]*fr[7]*pow(to[4], 2.0) + fr[0]*fr[7]*pow(to[5], 2.0) + fr[0]*fr[7]*pow(to[6], 2.0) - fr[0]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[1]*to[1] + 2*fr[0]*fr[2]*to[2] + 2*fr[0]*fr[3]*to[3] + 2*fr[0]*fr[4]*to[4] + 2*fr[0]*fr[5]*to[5] + 2*fr[0]*fr[6]*to[6] + to[0]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) - pow(fr[2], 2.0) - pow(fr[3], 2.0) - pow(fr[4], 2.0) - pow(fr[5], 2.0) - pow(fr[6], 2.0) - pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[1] + fr[1]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[1]*pow(to[0], 2.0) - fr[0]*fr[1]*pow(to[1], 2.0) - fr[0]*fr[1]*pow(to[2], 2.0) - fr[0]*fr[1]*pow(to[3], 2.0) - fr[0]*fr[1]*pow(to[4], 2.0) - fr[0]*fr[1]*pow(to[5], 2.0) - fr[0]*fr[1]*pow(to[6], 2.0) - fr[0]*fr[1]*pow(to[7], 2.0) + 2*fr[1]*fr[2]*to[0]*to[2] + 2*fr[1]*fr[3]*to[0]*to[3] + 2*fr[1]*fr[4]*to[0]*to[4] + 2*fr[1]*fr[5]*to[0]*to[5] + 2*fr[1]*fr[6]*to[0]*to[6] + 2*fr[1]*fr[7]*to[0]*to[7] - to[0]*to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + v[1]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[0]*fr[1]*to[0]*to[1] + 4*fr[1]*fr[2]*to[1]*to[2] + 4*fr[1]*fr[3]*to[1]*to[3] + 4*fr[1]*fr[4]*to[1]*to[4] + 4*fr[1]*fr[5]*to[1]*to[5] + 4*fr[1]*fr[6]*to[1]*to[6] + 4*fr[1]*fr[7]*to[1]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - pow(to[1], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) - 2*v[2]*(cos_th*sin_th*(-fr[1]*to[2] + fr[2]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[2]*pow(to[0], 2.0) + fr[1]*fr[2]*pow(to[1], 2.0) - fr[1]*fr[2]*pow(to[2], 2.0) + fr[1]*fr[2]*pow(to[3], 2.0) + fr[1]*fr[2]*pow(to[4], 2.0) + fr[1]*fr[2]*pow(to[5], 2.0) + fr[1]*fr[2]*pow(to[6], 2.0) + fr[1]*fr[2]*pow(to[7], 2.0) - 2*fr[1]*fr[3]*to[2]*to[3] - 2*fr[1]*fr[4]*to[2]*to[4] - 2*fr[1]*fr[5]*to[2]*to[5] - 2*fr[1]*fr[6]*to[2]*to[6] - 2*fr[1]*fr[7]*to[2]*to[7] - to[2]*(2*fr[0]*fr[1]*to[0] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[3]*(cos_th*sin_th*(-fr[1]*to[3] + fr[3]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[3]*pow(to[0], 2.0) + fr[1]*fr[3]*pow(to[1], 2.0) + fr[1]*fr[3]*pow(to[2], 2.0) - fr[1]*fr[3]*pow(to[3], 2.0) + fr[1]*fr[3]*pow(to[4], 2.0) + fr[1]*fr[3]*pow(to[5], 2.0) + fr[1]*fr[3]*pow(to[6], 2.0) + fr[1]*fr[3]*pow(to[7], 2.0) - 2*fr[1]*fr[4]*to[3]*to[4] - 2*fr[1]*fr[5]*to[3]*to[5] - 2*fr[1]*fr[6]*to[3]*to[6] - 2*fr[1]*fr[7]*to[3]*to[7] - to[3]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[4]*(cos_th*sin_th*(-fr[1]*to[4] + fr[4]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[4]*pow(to[0], 2.0) + fr[1]*fr[4]*pow(to[1], 2.0) + fr[1]*fr[4]*pow(to[2], 2.0) + fr[1]*fr[4]*pow(to[3], 2.0) - fr[1]*fr[4]*pow(to[4], 2.0) + fr[1]*fr[4]*pow(to[5], 2.0) + fr[1]*fr[4]*pow(to[6], 2.0) + fr[1]*fr[4]*pow(to[7], 2.0) - 2*fr[1]*fr[5]*to[4]*to[5] - 2*fr[1]*fr[6]*to[4]*to[6] - 2*fr[1]*fr[7]*to[4]*to[7] - to[4]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] + 2*fr[1]*fr[3]*to[3] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[1]*to[5] + fr[5]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[5]*pow(to[0], 2.0) + fr[1]*fr[5]*pow(to[1], 2.0) + fr[1]*fr[5]*pow(to[2], 2.0) + fr[1]*fr[5]*pow(to[3], 2.0) + fr[1]*fr[5]*pow(to[4], 2.0) - fr[1]*fr[5]*pow(to[5], 2.0) + fr[1]*fr[5]*pow(to[6], 2.0) + fr[1]*fr[5]*pow(to[7], 2.0) - 2*fr[1]*fr[6]*to[5]*to[6] - 2*fr[1]*fr[7]*to[5]*to[7] - to[5]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] + 2*fr[1]*fr[3]*to[3] + 2*fr[1]*fr[4]*to[4] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[6]*(cos_th*sin_th*(-fr[1]*to[6] + fr[6]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[6]*pow(to[0], 2.0) + fr[1]*fr[6]*pow(to[1], 2.0) + fr[1]*fr[6]*pow(to[2], 2.0) + fr[1]*fr[6]*pow(to[3], 2.0) + fr[1]*fr[6]*pow(to[4], 2.0) + fr[1]*fr[6]*pow(to[5], 2.0) - fr[1]*fr[6]*pow(to[6], 2.0) + fr[1]*fr[6]*pow(to[7], 2.0) - 2*fr[1]*fr[7]*to[6]*to[7] - to[6]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] + 2*fr[1]*fr[3]*to[3] + 2*fr[1]*fr[4]*to[4] + 2*fr[1]*fr[5]*to[5] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[7]*(cos_th*sin_th*(-fr[1]*to[7] + fr[7]*to[1]) + pow(sin_th, 2.0)*(fr[1]*fr[7]*pow(to[0], 2.0) + fr[1]*fr[7]*pow(to[1], 2.0) + fr[1]*fr[7]*pow(to[2], 2.0) + fr[1]*fr[7]*pow(to[3], 2.0) + fr[1]*fr[7]*pow(to[4], 2.0) + fr[1]*fr[7]*pow(to[5], 2.0) + fr[1]*fr[7]*pow(to[6], 2.0) - fr[1]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[1]*to[0] + 2*fr[1]*fr[2]*to[2] + 2*fr[1]*fr[3]*to[3] + 2*fr[1]*fr[4]*to[4] + 2*fr[1]*fr[5]*to[5] + 2*fr[1]*fr[6]*to[6] - to[1]*(pow(fr[0], 2.0) - pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[2] + fr[2]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[2]*pow(to[0], 2.0) - fr[0]*fr[2]*pow(to[1], 2.0) - fr[0]*fr[2]*pow(to[2], 2.0) - fr[0]*fr[2]*pow(to[3], 2.0) - fr[0]*fr[2]*pow(to[4], 2.0) - fr[0]*fr[2]*pow(to[5], 2.0) - fr[0]*fr[2]*pow(to[6], 2.0) - fr[0]*fr[2]*pow(to[7], 2.0) + 2*fr[1]*fr[2]*to[0]*to[1] + 2*fr[2]*fr[3]*to[0]*to[3] + 2*fr[2]*fr[4]*to[0]*to[4] + 2*fr[2]*fr[5]*to[0]*to[5] + 2*fr[2]*fr[6]*to[0]*to[6] + 2*fr[2]*fr[7]*to[0]*to[7] - to[0]*to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[2] + fr[2]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[2]*to[0]*to[1] + fr[1]*fr[2]*pow(to[0], 2.0) - fr[1]*fr[2]*pow(to[1], 2.0) + fr[1]*fr[2]*pow(to[2], 2.0) + fr[1]*fr[2]*pow(to[3], 2.0) + fr[1]*fr[2]*pow(to[4], 2.0) + fr[1]*fr[2]*pow(to[5], 2.0) + fr[1]*fr[2]*pow(to[6], 2.0) + fr[1]*fr[2]*pow(to[7], 2.0) - 2*fr[2]*fr[3]*to[1]*to[3] - 2*fr[2]*fr[4]*to[1]*to[4] - 2*fr[2]*fr[5]*to[1]*to[5] - 2*fr[2]*fr[6]*to[1]*to[6] - 2*fr[2]*fr[7]*to[1]*to[7] + to[1]*to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + v[2]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[2]*fr[3]*to[2]*to[3] + 4*fr[2]*fr[4]*to[2]*to[4] + 4*fr[2]*fr[5]*to[2]*to[5] + 4*fr[2]*fr[6]*to[2]*to[6] + 4*fr[2]*fr[7]*to[2]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + 4*to[2]*(fr[0]*fr[2]*to[0] + fr[1]*fr[2]*to[1]) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) - 2*v[3]*(cos_th*sin_th*(-fr[2]*to[3] + fr[3]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[3]*pow(to[0], 2.0) + fr[2]*fr[3]*pow(to[1], 2.0) + fr[2]*fr[3]*pow(to[2], 2.0) - fr[2]*fr[3]*pow(to[3], 2.0) + fr[2]*fr[3]*pow(to[4], 2.0) + fr[2]*fr[3]*pow(to[5], 2.0) + fr[2]*fr[3]*pow(to[6], 2.0) + fr[2]*fr[3]*pow(to[7], 2.0) - 2*fr[2]*fr[4]*to[3]*to[4] - 2*fr[2]*fr[5]*to[3]*to[5] - 2*fr[2]*fr[6]*to[3]*to[6] - 2*fr[2]*fr[7]*to[3]*to[7] - to[3]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[4]*(cos_th*sin_th*(-fr[2]*to[4] + fr[4]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[4]*pow(to[0], 2.0) + fr[2]*fr[4]*pow(to[1], 2.0) + fr[2]*fr[4]*pow(to[2], 2.0) + fr[2]*fr[4]*pow(to[3], 2.0) - fr[2]*fr[4]*pow(to[4], 2.0) + fr[2]*fr[4]*pow(to[5], 2.0) + fr[2]*fr[4]*pow(to[6], 2.0) + fr[2]*fr[4]*pow(to[7], 2.0) - 2*fr[2]*fr[5]*to[4]*to[5] - 2*fr[2]*fr[6]*to[4]*to[6] - 2*fr[2]*fr[7]*to[4]*to[7] - to[4]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] + 2*fr[2]*fr[3]*to[3] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[2]*to[5] + fr[5]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[5]*pow(to[0], 2.0) + fr[2]*fr[5]*pow(to[1], 2.0) + fr[2]*fr[5]*pow(to[2], 2.0) + fr[2]*fr[5]*pow(to[3], 2.0) + fr[2]*fr[5]*pow(to[4], 2.0) - fr[2]*fr[5]*pow(to[5], 2.0) + fr[2]*fr[5]*pow(to[6], 2.0) + fr[2]*fr[5]*pow(to[7], 2.0) - 2*fr[2]*fr[6]*to[5]*to[6] - 2*fr[2]*fr[7]*to[5]*to[7] - to[5]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] + 2*fr[2]*fr[3]*to[3] + 2*fr[2]*fr[4]*to[4] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[6]*(cos_th*sin_th*(-fr[2]*to[6] + fr[6]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[6]*pow(to[0], 2.0) + fr[2]*fr[6]*pow(to[1], 2.0) + fr[2]*fr[6]*pow(to[2], 2.0) + fr[2]*fr[6]*pow(to[3], 2.0) + fr[2]*fr[6]*pow(to[4], 2.0) + fr[2]*fr[6]*pow(to[5], 2.0) - fr[2]*fr[6]*pow(to[6], 2.0) + fr[2]*fr[6]*pow(to[7], 2.0) - 2*fr[2]*fr[7]*to[6]*to[7] - to[6]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] + 2*fr[2]*fr[3]*to[3] + 2*fr[2]*fr[4]*to[4] + 2*fr[2]*fr[5]*to[5] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[7]*(cos_th*sin_th*(-fr[2]*to[7] + fr[7]*to[2]) + pow(sin_th, 2.0)*(fr[2]*fr[7]*pow(to[0], 2.0) + fr[2]*fr[7]*pow(to[1], 2.0) + fr[2]*fr[7]*pow(to[2], 2.0) + fr[2]*fr[7]*pow(to[3], 2.0) + fr[2]*fr[7]*pow(to[4], 2.0) + fr[2]*fr[7]*pow(to[5], 2.0) + fr[2]*fr[7]*pow(to[6], 2.0) - fr[2]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[2]*to[0] + 2*fr[1]*fr[2]*to[1] + 2*fr[2]*fr[3]*to[3] + 2*fr[2]*fr[4]*to[4] + 2*fr[2]*fr[5]*to[5] + 2*fr[2]*fr[6]*to[6] - to[2]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) - pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[3] + fr[3]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[3]*pow(to[0], 2.0) - fr[0]*fr[3]*pow(to[1], 2.0) - fr[0]*fr[3]*pow(to[2], 2.0) - fr[0]*fr[3]*pow(to[3], 2.0) - fr[0]*fr[3]*pow(to[4], 2.0) - fr[0]*fr[3]*pow(to[5], 2.0) - fr[0]*fr[3]*pow(to[6], 2.0) - fr[0]*fr[3]*pow(to[7], 2.0) + 2*fr[1]*fr[3]*to[0]*to[1] + 2*fr[2]*fr[3]*to[0]*to[2] + 2*fr[3]*fr[4]*to[0]*to[4] + 2*fr[3]*fr[5]*to[0]*to[5] + 2*fr[3]*fr[6]*to[0]*to[6] + 2*fr[3]*fr[7]*to[0]*to[7] - to[0]*to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[3] + fr[3]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[3]*to[0]*to[1] + fr[1]*fr[3]*pow(to[0], 2.0) - fr[1]*fr[3]*pow(to[1], 2.0) + fr[1]*fr[3]*pow(to[2], 2.0) + fr[1]*fr[3]*pow(to[3], 2.0) + fr[1]*fr[3]*pow(to[4], 2.0) + fr[1]*fr[3]*pow(to[5], 2.0) + fr[1]*fr[3]*pow(to[6], 2.0) + fr[1]*fr[3]*pow(to[7], 2.0) - 2*fr[2]*fr[3]*to[1]*to[2] - 2*fr[3]*fr[4]*to[1]*to[4] - 2*fr[3]*fr[5]*to[1]*to[5] - 2*fr[3]*fr[6]*to[1]*to[6] - 2*fr[3]*fr[7]*to[1]*to[7] + to[1]*to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[3] + fr[3]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[3]*pow(to[0], 2.0) + fr[2]*fr[3]*pow(to[1], 2.0) - fr[2]*fr[3]*pow(to[2], 2.0) + fr[2]*fr[3]*pow(to[3], 2.0) + fr[2]*fr[3]*pow(to[4], 2.0) + fr[2]*fr[3]*pow(to[5], 2.0) + fr[2]*fr[3]*pow(to[6], 2.0) + fr[2]*fr[3]*pow(to[7], 2.0) - 2*fr[3]*fr[4]*to[2]*to[4] - 2*fr[3]*fr[5]*to[2]*to[5] - 2*fr[3]*fr[6]*to[2]*to[6] - 2*fr[3]*fr[7]*to[2]*to[7] + to[2]*to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[2]*(fr[0]*fr[3]*to[0] + fr[1]*fr[3]*to[1]))) + v[3]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[3]*fr[4]*to[3]*to[4] + 4*fr[3]*fr[5]*to[3]*to[5] + 4*fr[3]*fr[6]*to[3]*to[6] + 4*fr[3]*fr[7]*to[3]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + 4*to[3]*(fr[0]*fr[3]*to[0] + fr[1]*fr[3]*to[1] + fr[2]*fr[3]*to[2]) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) - 2*v[4]*(cos_th*sin_th*(-fr[3]*to[4] + fr[4]*to[3]) + pow(sin_th, 2.0)*(fr[3]*fr[4]*pow(to[0], 2.0) + fr[3]*fr[4]*pow(to[1], 2.0) + fr[3]*fr[4]*pow(to[2], 2.0) + fr[3]*fr[4]*pow(to[3], 2.0) - fr[3]*fr[4]*pow(to[4], 2.0) + fr[3]*fr[4]*pow(to[5], 2.0) + fr[3]*fr[4]*pow(to[6], 2.0) + fr[3]*fr[4]*pow(to[7], 2.0) - 2*fr[3]*fr[5]*to[4]*to[5] - 2*fr[3]*fr[6]*to[4]*to[6] - 2*fr[3]*fr[7]*to[4]*to[7] - to[4]*(2*fr[0]*fr[3]*to[0] + 2*fr[1]*fr[3]*to[1] + 2*fr[2]*fr[3]*to[2] - to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[5]*(cos_th*sin_th*(-fr[3]*to[5] + fr[5]*to[3]) + pow(sin_th, 2.0)*(fr[3]*fr[5]*pow(to[0], 2.0) + fr[3]*fr[5]*pow(to[1], 2.0) + fr[3]*fr[5]*pow(to[2], 2.0) + fr[3]*fr[5]*pow(to[3], 2.0) + fr[3]*fr[5]*pow(to[4], 2.0) - fr[3]*fr[5]*pow(to[5], 2.0) + fr[3]*fr[5]*pow(to[6], 2.0) + fr[3]*fr[5]*pow(to[7], 2.0) - 2*fr[3]*fr[6]*to[5]*to[6] - 2*fr[3]*fr[7]*to[5]*to[7] - to[5]*(2*fr[0]*fr[3]*to[0] + 2*fr[1]*fr[3]*to[1] + 2*fr[2]*fr[3]*to[2] + 2*fr[3]*fr[4]*to[4] - to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[6]*(cos_th*sin_th*(-fr[3]*to[6] + fr[6]*to[3]) + pow(sin_th, 2.0)*(fr[3]*fr[6]*pow(to[0], 2.0) + fr[3]*fr[6]*pow(to[1], 2.0) + fr[3]*fr[6]*pow(to[2], 2.0) + fr[3]*fr[6]*pow(to[3], 2.0) + fr[3]*fr[6]*pow(to[4], 2.0) + fr[3]*fr[6]*pow(to[5], 2.0) - fr[3]*fr[6]*pow(to[6], 2.0) + fr[3]*fr[6]*pow(to[7], 2.0) - 2*fr[3]*fr[7]*to[6]*to[7] - to[6]*(2*fr[0]*fr[3]*to[0] + 2*fr[1]*fr[3]*to[1] + 2*fr[2]*fr[3]*to[2] + 2*fr[3]*fr[4]*to[4] + 2*fr[3]*fr[5]*to[5] - to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[7]*(cos_th*sin_th*(-fr[3]*to[7] + fr[7]*to[3]) + pow(sin_th, 2.0)*(fr[3]*fr[7]*pow(to[0], 2.0) + fr[3]*fr[7]*pow(to[1], 2.0) + fr[3]*fr[7]*pow(to[2], 2.0) + fr[3]*fr[7]*pow(to[3], 2.0) + fr[3]*fr[7]*pow(to[4], 2.0) + fr[3]*fr[7]*pow(to[5], 2.0) + fr[3]*fr[7]*pow(to[6], 2.0) - fr[3]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[3]*to[0] + 2*fr[1]*fr[3]*to[1] + 2*fr[2]*fr[3]*to[2] + 2*fr[3]*fr[4]*to[4] + 2*fr[3]*fr[5]*to[5] + 2*fr[3]*fr[6]*to[6] - to[3]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) - pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[4] + fr[4]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[4]*pow(to[0], 2.0) - fr[0]*fr[4]*pow(to[1], 2.0) - fr[0]*fr[4]*pow(to[2], 2.0) - fr[0]*fr[4]*pow(to[3], 2.0) - fr[0]*fr[4]*pow(to[4], 2.0) - fr[0]*fr[4]*pow(to[5], 2.0) - fr[0]*fr[4]*pow(to[6], 2.0) - fr[0]*fr[4]*pow(to[7], 2.0) + 2*fr[1]*fr[4]*to[0]*to[1] + 2*fr[2]*fr[4]*to[0]*to[2] + 2*fr[3]*fr[4]*to[0]*to[3] + 2*fr[4]*fr[5]*to[0]*to[5] + 2*fr[4]*fr[6]*to[0]*to[6] + 2*fr[4]*fr[7]*to[0]*to[7] - to[0]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[4] + fr[4]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[4]*to[0]*to[1] + fr[1]*fr[4]*pow(to[0], 2.0) - fr[1]*fr[4]*pow(to[1], 2.0) + fr[1]*fr[4]*pow(to[2], 2.0) + fr[1]*fr[4]*pow(to[3], 2.0) + fr[1]*fr[4]*pow(to[4], 2.0) + fr[1]*fr[4]*pow(to[5], 2.0) + fr[1]*fr[4]*pow(to[6], 2.0) + fr[1]*fr[4]*pow(to[7], 2.0) - 2*fr[2]*fr[4]*to[1]*to[2] - 2*fr[3]*fr[4]*to[1]*to[3] - 2*fr[4]*fr[5]*to[1]*to[5] - 2*fr[4]*fr[6]*to[1]*to[6] - 2*fr[4]*fr[7]*to[1]*to[7] + to[1]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[4] + fr[4]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[4]*pow(to[0], 2.0) + fr[2]*fr[4]*pow(to[1], 2.0) - fr[2]*fr[4]*pow(to[2], 2.0) + fr[2]*fr[4]*pow(to[3], 2.0) + fr[2]*fr[4]*pow(to[4], 2.0) + fr[2]*fr[4]*pow(to[5], 2.0) + fr[2]*fr[4]*pow(to[6], 2.0) + fr[2]*fr[4]*pow(to[7], 2.0) - 2*fr[3]*fr[4]*to[2]*to[3] - 2*fr[4]*fr[5]*to[2]*to[5] - 2*fr[4]*fr[6]*to[2]*to[6] - 2*fr[4]*fr[7]*to[2]*to[7] + to[2]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[2]*(fr[0]*fr[4]*to[0] + fr[1]*fr[4]*to[1]))) + 2*v[3]*(cos_th*sin_th*(-fr[3]*to[4] + fr[4]*to[3]) - pow(sin_th, 2.0)*(fr[3]*fr[4]*pow(to[0], 2.0) + fr[3]*fr[4]*pow(to[1], 2.0) + fr[3]*fr[4]*pow(to[2], 2.0) - fr[3]*fr[4]*pow(to[3], 2.0) + fr[3]*fr[4]*pow(to[4], 2.0) + fr[3]*fr[4]*pow(to[5], 2.0) + fr[3]*fr[4]*pow(to[6], 2.0) + fr[3]*fr[4]*pow(to[7], 2.0) - 2*fr[4]*fr[5]*to[3]*to[5] - 2*fr[4]*fr[6]*to[3]*to[6] - 2*fr[4]*fr[7]*to[3]*to[7] + to[3]*to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[3]*(fr[0]*fr[4]*to[0] + fr[1]*fr[4]*to[1] + fr[2]*fr[4]*to[2]))) + v[4]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[4]*fr[5]*to[4]*to[5] + 4*fr[4]*fr[6]*to[4]*to[6] + 4*fr[4]*fr[7]*to[4]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + 4*to[4]*(fr[0]*fr[4]*to[0] + fr[1]*fr[4]*to[1] + fr[2]*fr[4]*to[2] + fr[3]*fr[4]*to[3]) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) - 2*v[5]*(cos_th*sin_th*(-fr[4]*to[5] + fr[5]*to[4]) + pow(sin_th, 2.0)*(fr[4]*fr[5]*pow(to[0], 2.0) + fr[4]*fr[5]*pow(to[1], 2.0) + fr[4]*fr[5]*pow(to[2], 2.0) + fr[4]*fr[5]*pow(to[3], 2.0) + fr[4]*fr[5]*pow(to[4], 2.0) - fr[4]*fr[5]*pow(to[5], 2.0) + fr[4]*fr[5]*pow(to[6], 2.0) + fr[4]*fr[5]*pow(to[7], 2.0) - 2*fr[4]*fr[6]*to[5]*to[6] - 2*fr[4]*fr[7]*to[5]*to[7] - to[5]*(2*fr[0]*fr[4]*to[0] + 2*fr[1]*fr[4]*to[1] + 2*fr[2]*fr[4]*to[2] + 2*fr[3]*fr[4]*to[3] - to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[6]*(cos_th*sin_th*(-fr[4]*to[6] + fr[6]*to[4]) + pow(sin_th, 2.0)*(fr[4]*fr[6]*pow(to[0], 2.0) + fr[4]*fr[6]*pow(to[1], 2.0) + fr[4]*fr[6]*pow(to[2], 2.0) + fr[4]*fr[6]*pow(to[3], 2.0) + fr[4]*fr[6]*pow(to[4], 2.0) + fr[4]*fr[6]*pow(to[5], 2.0) - fr[4]*fr[6]*pow(to[6], 2.0) + fr[4]*fr[6]*pow(to[7], 2.0) - 2*fr[4]*fr[7]*to[6]*to[7] - to[6]*(2*fr[0]*fr[4]*to[0] + 2*fr[1]*fr[4]*to[1] + 2*fr[2]*fr[4]*to[2] + 2*fr[3]*fr[4]*to[3] + 2*fr[4]*fr[5]*to[5] - to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[7]*(cos_th*sin_th*(-fr[4]*to[7] + fr[7]*to[4]) + pow(sin_th, 2.0)*(fr[4]*fr[7]*pow(to[0], 2.0) + fr[4]*fr[7]*pow(to[1], 2.0) + fr[4]*fr[7]*pow(to[2], 2.0) + fr[4]*fr[7]*pow(to[3], 2.0) + fr[4]*fr[7]*pow(to[4], 2.0) + fr[4]*fr[7]*pow(to[5], 2.0) + fr[4]*fr[7]*pow(to[6], 2.0) - fr[4]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[4]*to[0] + 2*fr[1]*fr[4]*to[1] + 2*fr[2]*fr[4]*to[2] + 2*fr[3]*fr[4]*to[3] + 2*fr[4]*fr[5]*to[5] + 2*fr[4]*fr[6]*to[6] - to[4]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) - pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[5] + fr[5]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[5]*pow(to[0], 2.0) - fr[0]*fr[5]*pow(to[1], 2.0) - fr[0]*fr[5]*pow(to[2], 2.0) - fr[0]*fr[5]*pow(to[3], 2.0) - fr[0]*fr[5]*pow(to[4], 2.0) - fr[0]*fr[5]*pow(to[5], 2.0) - fr[0]*fr[5]*pow(to[6], 2.0) - fr[0]*fr[5]*pow(to[7], 2.0) + 2*fr[1]*fr[5]*to[0]*to[1] + 2*fr[2]*fr[5]*to[0]*to[2] + 2*fr[3]*fr[5]*to[0]*to[3] + 2*fr[4]*fr[5]*to[0]*to[4] + 2*fr[5]*fr[6]*to[0]*to[6] + 2*fr[5]*fr[7]*to[0]*to[7] - to[0]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[5] + fr[5]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[5]*to[0]*to[1] + fr[1]*fr[5]*pow(to[0], 2.0) - fr[1]*fr[5]*pow(to[1], 2.0) + fr[1]*fr[5]*pow(to[2], 2.0) + fr[1]*fr[5]*pow(to[3], 2.0) + fr[1]*fr[5]*pow(to[4], 2.0) + fr[1]*fr[5]*pow(to[5], 2.0) + fr[1]*fr[5]*pow(to[6], 2.0) + fr[1]*fr[5]*pow(to[7], 2.0) - 2*fr[2]*fr[5]*to[1]*to[2] - 2*fr[3]*fr[5]*to[1]*to[3] - 2*fr[4]*fr[5]*to[1]*to[4] - 2*fr[5]*fr[6]*to[1]*to[6] - 2*fr[5]*fr[7]*to[1]*to[7] + to[1]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[5] + fr[5]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[5]*pow(to[0], 2.0) + fr[2]*fr[5]*pow(to[1], 2.0) - fr[2]*fr[5]*pow(to[2], 2.0) + fr[2]*fr[5]*pow(to[3], 2.0) + fr[2]*fr[5]*pow(to[4], 2.0) + fr[2]*fr[5]*pow(to[5], 2.0) + fr[2]*fr[5]*pow(to[6], 2.0) + fr[2]*fr[5]*pow(to[7], 2.0) - 2*fr[3]*fr[5]*to[2]*to[3] - 2*fr[4]*fr[5]*to[2]*to[4] - 2*fr[5]*fr[6]*to[2]*to[6] - 2*fr[5]*fr[7]*to[2]*to[7] + to[2]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[2]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1]))) + 2*v[3]*(cos_th*sin_th*(-fr[3]*to[5] + fr[5]*to[3]) - pow(sin_th, 2.0)*(fr[3]*fr[5]*pow(to[0], 2.0) + fr[3]*fr[5]*pow(to[1], 2.0) + fr[3]*fr[5]*pow(to[2], 2.0) - fr[3]*fr[5]*pow(to[3], 2.0) + fr[3]*fr[5]*pow(to[4], 2.0) + fr[3]*fr[5]*pow(to[5], 2.0) + fr[3]*fr[5]*pow(to[6], 2.0) + fr[3]*fr[5]*pow(to[7], 2.0) - 2*fr[4]*fr[5]*to[3]*to[4] - 2*fr[5]*fr[6]*to[3]*to[6] - 2*fr[5]*fr[7]*to[3]*to[7] + to[3]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[3]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1] + fr[2]*fr[5]*to[2]))) + 2*v[4]*(cos_th*sin_th*(-fr[4]*to[5] + fr[5]*to[4]) - pow(sin_th, 2.0)*(fr[4]*fr[5]*pow(to[0], 2.0) + fr[4]*fr[5]*pow(to[1], 2.0) + fr[4]*fr[5]*pow(to[2], 2.0) + fr[4]*fr[5]*pow(to[3], 2.0) - fr[4]*fr[5]*pow(to[4], 2.0) + fr[4]*fr[5]*pow(to[5], 2.0) + fr[4]*fr[5]*pow(to[6], 2.0) + fr[4]*fr[5]*pow(to[7], 2.0) - 2*fr[5]*fr[6]*to[4]*to[6] - 2*fr[5]*fr[7]*to[4]*to[7] + to[4]*to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[4]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1] + fr[2]*fr[5]*to[2] + fr[3]*fr[5]*to[3]))) + v[5]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[5]*fr[6]*to[5]*to[6] + 4*fr[5]*fr[7]*to[5]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) - pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + 4*to[5]*(fr[0]*fr[5]*to[0] + fr[1]*fr[5]*to[1] + fr[2]*fr[5]*to[2] + fr[3]*fr[5]*to[3] + fr[4]*fr[5]*to[4]) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))) - 2*v[6]*(cos_th*sin_th*(-fr[5]*to[6] + fr[6]*to[5]) + pow(sin_th, 2.0)*(fr[5]*fr[6]*pow(to[0], 2.0) + fr[5]*fr[6]*pow(to[1], 2.0) + fr[5]*fr[6]*pow(to[2], 2.0) + fr[5]*fr[6]*pow(to[3], 2.0) + fr[5]*fr[6]*pow(to[4], 2.0) + fr[5]*fr[6]*pow(to[5], 2.0) - fr[5]*fr[6]*pow(to[6], 2.0) + fr[5]*fr[6]*pow(to[7], 2.0) - 2*fr[5]*fr[7]*to[6]*to[7] - to[6]*(2*fr[0]*fr[5]*to[0] + 2*fr[1]*fr[5]*to[1] + 2*fr[2]*fr[5]*to[2] + 2*fr[3]*fr[5]*to[3] + 2*fr[4]*fr[5]*to[4] - to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))) - 2*v[7]*(cos_th*sin_th*(-fr[5]*to[7] + fr[7]*to[5]) + pow(sin_th, 2.0)*(fr[5]*fr[7]*pow(to[0], 2.0) + fr[5]*fr[7]*pow(to[1], 2.0) + fr[5]*fr[7]*pow(to[2], 2.0) + fr[5]*fr[7]*pow(to[3], 2.0) + fr[5]*fr[7]*pow(to[4], 2.0) + fr[5]*fr[7]*pow(to[5], 2.0) + fr[5]*fr[7]*pow(to[6], 2.0) - fr[5]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[5]*to[0] + 2*fr[1]*fr[5]*to[1] + 2*fr[2]*fr[5]*to[2] + 2*fr[3]*fr[5]*to[3] + 2*fr[4]*fr[5]*to[4] + 2*fr[5]*fr[6]*to[6] - to[5]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) - pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[6] + fr[6]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[6]*pow(to[0], 2.0) - fr[0]*fr[6]*pow(to[1], 2.0) - fr[0]*fr[6]*pow(to[2], 2.0) - fr[0]*fr[6]*pow(to[3], 2.0) - fr[0]*fr[6]*pow(to[4], 2.0) - fr[0]*fr[6]*pow(to[5], 2.0) - fr[0]*fr[6]*pow(to[6], 2.0) - fr[0]*fr[6]*pow(to[7], 2.0) + 2*fr[1]*fr[6]*to[0]*to[1] + 2*fr[2]*fr[6]*to[0]*to[2] + 2*fr[3]*fr[6]*to[0]*to[3] + 2*fr[4]*fr[6]*to[0]*to[4] + 2*fr[5]*fr[6]*to[0]*to[5] + 2*fr[6]*fr[7]*to[0]*to[7] - to[0]*to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[6] + fr[6]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[6]*to[0]*to[1] + fr[1]*fr[6]*pow(to[0], 2.0) - fr[1]*fr[6]*pow(to[1], 2.0) + fr[1]*fr[6]*pow(to[2], 2.0) + fr[1]*fr[6]*pow(to[3], 2.0) + fr[1]*fr[6]*pow(to[4], 2.0) + fr[1]*fr[6]*pow(to[5], 2.0) + fr[1]*fr[6]*pow(to[6], 2.0) + fr[1]*fr[6]*pow(to[7], 2.0) - 2*fr[2]*fr[6]*to[1]*to[2] - 2*fr[3]*fr[6]*to[1]*to[3] - 2*fr[4]*fr[6]*to[1]*to[4] - 2*fr[5]*fr[6]*to[1]*to[5] - 2*fr[6]*fr[7]*to[1]*to[7] + to[1]*to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[6] + fr[6]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[6]*pow(to[0], 2.0) + fr[2]*fr[6]*pow(to[1], 2.0) - fr[2]*fr[6]*pow(to[2], 2.0) + fr[2]*fr[6]*pow(to[3], 2.0) + fr[2]*fr[6]*pow(to[4], 2.0) + fr[2]*fr[6]*pow(to[5], 2.0) + fr[2]*fr[6]*pow(to[6], 2.0) + fr[2]*fr[6]*pow(to[7], 2.0) - 2*fr[3]*fr[6]*to[2]*to[3] - 2*fr[4]*fr[6]*to[2]*to[4] - 2*fr[5]*fr[6]*to[2]*to[5] - 2*fr[6]*fr[7]*to[2]*to[7] + to[2]*to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[2]*(fr[0]*fr[6]*to[0] + fr[1]*fr[6]*to[1]))) + 2*v[3]*(cos_th*sin_th*(-fr[3]*to[6] + fr[6]*to[3]) - pow(sin_th, 2.0)*(fr[3]*fr[6]*pow(to[0], 2.0) + fr[3]*fr[6]*pow(to[1], 2.0) + fr[3]*fr[6]*pow(to[2], 2.0) - fr[3]*fr[6]*pow(to[3], 2.0) + fr[3]*fr[6]*pow(to[4], 2.0) + fr[3]*fr[6]*pow(to[5], 2.0) + fr[3]*fr[6]*pow(to[6], 2.0) + fr[3]*fr[6]*pow(to[7], 2.0) - 2*fr[4]*fr[6]*to[3]*to[4] - 2*fr[5]*fr[6]*to[3]*to[5] - 2*fr[6]*fr[7]*to[3]*to[7] + to[3]*to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[3]*(fr[0]*fr[6]*to[0] + fr[1]*fr[6]*to[1] + fr[2]*fr[6]*to[2]))) + 2*v[4]*(cos_th*sin_th*(-fr[4]*to[6] + fr[6]*to[4]) - pow(sin_th, 2.0)*(fr[4]*fr[6]*pow(to[0], 2.0) + fr[4]*fr[6]*pow(to[1], 2.0) + fr[4]*fr[6]*pow(to[2], 2.0) + fr[4]*fr[6]*pow(to[3], 2.0) - fr[4]*fr[6]*pow(to[4], 2.0) + fr[4]*fr[6]*pow(to[5], 2.0) + fr[4]*fr[6]*pow(to[6], 2.0) + fr[4]*fr[6]*pow(to[7], 2.0) - 2*fr[5]*fr[6]*to[4]*to[5] - 2*fr[6]*fr[7]*to[4]*to[7] + to[4]*to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[4]*(fr[0]*fr[6]*to[0] + fr[1]*fr[6]*to[1] + fr[2]*fr[6]*to[2] + fr[3]*fr[6]*to[3]))) + 2*v[5]*(cos_th*sin_th*(-fr[5]*to[6] + fr[6]*to[5]) - pow(sin_th, 2.0)*(fr[5]*fr[6]*pow(to[0], 2.0) + fr[5]*fr[6]*pow(to[1], 2.0) + fr[5]*fr[6]*pow(to[2], 2.0) + fr[5]*fr[6]*pow(to[3], 2.0) + fr[5]*fr[6]*pow(to[4], 2.0) - fr[5]*fr[6]*pow(to[5], 2.0) + fr[5]*fr[6]*pow(to[6], 2.0) + fr[5]*fr[6]*pow(to[7], 2.0) - 2*fr[6]*fr[7]*to[5]*to[7] + to[5]*to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) - 2*to[5]*(fr[0]*fr[6]*to[0] + fr[1]*fr[6]*to[1] + fr[2]*fr[6]*to[2] + fr[3]*fr[6]*to[3] + fr[4]*fr[6]*to[4]))) + v[6]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(4*fr[6]*fr[7]*to[6]*to[7] + pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) - pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)) + 4*to[6]*(fr[0]*fr[6]*to[0] + fr[1]*fr[6]*to[1] + fr[2]*fr[6]*to[2] + fr[3]*fr[6]*to[3] + fr[4]*fr[6]*to[4] + fr[5]*fr[6]*to[5]) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0)))) - 2*v[7]*(cos_th*sin_th*(-fr[6]*to[7] + fr[7]*to[6]) + pow(sin_th, 2.0)*(fr[6]*fr[7]*pow(to[0], 2.0) + fr[6]*fr[7]*pow(to[1], 2.0) + fr[6]*fr[7]*pow(to[2], 2.0) + fr[6]*fr[7]*pow(to[3], 2.0) + fr[6]*fr[7]*pow(to[4], 2.0) + fr[6]*fr[7]*pow(to[5], 2.0) + fr[6]*fr[7]*pow(to[6], 2.0) - fr[6]*fr[7]*pow(to[7], 2.0) - to[7]*(2*fr[0]*fr[6]*to[0] + 2*fr[1]*fr[6]*to[1] + 2*fr[2]*fr[6]*to[2] + 2*fr[3]*fr[6]*to[3] + 2*fr[4]*fr[6]*to[4] + 2*fr[5]*fr[6]*to[5] - to[6]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) - pow(fr[6], 2.0) + pow(fr[7], 2.0))))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))), (2*v[0]*(cos_th*sin_th*(-fr[0]*to[7] + fr[7]*to[0]) + pow(sin_th, 2.0)*(fr[0]*fr[7]*pow(to[0], 2.0) - fr[0]*fr[7]*pow(to[1], 2.0) - fr[0]*fr[7]*pow(to[2], 2.0) - fr[0]*fr[7]*pow(to[3], 2.0) - fr[0]*fr[7]*pow(to[4], 2.0) - fr[0]*fr[7]*pow(to[5], 2.0) - fr[0]*fr[7]*pow(to[6], 2.0) - fr[0]*fr[7]*pow(to[7], 2.0) + 2*fr[1]*fr[7]*to[0]*to[1] + 2*fr[2]*fr[7]*to[0]*to[2] + 2*fr[3]*fr[7]*to[0]*to[3] + 2*fr[4]*fr[7]*to[0]*to[4] + 2*fr[5]*fr[7]*to[0]*to[5] + 2*fr[6]*fr[7]*to[0]*to[6] - to[0]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)))) + 2*v[1]*(cos_th*sin_th*(-fr[1]*to[7] + fr[7]*to[1]) - pow(sin_th, 2.0)*(-2*fr[0]*fr[7]*to[0]*to[1] + fr[1]*fr[7]*pow(to[0], 2.0) - fr[1]*fr[7]*pow(to[1], 2.0) + fr[1]*fr[7]*pow(to[2], 2.0) + fr[1]*fr[7]*pow(to[3], 2.0) + fr[1]*fr[7]*pow(to[4], 2.0) + fr[1]*fr[7]*pow(to[5], 2.0) + fr[1]*fr[7]*pow(to[6], 2.0) + fr[1]*fr[7]*pow(to[7], 2.0) - 2*fr[2]*fr[7]*to[1]*to[2] - 2*fr[3]*fr[7]*to[1]*to[3] - 2*fr[4]*fr[7]*to[1]*to[4] - 2*fr[5]*fr[7]*to[1]*to[5] - 2*fr[6]*fr[7]*to[1]*to[6] + to[1]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)))) + 2*v[2]*(cos_th*sin_th*(-fr[2]*to[7] + fr[7]*to[2]) - pow(sin_th, 2.0)*(fr[2]*fr[7]*pow(to[0], 2.0) + fr[2]*fr[7]*pow(to[1], 2.0) - fr[2]*fr[7]*pow(to[2], 2.0) + fr[2]*fr[7]*pow(to[3], 2.0) + fr[2]*fr[7]*pow(to[4], 2.0) + fr[2]*fr[7]*pow(to[5], 2.0) + fr[2]*fr[7]*pow(to[6], 2.0) + fr[2]*fr[7]*pow(to[7], 2.0) - 2*fr[3]*fr[7]*to[2]*to[3] - 2*fr[4]*fr[7]*to[2]*to[4] - 2*fr[5]*fr[7]*to[2]*to[5] - 2*fr[6]*fr[7]*to[2]*to[6] + to[2]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) - 2*to[2]*(fr[0]*fr[7]*to[0] + fr[1]*fr[7]*to[1]))) + 2*v[3]*(cos_th*sin_th*(-fr[3]*to[7] + fr[7]*to[3]) - pow(sin_th, 2.0)*(fr[3]*fr[7]*pow(to[0], 2.0) + fr[3]*fr[7]*pow(to[1], 2.0) + fr[3]*fr[7]*pow(to[2], 2.0) - fr[3]*fr[7]*pow(to[3], 2.0) + fr[3]*fr[7]*pow(to[4], 2.0) + fr[3]*fr[7]*pow(to[5], 2.0) + fr[3]*fr[7]*pow(to[6], 2.0) + fr[3]*fr[7]*pow(to[7], 2.0) - 2*fr[4]*fr[7]*to[3]*to[4] - 2*fr[5]*fr[7]*to[3]*to[5] - 2*fr[6]*fr[7]*to[3]*to[6] + to[3]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) - 2*to[3]*(fr[0]*fr[7]*to[0] + fr[1]*fr[7]*to[1] + fr[2]*fr[7]*to[2]))) + 2*v[4]*(cos_th*sin_th*(-fr[4]*to[7] + fr[7]*to[4]) - pow(sin_th, 2.0)*(fr[4]*fr[7]*pow(to[0], 2.0) + fr[4]*fr[7]*pow(to[1], 2.0) + fr[4]*fr[7]*pow(to[2], 2.0) + fr[4]*fr[7]*pow(to[3], 2.0) - fr[4]*fr[7]*pow(to[4], 2.0) + fr[4]*fr[7]*pow(to[5], 2.0) + fr[4]*fr[7]*pow(to[6], 2.0) + fr[4]*fr[7]*pow(to[7], 2.0) - 2*fr[5]*fr[7]*to[4]*to[5] - 2*fr[6]*fr[7]*to[4]*to[6] + to[4]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) - 2*to[4]*(fr[0]*fr[7]*to[0] + fr[1]*fr[7]*to[1] + fr[2]*fr[7]*to[2] + fr[3]*fr[7]*to[3]))) + 2*v[5]*(cos_th*sin_th*(-fr[5]*to[7] + fr[7]*to[5]) - pow(sin_th, 2.0)*(fr[5]*fr[7]*pow(to[0], 2.0) + fr[5]*fr[7]*pow(to[1], 2.0) + fr[5]*fr[7]*pow(to[2], 2.0) + fr[5]*fr[7]*pow(to[3], 2.0) + fr[5]*fr[7]*pow(to[4], 2.0) - fr[5]*fr[7]*pow(to[5], 2.0) + fr[5]*fr[7]*pow(to[6], 2.0) + fr[5]*fr[7]*pow(to[7], 2.0) - 2*fr[6]*fr[7]*to[5]*to[6] + to[5]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) - 2*to[5]*(fr[0]*fr[7]*to[0] + fr[1]*fr[7]*to[1] + fr[2]*fr[7]*to[2] + fr[3]*fr[7]*to[3] + fr[4]*fr[7]*to[4]))) + 2*v[6]*(cos_th*sin_th*(-fr[6]*to[7] + fr[7]*to[6]) - pow(sin_th, 2.0)*(fr[6]*fr[7]*pow(to[0], 2.0) + fr[6]*fr[7]*pow(to[1], 2.0) + fr[6]*fr[7]*pow(to[2], 2.0) + fr[6]*fr[7]*pow(to[3], 2.0) + fr[6]*fr[7]*pow(to[4], 2.0) + fr[6]*fr[7]*pow(to[5], 2.0) - fr[6]*fr[7]*pow(to[6], 2.0) + fr[6]*fr[7]*pow(to[7], 2.0) + to[6]*to[7]*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) - 2*to[6]*(fr[0]*fr[7]*to[0] + fr[1]*fr[7]*to[1] + fr[2]*fr[7]*to[2] + fr[3]*fr[7]*to[3] + fr[4]*fr[7]*to[4] + fr[5]*fr[7]*to[5]))) + v[7]*(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) - pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) - pow(fr[7], 2.0)) + 4*to[7]*(fr[0]*fr[7]*to[0] + fr[1]*fr[7]*to[1] + fr[2]*fr[7]*to[2] + fr[3]*fr[7]*to[3] + fr[4]*fr[7]*to[4] + fr[5]*fr[7]*to[5] + fr[6]*fr[7]*to[6]))))/(pow(cos_th, 2.0) + 2*cos_th*sin_th*(fr[0]*to[0] + fr[1]*to[1] + fr[2]*to[2] + fr[3]*to[3] + fr[4]*to[4] + fr[5]*to[5] + fr[6]*to[6] + fr[7]*to[7]) + pow(sin_th, 2.0)*(pow(to[0], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[1], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[2], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[3], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[4], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[5], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[6], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)) + pow(to[7], 2.0)*(pow(fr[0], 2.0) + pow(fr[1], 2.0) + pow(fr[2], 2.0) + pow(fr[3], 2.0) + pow(fr[4], 2.0) + pow(fr[5], 2.0) + pow(fr[6], 2.0) + pow(fr[7], 2.0)))));
}


float[N] loadParamsJuliaVect(out float u[N]){
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; u[5] = JuliaVect6; u[6] = JuliaVect7; u[7] = JuliaVect8; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; u[5] = Position6; u[6] = Position7; u[7] = Position8; 
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
        mulPwr(flipA(z),pow1),
        mulPwr(flipB(z),pow2)
    );
    //z = mul3(
    //    mulPwr(flipA(z),pow1),
    //    mulPwr(flipB(z),pow2),
    //    mulPwr(flipC(z),pow3)
    //);
    
}
    
bool inside(vec3 pt) {
    float z[N] = frame(O,pt);
    float z0[N] = z;
	vec3 zPt;
  	float r;
  	int i=0;
  	r=abs(norm(z));
	orbitTrap = vec4(100000);
    while(r<Bailout && (i<Iterations)) {
      float zprev[N] = z;
  		iter(z);
      if (addInitial) { z = add(z,z0); }
      if (addJulia) { z = add(z,JuliaVect); }
      if (addPrevious) { z = add(z,zprev); }
  		
  		r=abs(norm(z));
		if (i<ColorIterations) {
		zPt = vec3(z[FrameX-1],z[FrameY-1],z[FrameZ-1]);
		orbitTrap = min(orbitTrap, abs(vec4(zPt.x,zPt.y,zPt.z,r*r)));
		}

  		i++;
  	}
	return ((r < Bailout && r > Bailin) || BailInvert);
}

    vec3 color(vec3 pt) {

	orbitTrap.w = sqrt(orbitTrap.w);

	vec3 orbitColor;
	orbitColor = X.xyz*X.w*orbitTrap.x +
	Y.xyz*Y.w*orbitTrap.y +
	Z.xyz*Z.w*orbitTrap.z +
	R.xyz*R.w*orbitTrap.w;

	vec3 color = mix(BaseColor, 3.0*orbitColor,  OrbitStrength);
	return color;
}
#preset Default
AutoFocus = true
NormalScale = 1
AOScale = 0.5882353
Glow = 1
AOStrength = 1
Samples = 20
Stratify = true
DebugInside = false
CentralDifferences = true
SampleNeighbors = true
Near = 0
Far = 12
DepthToAlpha = false
DebugNormals = false
Gamma = 1.0
SpecularExp = 16.364
SpotLight = 1,1,1,0.1
SpotLightDir = 0.63626,0.5
CamLight = 1,1,1,1.53846
CamLightMin = 0.12121
Specular = 1
BaseColor = 0.4,0.690196,1
OrbitStrength = 0.5504587
X = 0.0784314,1,0.937255,0.2148148
Y = 0.45098,0.823529,0.0862745,1
Z = 0.988235,0.913725,0.309804,0.9407407
R = 0.937255,0.156863,0.156863,0.7777778
BackgroundColor = 0.933333,0.933333,0.92549
GradientBackground = 0
CycleColors = true
Cycles = 10.13333
ColorIterations = 28
FOV = 0.4
Eye = -0.296716,-0.0422444,-4.62051
Target = -1.42768,-0.137922,5.31487
Up = 0.0013069,0.999951,0.0097783
EquiRectangular = false
#endpreset

#preset trueblue
BaseColor = 0.4,0.690196,1
OrbitStrength = 0.4311927
X = 0.0784314,1,0.937255,0.9259259
Y = 0.447059,0.623529,0.811765,0.119403
Z = 0.768628,0.627451,0,-0.1555556
R = 0.0784314,1,0.937255,-0.0962963
BackgroundColor = 0.933333,0.933333,0.92549
GradientBackground = 0
CycleColors = true
Cycles = 10.13333
ColorIterations = 28
#endpreset

#preset sheen
BaseColor = 0.4,0.690196,1
OrbitStrength = 0.5504587
X = 0.0784314,1,0.937255,0.2148148
Y = 0.45098,0.823529,0.0862745,1
Z = 0.988235,0.913725,0.309804,0.9407407
R = 0.937255,0.156863,0.156863,0.7777778
BackgroundColor = 0.933333,0.933333,0.92549
GradientBackground = 0
CycleColors = true
Cycles = 10.13333
ColorIterations = 28
#endpreset