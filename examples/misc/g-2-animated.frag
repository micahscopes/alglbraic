#version 130
#define providesInside
#define providesInit
#define SubframeMax 7
#define IterationsBetweenRedraws 8

#info GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = [-1,-1]
#include "Brute-Raytracer.frag"
#group Algebraic

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

// mutation indices (Lehmer or Lexicographic)
uniform int mutationA; slider[0,0,24]
uniform int mutationB; slider[0,0,24]
uniform int mutationC; slider[0,0,24]
uniform int mutationD; slider[0,0,24]



// extra parameters to play with (useful as weights)
uniform float A; slider[-2,1,2]
uniform float B; slider[-2,1,2]
uniform float C; slider[-2,1,2]
uniform float D; slider[-2,1,2]

// powers for multiplication, if need be
uniform int pow1; slider[0,1,24]
uniform int pow2; slider[0,1,24]
uniform int pow3; slider[0,1,24]
uniform int pow4; slider[0,1,24]

// ordinary fractal stuff
uniform int Iterations; slider[0,16,264]
uniform float Bailout; slider[-30,5,30]
uniform bool Julia; checkbox[false]

// instead of adding the Julia point or z(0), use z(i-1) (the last point)
uniform bool usePrevious; checkbox[false]
uniform float time;


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

float norm(float a[N]){
    return inner(a,rev(a))[0];
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

float[N] pow(float a[N],int n) {
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

int[N] permutationLexicographic(int i)
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

int[N] permutationLehmer(int n) {
    int result[N];
    int working[N];
    for (int i = 0; i < N; i++) {
        result[i] = i;
        working[i] = i;
    }
    int item;
    bool found = false;
    for (int i = 0; i < N; i++) {
        item = int(n % (N-i));
        n = int(floor(n / (N-i)));
        result[i] = working[item];
        for (int j = 0; j<N-i-1; j++) {
            if(working[j] == result[i]) {found = true;}
            if(found){working[j] = working[j+1];}
        }
    }
    return result;
}

int[N] permutation(int n){
  // choose which variation you want to use
  return permutationLehmer(n);
}

float[N] mutate(float A[N],int P[N],bool inverse) {
    float permutated[N] = zero();
    for(int i = 0; i < N; i++) {
        if(!inverse) {
            permutated[i] = A[P[i]];
        } else {
            permutated[P[i]] = A[i];
        }
    }
    return permutated;
}

float[N] mutate(float A[N],int P[N]) {
  return mutate(A,P,false);
}

// the mutations
int MA[N];
int MB[N];
int MC[N];
int MD[N];

void initMutations() {
	MA = permutation(mutationA);
	MB = permutation(mutationB);
	MC = permutation(mutationC);
	MD = permutation(mutationD);
}


float O[N];
float Js[N];
float JuliaVect[N];

void init(){
    loadParamsPosition(O);
    loadParamsJuliaVect(Js);
    O[0] += A*sin(Js[0]*time);
    O[1] += B*sin(Js[1]*time);
    O[2] += C*sin(Js[2]*time);
    O[3] += D*sin(Js[3]*time);
    initMutations();
}

void iter(inout float z[N]) {

float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(rev(z),MB);
float MzC[N] = mutate(z,MC);
z = mul(
    pow(MzA,pow1),
    pow(MzB,pow2)
);

}

bool inside(vec3 pt) {
    float z[N] = frame(O,pt);
    float z0[N] = z;
  	float r;
  	int i=0;
  	r=	norm(z);

    while(r<Bailout && (i<Iterations)) {
      float zprev[N];
      if (usePrevious) { zprev = z; } else { zprev = z0; }
  		iter(z);
  		z = add(z,(Julia ? JuliaVect : zprev));
  		r=norm(z);
  		i++;
  	}
	return (r<Bailout);
}
#preset Init
FOV = 0.4
Eye = -1.07838,0.473653,2.81054
Target = 3.11212,-0.311375,-6.23511
Up = 0.238239,-0.954092,0.181526
EquiRectangular = false
Gamma = 2.17595
ToneMapping = 3
Exposure = 0.3261
Brightness = 1
Contrast = 1
Saturation = 1
NormalScale = 1
AOScale = 1
Glow = 1
AOStrength = 0.6
Samples = 40
Stratify = true
DebugInside = false
CentralDifferences = true
SampleNeighbors = true
Near = 0
Far = 15
ShowDepth = false
DebugNormals = false
Specular = 1.5
SpecularExp = 16
SpotLight = 1,1,1,0.38043
SpotLightDir = 0.1,0.1
CamLight = 1,1,1,1
CamLightMin = 0
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
JuliaVect1 = 1.04132
JuliaVect2 = 0.83332
JuliaVect3 = 0.43332
JuliaVect4 = 0.66668
Position1 = 0.5512
Position2 = 0.3492
Position3 = -0.28572
Position4 = -0.09524
FrameX = 1
FrameY = 3
FrameZ = 4
mutationA = 0
mutationB = 0
mutationC = 0
mutationD = 0
A = 0.30168
B = 0.4134
C = 0
D = 0.53932
pow1 = 2
pow2 = 1
pow3 = 1
pow4 = 1
Iterations = 47
Bailout = 25.6203
Julia = false
usePrevious = false
#endpreset

#preset SomeOtherPreset
FOV = 0.4
Eye = 0.980771,1.21666,-4.38029
Target = -1.26431,-1.63188,4.93881
Up = 0.956431,0.104596,0.272579
EquiRectangular = false
Gamma = 2.17595
ToneMapping = 3
Exposure = 0.3261
Brightness = 1
Contrast = 1
Saturation = 1
NormalScale = 1
AOScale = 1
Glow = 1
AOStrength = 0.6
Samples = 40
Stratify = true
DebugInside = false
CentralDifferences = true
SampleNeighbors = true
Near = 0
Far = 15
ShowDepth = false
DebugNormals = false
Specular = 1.5
SpecularExp = 16
SpotLight = 1,1,1,0.38043
SpotLightDir = 0.1,0.1
CamLight = 1,1,1,1
CamLightMin = 0
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
JuliaVect1 = 0.54544
JuliaVect2 = -0.66668
JuliaVect3 = 0.5
JuliaVect4 = 0
Position1 = -0.23624
Position2 = -0.8254
Position3 = -0.09524
Position4 = 0.3492
FrameX = 1
FrameY = 2
FrameZ = 4
mutationA = 0
mutationB = 0
mutationC = 0
mutationD = 0
A = 0.45812
B = 0.48044
C = 0.72624
D = 0.6292
pow1 = 2
pow2 = 1
pow3 = 1
pow4 = 1
Iterations = 21
Bailout = 25.6203
Julia = true
usePrevious = false
#endpreset
