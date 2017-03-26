#version 130
//#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 4
#include "DE-Raytracer.frag"

#info GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = [-1,-1]
//#include "Brute-Raytracer.frag"
#group Algebraic
    
// the default p-norm power (p).
uniform float NormPower; slider[0.2,2,100]
const int N = 4;
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]

uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]

uniform int FrameX; slider[1,1,4]
uniform int FrameY; slider[1,2,4]
uniform int FrameZ; slider[1,3,4]

// sign involutions
uniform int flipperA; slider[0,0,16]
uniform int flipperB; slider[0,0,16]
uniform int flipperC; slider[0,0,16]



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
    
#group DE
uniform float ih; slider[0,100000000,100000000]


float[N] product(float u[N], float v[N]) {
    return float[N](u[0]*v[0] - u[1]*v[1] - u[2]*v[2] - u[3]*v[3], u[0]*v[1] + u[1]*v[0] + u[2]*v[3] - u[3]*v[2], u[0]*v[2] - u[1]*v[3] + u[2]*v[0] + u[3]*v[1], u[0]*v[3] + u[1]*v[2] - u[2]*v[1] + u[3]*v[0]);
}


float[N] inner(float u[N], float v[N]) {
    return float[N](-u[1]*v[1] - u[2]*v[2] - u[3]*v[3], u[2]*v[3] - u[3]*v[2], -u[1]*v[3] + u[3]*v[1], 0);
}


float[N] outer(float u[N], float v[N]) {
    return float[N](u[0]*v[0], u[0]*v[1] + u[1]*v[0], u[0]*v[2] + u[2]*v[0], u[0]*v[3] + u[1]*v[2] - u[2]*v[1] + u[3]*v[0]);
}


float[N] rev(float u[N]) {
    return float[N](u[0], u[1], u[2], -u[3]);
}


float pNormSq(float u[N], float p) {
    float normSq = 0;
    for(int i=0; i<N; i++){
        normSq = normSq + pow(u[i],p);
    }
    return normSq;
}

float pNorm(float u[N], float p) {
    return pow(abs(pNormSq(u,p)),1.0/p);
}

//float norm(float a[N]){
//return inner(a,rev(a))[0];
//}

float norm(float a[N]){
	return pNorm(a,NormPower);
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
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; 
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

float[N] iter(float z[N]) {
    
    return mul(
        pwr(flipA(z),pow1),
        pwr(flipB(z),pow2)
    );
    
}

float DE(vec3 pt) {
    float h = 1.0/ih;
	h = pow(h,4);
    float z[N] = frame(O,pt);
    float z0[N] = z;
  	float r;
  	int i=0;
  	//r=abs(norm(z));
  	
  	float dx[N] = float[N](h,0,0,0);
  	float dy[N] = float[N](0,h,0,0);
  	float dz[N] = float[N](0,0,h,0);
  	float dw[N] = float[N](0,0,0,h);
  	
	float Rx[N]=add(z,dx);
	float Ry[N]=add(z,dy);
	float Rz[N]=add(z,dz);
	float Rw[N]=add(z,dw);
	
    while( i<Iterations) {
		float zprev[N];
		if (usePrevious) { zprev = z; } else { zprev = z0; }
		z = add(iter(z),(Julia ? JuliaVect : zprev));
		Rx = add(iter(Rx),(Julia ? JuliaVect : add(zprev,dx)));
		Ry = add(iter(Ry),(Julia ? JuliaVect : add(zprev,dy)));
		Rz = add(iter(Rz),(Julia ? JuliaVect : add(zprev,dz)));
		Rw = add(iter(Rw),(Julia ? JuliaVect : add(zprev,dw)));
		//r=norm(z);
		i++;
  	}
  	float drx = norm(sub(Rx,z))/h;
  	float dry = norm(sub(Ry,z))/h;
  	float drz = norm(sub(Rz,z))/h;
  	float drw = norm(sub(Rw,z))/h;
  	
  	return norm(z) * log(norm(z)) / sqrt(pow(drx,2) + pow(dry,2) + pow(drz,2));// + pow(drw,2));
	//return ((r < Bailout && r > Bailin) || BailInvert);
}

#preset Init
FOV = 0.4
Eye = -2.08854,1.18207,0.897848
Target = 6.31636,-3.1734,-2.32513
Up = 0.210907,-0.300889,0.930045
EquiRectangular = false
FocalPlane = 1
Aperture = 0
Gamma = 2.17595
ToneMapping = 3
Exposure = 0.3261
Brightness = 1
Contrast = 1
Saturation = 1
GaussianWeight = 1
AntiAliasScale = 2
Detail = -2.3
DetailAO = -0.5
FudgeFactor = 1
MaxRaySteps = 56
Dither = 0.5
NormalBackStep = 1
AO = 0,0,0,0.7
Specular = 1.5
SpecularExp = 16
SpecularMax = 10
SpotLight = 1,1,1,0.38043
SpotLightDir = 0.1,0.1
CamLight = 1,1,1,1
CamLightMin = 0
Glow = 1,1,1,0.16667
GlowMax = 20
Fog = 0
HardShadow = 0
ShadowSoft = 2
Reflection = 0
DebugSun = false
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
EnableFloor = true
FloorNormal = 0,0,1
FloorHeight = 0
FloorColor = 1,1,1
NormPower = 2
JuliaVect1 = 0
JuliaVect2 = 0
JuliaVect3 = 0
JuliaVect4 = 0
Position1 = 0
Position2 = 0
Position3 = 0
Position4 = 0
FrameX = 1
FrameY = 2
FrameZ = 3
flipperA = 0
flipperB = 0
flipperC = 0
auxA = 1
auxB = 1
auxC = 1
auxD = 1
pow1 = 1
pow2 = 1
pow3 = 1
pow4 = 1
Iterations = 53
Bailout = 4
Bailin = -4
BailInvert = false
Julia = false
usePrevious = false
ih = 6
#endpreset


#preset Default
FOV = 0.62536
Eye = 1.65826,-1.22975,0.277736
Target = -5.2432,4.25801,-0.607125
Up = 0.401286,0.369883,-0.83588
EquiRectangular = false
FocalPlane = 1
Aperture = 0
Gamma = 2.08335
ToneMapping = 3
Exposure = 0.6522
Brightness = 1
Contrast = 1
Saturation = 1
GaussianWeight = 1
AntiAliasScale = 2
Detail = -2.84956
DetailAO = -1.35716
FudgeFactor = 1
MaxRaySteps = 164
BoundingSphere = 2
Dither = 0.51754
NormalBackStep = 1
AO = 0,0,0,0.85185
Specular = 1.6456
SpecularExp = 16.364
SpecularMax = 10
SpotLight = 1,1,1,1
SpotLightDir = 0.63626,0.5
CamLight = 1,1,1,1.53846
CamLightMin = 0.12121
Glow = 1,1,1,0.43836
GlowMax = 52
Fog = 0
HardShadow = 0.35385
ShadowSoft = 12.5806
Reflection = 0
DebugSun = false
BaseColor = 1,1,1
OrbitStrength = 0.14286
X = 1,1,1,1
Y = 0.345098,0.666667,0,0.02912
Z = 1,0.666667,0,1
R = 0.0784314,1,0.941176,-0.0194
BackgroundColor = 0.607843,0.866667,0.560784
GradientBackground = 0.3261
CycleColors = false
Cycles = 4.04901
EnableFloor = false
FloorNormal = 0,0,0
FloorHeight = 0
FloorColor = 1,1,1
Iterations = 12
ColorIterations = 8
Power = 8
Bailout = 6.279
AlternateVersion = true
RotVector = 1,1,1
RotAngle = 0
Julia = false
JuliaC = 0,0,0
#endpreset