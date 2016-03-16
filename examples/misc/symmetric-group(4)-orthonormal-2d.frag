#version 130
#define providesInit
#include "Progressive2D.frag"
#info 5 dimensional fractal quest on Symmetric group algebra of order 4 over Symbolic Ring
#group Algebraic
    
// the default p-norm power (p).
uniform float NormPower; slider[0.000000001,2,100]
const int N = 5;
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]
uniform float JuliaVect5; slider[-2,0,2]

uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]
uniform float Position5; slider[-2,0,2]

uniform int FrameX; slider[1,1,5]
uniform int FrameY; slider[1,2,5]

// sign involutions
uniform int flipperA; slider[0,0,32]
uniform int flipperB; slider[0,0,32]
uniform int flipperC; slider[0,0,32]



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
    
uniform float R; slider[0,0,1]
uniform float G; slider[0,0.4,1]
uniform float B; slider[0,0.7,1]
uniform float Divider; slider[0,35,50]
uniform float Power; slider[0,0.6,6]
uniform float Radius; slider[0,1.332,5]
vec2 mapCenter = vec2(0.5,0.5);
float mapRadius =0.4;
uniform bool ShowMap; checkbox[true]
uniform float MapZoom; slider[0.01,2.1,6]

    

float[N] product(float u[N], float v[N]) {
    return float[N](u[0]*v[0] + 6*u[1]*v[1] + 3*u[2]*v[2] + 8*u[3]*v[3] + 6*u[4]*v[4], u[0]*v[1] + u[1]*v[0] + u[1]*v[2] + 4*u[1]*v[3] + u[2]*v[1] + 2*u[2]*v[4] + 4*u[3]*v[1] + 4*u[3]*v[4] + 2*u[4]*v[2] + 4*u[4]*v[3], u[0]*v[2] + 2*u[1]*v[1] + 4*u[1]*v[4] + u[2]*v[0] + 2*u[2]*v[2] + 8*u[3]*v[3] + 4*u[4]*v[1] + 2*u[4]*v[4], u[0]*v[3] + 3*u[1]*v[1] + 3*u[1]*v[4] + 3*u[2]*v[3] + u[3]*v[0] + 3*u[3]*v[2] + 4*u[3]*v[3] + 3*u[4]*v[1] + 3*u[4]*v[4], u[0]*v[4] + 2*u[1]*v[2] + 4*u[1]*v[3] + 2*u[2]*v[1] + u[2]*v[4] + 4*u[3]*v[1] + 4*u[3]*v[4] + u[4]*v[0] + u[4]*v[2] + 4*u[4]*v[3]);
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

float norm(float u[N]) {
    return pNorm(u,NormPower);
}

float[N] antipode(float u[N]) {
    return float[N](u[0], u[1], u[2], u[3], u[4]);
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
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; 
    return u;
}


float[N] frame(float v[N], vec2 p){
    // "Frame" a "window" through which to view vector v, via a "subvector" p.

    // Points p form a linear subspace of the N dimensional Euclidean space,
    // but not necessarily of the vector space we are looking at.  They are
    // really just "slices" of larger vectors.

    if(FrameX == FrameY) {
        return v; //error, please set frame indices to be different
    }
    for(int i = 0; i<N; i++) {
       if (i == FrameX-1) { v[i] = p[0]; }
        if (i == FrameY-1) { v[i] = p[1]; }
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
    
vec3 getMapColor2D(vec2 c) {
	vec2 p =  (aaCoord-mapCenter)/(mapRadius);
	p*=MapZoom; p.x/=pixelSize.x/pixelSize.y;
	if (abs(p.x)<3.0*pixelSize.y*MapZoom) return vec3(0.0,0.0,0.0);
	if (abs(p.y)<3.0*pixelSize.x*MapZoom) return vec3(0.0,0.0,0.0);
    vec2 JuliaXY = vec2(JuliaVect[FrameX-1],JuliaVect[FrameY-1]);
    p += JuliaXY;

	float z[N] = frame(O,p);
	float z0[N] = z;
	float zprev[N];
	int i = 0;
	float r = 0;
    while(r<Bailout && i<Iterations) {
      float zprev[N];
      if (usePrevious) { zprev = z; } else { zprev = z0; }
  		iter(z);
  		z = add(z,zprev);
  		r=norm(z);
  		i++;
  	}
	if ((r < Bailout && r > Bailin) || BailInvert){
		return vec3(R,G,B)*0.5;
	} else {
		return vec3(1.0);
	}
}

vec3 color(vec2 c) {
	if (ShowMap && Julia) {
		vec2 w = (aaCoord-mapCenter);
		w.y/=(pixelSize.y/pixelSize.x);
		if (length(w)<mapRadius) return getMapColor2D(c);
		if (length(w)<mapRadius+0.01) return vec3(0.0,0.0,0.0);
	}
    float z[N] = frame(O,c);
    float z0[N] = z;
  	float r;
  	int i=0;
  	r=norm(z);

    while(r<Bailout && (i<Iterations)) {
      float zprev[N];
      if (usePrevious) { zprev = z; } else { zprev = z0; }
  		iter(z);
  		z = add(z,(Julia ? JuliaVect : zprev));
  		r=norm(z);
  		i++;
  	}
	if ((r < Bailout && r > Bailin) && !BailInvert) {
		return vec3(1.0);
	} else {
		return vec3(R,G,B);
	}
}

    

#preset Default
Center = 0.58022,-0.0209826
Zoom = 0.854514
Gamma = 2.17595
ToneMapping = 3
Exposure = 1
Brightness = 1
Contrast = 1
Saturation = 1
AARange = 2
AAExp = 1
GaussianAA = true
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
mutationA = 0
mutationB = 0
mutationC = 0
mutationD = 0
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
Iterations = 264
Bailout = 5
Julia = false
usePrevious = false
R = 0
G = 0
B = 0
Divider = 30.292
Power = 0.67998
Radius = 1.332
ShowMap = true
MapZoom = 2.1
#endpreset

#preset Mandel2
Center = -0.335155,0.124422
Zoom = 630.163
Iterations = 623
R = 0.25624
G = 0.66875
B = 1
Julia = false
JuliaX = -0.6
JuliaY = 1.3
#endpreset

#preset Julia1
Center = -0.00932198,0
Zoom = 1.26502
Iterations = 69
R = 0.76875
G = 0.4
B = 0.7
Julia = true
JuliaX = -1.26472
JuliaY = -0.05884
#endpreset

#preset nice Julia
Center = 0.16416,0.0265285
Zoom = 0.854514
Iterations = 328
R = 0
G = 0.4
B = 0.7
Julia = true
JuliaX = -0.20588
JuliaY = 0.79412
ShowMap = true
MapZoom = 1.74267
#endpreset
    