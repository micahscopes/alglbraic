#version 130
#define providesInside
#define providesInit

#info TEST RUN
#include "Brute-Raytracer.frag"
#group Algebraic

const int N = 4;
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,1,2]
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
uniform vec3 frame; slider[(1,1,1),(1,2,3),(4,4,4)]
uniform float A; slider[-2,1,2]
uniform float B; slider[-2,1,2]
uniform float C; slider[-2,1,2]
uniform float D; slider[-2,1,2]
uniform int mutation1; slider[0,0,24]
uniform int mutation2; slider[0,0,24]
uniform int mutation3; slider[0,0,24]
uniform int mutation4; slider[0,0,24]
uniform int pow1; slider[0,1,24]
uniform int pow2; slider[0,1,24]
uniform int pow3; slider[0,1,24]
uniform int pow4; slider[0,1,24]

uniform int Iterations; slider[0,16,5000]
uniform float Bailout; slider[0,5,30]
uniform bool Julia; checkbox[false]
uniform bool usePrevious; checkbox[false]

//mutations
int M1[N];
int M2[N];
int M3[N];
int M4[N];

float[N] mul(float u[N], float v[N]) {
  return product(u,v);
}

float[N] mul(float a, float b[N]){
  float result[N];
  for (i = 0; i < N; ++i){
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
  for (i = 0; i < N; ++i){
    result[i] = a[i]+b[i];
  }
  return c;
}

float[N] sub(float a[N], float b[N]) {
  float c[N];
  for (i = 0; i < N; ++i){
    result[i] = a[i]-b[i];
  }
  return c;
}


float[N] inner(float u[N], float v[N]) {
    return float[N](mul(mul(-3, u[3]), v[3]), 0, 0, 0);
}


float[N] outer(float u[N], float v[N]) {
    return float[N](mul(u[3], v[3]), mul(mul(2, u[3]), v[3]), mul(mul(2, u[3]), v[3]), mul(mul(2, u[3]), v[3]));
}


float[N] rev(float u[N]) {
    return float[N](u[3], u[3], u[3], mul(-1, u[3]));
}


float norm(float a[N]){
    return inner(a,rev(a))[0];
}


float[N] loadParamsJuliaVect(out float u[N]){
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; u[5] = JuliaVect6; u[6] = JuliaVect7; u[7] = JuliaVect8;
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; u[5] = Position6; u[6] = Position7; u[7] = Position8;
    return u;
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
    int result[N] = int[N](0);
    int working[N] = int[N](0);
    for (int i = 0; i < N; i++) {
        result[i] = i;
        working[N] = i;
    }
    bool found = false;
    for (int i = 0; i < N; i++) {
        item = int(n % (N-i));
        n = floor(n / (N-i));
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
    float permutated[N] = float[N](0);
    for(int i = 0; i < N; i++) {
        if(!inverse) {
            permutated[i] = A[P[i]];
        } else {
            permutated[P[i]] = A[i];
        }
    }
    return permutated;
}


float[N] addFrame(float v[N], vec3 p){
    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return v; //error, please set frame indices to be different
    }
    for(int i = 0; i<N; i++) {
        if (i == frame.x-1) { v[i] = p.x; }
        else if (i == frame.y-1) { v[i] = p.x;  }
        else if (i == frame.z-1) { v[i] = p.x;  }
        }
return v;
}

float O[N];
float JuliaVect[N];
void init(){
    O = float[N](0);
    loadParamsPosition(O);
    loadParamsJuliaVect(JuliaVect);
	M1 = permutation(mutation1);
	M2 = permutation(mutation2);
	M3 = permutation(mutation3);
	M4 = permutation(mutation4);
}

float[N] iter(inout float z[N]) {
	return mul3(
            pow(mutate(z,M1),pow1),
            pow(mutate(z,M2),pow2),
            pow(mutate(z,M3),pow3)
            );
}

bool inside(vec3 pt) {
    float z[N] = addFrame(O,pt);
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
