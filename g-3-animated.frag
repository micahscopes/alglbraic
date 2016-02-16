#version 130
#define providesInside
#define providesInit
#define SubframeMax 8
#define IterationsBetweenRedraws 4

#info GEOMETRIC ALGEBRAIC FRACTALS 2016!!! Q = [-1,-1,-1]
#include "Brute-Raytracer.frag"
#group Algebraic
uniform float time;// slider[0,0,100]
uniform bool animate; checkbox[true]
// start time offset
uniform float time0; slider[-100,0,100]
const int N = 8;
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]
uniform float JuliaVect5; slider[-2,0,2]
uniform float JuliaVect6; slider[-2,0,2]
uniform float JuliaVect7; slider[-2,0,2]
uniform float JuliaVect8; slider[-2,0,2]

uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]
uniform float Position5; slider[-2,0,2]
uniform float Position6; slider[-2,0,2]
uniform float Position7; slider[-2,0,2]
uniform float Position8; slider[-2,0,2]

uniform int FrameX; slider[1,1,8]
uniform int FrameY; slider[1,2,8]
uniform int FrameZ; slider[1,3,8]

// mutation indices (Lehmer or Lexicographic)
uniform int mutationA; slider[0,0,40320]
uniform int mutationB; slider[0,0,40320]
uniform int mutationC; slider[0,0,40320]
uniform int mutationD; slider[0,0,40320]



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
uniform int Iterations; slider[0,16,4000]
uniform float Bailout; slider[0,5,30]
uniform bool Julia; checkbox[false]

// instead of adding the Julia point or z(0), use z(i-1) (the last point)
uniform bool usePrevious; checkbox[false]



float[N] product(float u[N], float v[N]) {
    return float[N](u[0]*v[0] - u[1]*v[1] - u[2]*v[2] - u[3]*v[3] - u[4]*v[4] - u[5]*v[5] - u[6]*v[6] + u[7]*v[7], u[0]*v[1] + u[1]*v[0] + u[2]*v[4] + u[3]*v[5] - u[4]*v[2] - u[5]*v[3] - u[6]*v[7] - u[7]*v[6], u[0]*v[2] - u[1]*v[4] + u[2]*v[0] + u[3]*v[6] + u[4]*v[1] + u[5]*v[7] - u[6]*v[3] + u[7]*v[5], u[0]*v[3] - u[1]*v[5] - u[2]*v[6] + u[3]*v[0] - u[4]*v[7] + u[5]*v[1] + u[6]*v[2] - u[7]*v[4], u[0]*v[4] + u[1]*v[2] - u[2]*v[1] - u[3]*v[7] + u[4]*v[0] + u[5]*v[6] - u[6]*v[5] - u[7]*v[3], u[0]*v[5] + u[1]*v[3] + u[2]*v[7] - u[3]*v[1] - u[4]*v[6] + u[5]*v[0] + u[6]*v[4] + u[7]*v[2], u[0]*v[6] - u[1]*v[7] + u[2]*v[3] - u[3]*v[2] + u[4]*v[5] - u[5]*v[4] + u[6]*v[0] - u[7]*v[1], u[0]*v[7] + u[1]*v[6] - u[2]*v[5] + u[3]*v[4] + u[4]*v[3] - u[5]*v[2] + u[6]*v[1] + u[7]*v[0]);
}


float[N] inner(float u[N], float v[N]) {
    return float[N](-u[1]*v[1] - u[2]*v[2] - u[3]*v[3] - u[4]*v[4] - u[5]*v[5] - u[6]*v[6] + u[7]*v[7], u[2]*v[4] + u[3]*v[5] - u[4]*v[2] - u[5]*v[3] - u[6]*v[7] - u[7]*v[6], -u[1]*v[4] + u[3]*v[6] + u[4]*v[1] + u[5]*v[7] - u[6]*v[3] + u[7]*v[5], -u[1]*v[5] - u[2]*v[6] - u[4]*v[7] + u[5]*v[1] + u[6]*v[2] - u[7]*v[4], -u[3]*v[7] - u[7]*v[3], u[2]*v[7] + u[7]*v[2], -u[1]*v[7] - u[7]*v[1], 0);
}


float[N] outer(float u[N], float v[N]) {
    return float[N](u[0]*v[0], u[0]*v[1] + u[1]*v[0], u[0]*v[2] + u[2]*v[0], u[0]*v[3] + u[3]*v[0], u[0]*v[4] + u[1]*v[2] - u[2]*v[1] + u[4]*v[0], u[0]*v[5] + u[1]*v[3] - u[3]*v[1] + u[5]*v[0], u[0]*v[6] + u[2]*v[3] - u[3]*v[2] + u[6]*v[0], u[0]*v[7] + u[1]*v[6] - u[2]*v[5] + u[3]*v[4] + u[4]*v[3] - u[5]*v[2] + u[6]*v[1] + u[7]*v[0]);
}


float[N] rev(float u[N]) {
    return float[N](u[0], u[1], u[2], u[3], -u[4], -u[5], -u[6], -u[7]);
}


float norm2(float u[N]) {
    return pow(pow(u[0], 2.0) + pow(u[1], 2.0) + pow(u[2], 2.0) + pow(u[3], 2.0) + pow(u[4], 2.0) + pow(u[5], 2.0) + pow(u[6], 2.0) + pow(u[7], 2.0), 0.5);
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
float TIME;
void init(){
    if(animate) {
		TIME = time + time0;
    } else { TIME = time0; }
    loadParamsPosition(O);
    loadParamsJuliaVect(Js);
    O[0] += A*sin(Js[0]*TIME);
    O[1] += B*sin(Js[1]*TIME);
    O[2] += C*sin(Js[2]*TIME);
    O[3] += D*sin(Js[3]*TIME);
    O[4] += A*sin(Js[4]*TIME);
    O[5] += B*cos(Js[5]*TIME);
    O[6] += C*cos(Js[6]*TIME);
    O[7] += D*sin(Js[7]*TIME);
    initMutations();
}

void iter(inout float z[N]) {

float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(z,MB);
float MzC[N] = mutate(rev(z),MC);
z = mul(
    pow(MzA,pow1),
    pow(MzC,pow3)
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
	return (r<Bailout);
}
#preset Init
FOV = 0.41112
Eye = -0.882505,2.01321,0.198164
Target = 2.68279,-7.31509,-0.323124
Up = -0.878512,-0.325521,-0.349648
EquiRectangular = false
Gamma = 1.44655
ToneMapping = 4
Exposure = 1
Brightness = 1.19565
Contrast = 1
Saturation = 0.79135
NormalScale = 0.3211
AOScale = 0.8029
Glow = 0.34177
AOStrength = 0.65487
Samples = 100
Stratify = true
DebugInside = false
CentralDifferences = true
SampleNeighbors = true
Near = 0
Far = 22.866
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
JuliaVect1 = 0.11572
JuliaVect2 = 0.16668
JuliaVect3 = -0.13332
JuliaVect4 = 0.3
JuliaVect5 = -1.53332
JuliaVect6 = 0.36668
JuliaVect7 = -0.26668
JuliaVect8 = 0.16668
Position1 = 0
Position2 = 0
Position3 = 0
Position4 = 0
Position5 = 0
Position6 = 0
Position7 = 0
Position8 = 0
FrameX = 6
FrameY = 7
FrameZ = 8
mutationA = 0
mutationB = 0
mutationC = 0
mutationD = 0
A = -0.14524
B = 0.4134
C = 0.72624
D = 0.67416
pow1 = 1
pow2 = 1
pow3 = 1
pow4 = 1
Iterations = 54
Bailout = 22.9926
Julia = false
usePrevious = false
animate = false
time0 = 31.344
#endpreset

#preset WOAH
FOV = 0.4
Eye = -2.01763,3.77525,-0.458302
Target = 2.3839,-5.13122,0.682544
Up = -0.575418,-0.386429,-0.720809
EquiRectangular = false
Gamma = 2.3585
ToneMapping = 4
Exposure = 0.99999
Brightness = 0.86955
Contrast = 1.75495
Saturation = 1
NormalScale = 0.3211
AOScale = 0.8029
Glow = 1
AOStrength = 0.77876
Samples = 51
Stratify = true
DebugInside = false
CentralDifferences = true
SampleNeighbors = true
Near = 0
Far = 27.9879
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
JuliaVect1 = 0.281
JuliaVect2 = 1.36668
JuliaVect3 = -1
JuliaVect4 = 0.43332
JuliaVect5 = 0.23332
JuliaVect6 = -0.36668
JuliaVect7 = 0.43332
JuliaVect8 = -0.1
Position1 = 0
Position2 = 0
Position3 = 0
Position4 = 0
Position5 = 0
Position6 = 0
Position7 = 0
Position8 = 0
FrameX = 6
FrameY = 7
FrameZ = 8
mutationA = 0
mutationB = 0
mutationC = 0
mutationD = 0
A = -0.14524
B = 0.21228
C = 0.18996
D = 0.04496
pow1 = 1
pow2 = 1
pow3 = 1
pow4 = 1
Iterations = 21
Bailout = 5
Julia = false
usePrevious = false
#endpreset

#preset z^3 form
FOV = 0.4
Eye = 0.323691,0.458608,4.16801
Target = -0.451619,-0.819078,-5.71968
Up = -0.864252,-0.488001,0.122165
EquiRectangular = false
Gamma = 2.3585
ToneMapping = 4
Exposure = 0.99999
Brightness = 0.86955
Contrast = 1.75495
Saturation = 1
NormalScale = 1
AOScale = 1
Glow = 0.1
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
JuliaVect1 = 0.281
JuliaVect2 = 1.36668
JuliaVect3 = -1
JuliaVect4 = 0.43332
JuliaVect5 = 0.23332
JuliaVect6 = -0.36668
JuliaVect7 = 0.43332
JuliaVect8 = -0.1
Position1 = 0.3622
Position2 = 0
Position3 = 0.31748
Position4 = -0.53968
Position5 = -0.79364
Position6 = -0.31748
Position7 = -0.50792
Position8 = 0
FrameX = 1
FrameY = 2
FrameZ = 6
mutationA = 0
mutationB = 0
mutationC = 0
mutationD = 0
A = -0.14524
B = 0.21228
C = 0.18996
D = 0.04496
pow1 = 1
pow2 = 1
pow3 = 1
pow4 = 1
Bailout = 5
Julia = false
usePrevious = false
Iterations = 16
#endpreset