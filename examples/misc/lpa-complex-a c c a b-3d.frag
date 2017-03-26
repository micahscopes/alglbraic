#version 130
#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 4

#info leavitt path algebra of with dimension 24, for graph(-a1_im*b10_im + a1_re*b10_re - a1_im*b1_im + a1_re*b1_re - a4_im*b7_im + a4_re*b7_re, a1_re*b10_im + a1_im*b10_re + a1_re*b1_im + a1_im*b1_re + a4_re*b7_im + a4_im*b7_re, -a2_im*b2_im + a2_re*b2_re, a2_re*b2_im + a2_im*b2_re, -a3_im*b11_im + a3_re*b11_re - a3_im*b12_im + a3_re*b12_re - a3_im*b3_im + a3_re*b3_re - a5_im*b8_im + a5_re*b8_re - a6_im*b9_im + a6_re*b9_re, a3_re*b11_im + a3_im*b11_re + a3_re*b12_im + a3_im*b12_re + a3_re*b3_im + a3_im*b3_re + a5_re*b8_im + a5_im*b8_re + a6_re*b9_im + a6_im*b9_re, -a4_im*b3_im + a4_re*b3_re - a1_im*b4_im + a1_re*b4_re, a4_re*b3_im + a4_im*b3_re + a1_re*b4_im + a1_im*b4_re, -a5_im*b1_im + a5_re*b1_re - a3_im*b5_im + a3_re*b5_re, a5_re*b1_im + a5_im*b1_re + a3_re*b5_im + a3_im*b5_re, -a6_im*b2_im + a6_re*b2_re - a3_im*b6_im + a3_re*b6_re, a6_re*b2_im + a6_im*b2_re + a3_re*b6_im + a3_im*b6_re, -a7_im*b1_im + a7_re*b1_re - a3_im*b7_im + a3_re*b7_re, a7_re*b1_im + a7_im*b1_re + a3_re*b7_im + a3_im*b7_re, -a8_im*b3_im + a8_re*b3_re - a1_im*b8_im + a1_re*b8_re, a8_re*b3_im + a8_im*b3_re + a1_re*b8_im + a1_im*b8_re, -a9_im*b3_im + a9_re*b3_re - a2_im*b9_im + a2_re*b9_re, a9_re*b3_im + a9_im*b3_re + a2_re*b9_im + a2_im*b9_re, a3_im*b12_im - a3_re*b12_re + a6_im*b9_im - a6_re*b9_re, -a3_re*b12_im - a3_im*b12_re - a6_re*b9_im - a6_im*b9_re, a3_im*b11_im - a3_re*b11_re + a5_im*b8_im - a5_re*b8_re, -a3_re*b11_im - a3_im*b11_re - a5_re*b8_im - a5_im*b8_re)
#include "Brute-Raytracer.frag"
#group Algebraic
    
// the default p-norm power (p).
uniform float NormPower; slider[0.000000001,2,100]
const int N = 24;
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
uniform float JuliaVect17; slider[-2,0,2]
uniform float JuliaVect18; slider[-2,0,2]
uniform float JuliaVect19; slider[-2,0,2]
uniform float JuliaVect20; slider[-2,0,2]
uniform float JuliaVect21; slider[-2,0,2]
uniform float JuliaVect22; slider[-2,0,2]
uniform float JuliaVect23; slider[-2,0,2]
uniform float JuliaVect24; slider[-2,0,2]

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
uniform float Position17; slider[-2,0,2]
uniform float Position18; slider[-2,0,2]
uniform float Position19; slider[-2,0,2]
uniform float Position20; slider[-2,0,2]
uniform float Position21; slider[-2,0,2]
uniform float Position22; slider[-2,0,2]
uniform float Position23; slider[-2,0,2]
uniform float Position24; slider[-2,0,2]

uniform int FrameX; slider[1,1,24]
uniform int FrameY; slider[1,2,24]
uniform int FrameZ; slider[1,3,24]

// sign involutions
uniform int flipperA; slider[0,0,16777216]
uniform int flipperB; slider[0,0,16777216]
uniform int flipperC; slider[0,0,16777216]



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
    return float[N](u[0]*v[0] + u[0]*v[18] - u[1]*v[19] - u[1]*v[1] + u[6]*v[12] - u[7]*v[13], u[0]*v[19] + u[0]*v[1] + u[1]*v[0] + u[1]*v[18] + u[6]*v[13] + u[7]*v[12], u[2]*v[2] - u[3]*v[3], u[2]*v[3] + u[3]*v[2], u[10]*v[16] - u[11]*v[17] + u[4]*v[20] + u[4]*v[22] + u[4]*v[4] - u[5]*v[21] - u[5]*v[23] - u[5]*v[5] + u[8]*v[14] - u[9]*v[15], u[10]*v[17] + u[11]*v[16] + u[4]*v[21] + u[4]*v[23] + u[4]*v[5] + u[5]*v[20] + u[5]*v[22] + u[5]*v[4] + u[8]*v[15] + u[9]*v[14], u[0]*v[6] - u[1]*v[7] + u[6]*v[4] - u[7]*v[5], u[0]*v[7] + u[1]*v[6] + u[6]*v[5] + u[7]*v[4], u[4]*v[8] - u[5]*v[9] + u[8]*v[0] - u[9]*v[1], u[4]*v[9] + u[5]*v[8] + u[8]*v[1] + u[9]*v[0], u[10]*v[2] - u[11]*v[3] + u[4]*v[10] - u[5]*v[11], u[10]*v[3] + u[11]*v[2] + u[4]*v[11] + u[5]*v[10], u[12]*v[0] - u[13]*v[1] + u[4]*v[12] - u[5]*v[13], u[12]*v[1] + u[13]*v[0] + u[4]*v[13] + u[5]*v[12], u[0]*v[14] + u[14]*v[4] - u[15]*v[5] - u[1]*v[15], u[0]*v[15] + u[14]*v[5] + u[15]*v[4] + u[1]*v[14], u[16]*v[4] - u[17]*v[5] + u[2]*v[16] - u[3]*v[17], u[16]*v[5] + u[17]*v[4] + u[2]*v[17] + u[3]*v[16], -u[10]*v[16] + u[11]*v[17] - u[4]*v[22] + u[5]*v[23], -u[10]*v[17] - u[11]*v[16] - u[4]*v[23] - u[5]*v[22], -u[4]*v[20] + u[5]*v[21] - u[8]*v[14] + u[9]*v[15], -u[4]*v[21] - u[5]*v[20] - u[8]*v[15] - u[9]*v[14],0,0);
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
    return pNorm(u,NormPower);
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
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; u[5] = JuliaVect6; u[6] = JuliaVect7; u[7] = JuliaVect8; u[8] = JuliaVect9; u[9] = JuliaVect10; u[10] = JuliaVect11; u[11] = JuliaVect12; u[12] = JuliaVect13; u[13] = JuliaVect14; u[14] = JuliaVect15; u[15] = JuliaVect16; u[16] = JuliaVect17; u[17] = JuliaVect18; u[18] = JuliaVect19; u[19] = JuliaVect20; u[20] = JuliaVect21; u[21] = JuliaVect22; u[22] = JuliaVect23; u[23] = JuliaVect24; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; u[5] = Position6; u[6] = Position7; u[7] = Position8; u[8] = Position9; u[9] = Position10; u[10] = Position11; u[11] = Position12; u[12] = Position13; u[13] = Position14; u[14] = Position15; u[15] = Position16; u[16] = Position17; u[17] = Position18; u[18] = Position19; u[19] = Position20; u[20] = Position21; u[21] = Position22; u[22] = Position23; u[23] = Position24; 
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
