#version 130
#define providesInside
#define providesInit

#info Geometric Algebra G([-1,-1])
#include "Brute-Raytracer.frag"
#group Geometric Algebraic

// Remaining Constant
uniform vec3 frame; slider[(1,1,1),(1,2,3),(4,4,4)]
uniform float position1; slider[-2,0,2]
uniform float position2; slider[-2,0,2]
uniform float position3; slider[-2,0,2]
uniform float position4; slider[-2,0,2]

uniform float weight1; slider[-2,1,2]
uniform float weight2; slider[-2,1,2]


uniform int Permutation1; slider[0,0,24]
uniform int Permutation2; slider[0,0,24]
uniform int Permutation3; slider[0,0,24]
uniform int Permutation4; slider[0,0,24]
uniform int Iterations; slider[0,16,5000]
uniform float Bailout; slider[0,5,30]

uniform bool Julia; checkbox[false]
uniform bool usePrevious; checkbox[false]
const int N = 4;
int P1[N];
int P2[N];
int P3[N];
int P4[N];
uniform float JuliaG1; slider[-2,0,2]
uniform float JuliaG2; slider[-2,0,2]
uniform float JuliaG3; slider[-2,0,2]
uniform float JuliaG4; slider[-2,0,2]
struct Geo{
vec4 q0;

};

Geo Geo0(){
return Geo(
	vec4(0,0,0,0)
);
}



    const Geo I = Geo(
	vec4(0,0,0,1)
);

Geo inner(Geo a, Geo b){
return Geo(
	vec4(-a.q0[1]*b.q0[1] - a.q0[2]*b.q0[2] - a.q0[3]*b.q0[3],a.q0[2]*b.q0[3] - a.q0[3]*b.q0[2],-a.q0[1]*b.q0[3] + a.q0[3]*b.q0[1],0)
);
}

Geo outer(Geo a, Geo b){
return Geo(
	vec4(a.q0[0]*b.q0[0],a.q0[0]*b.q0[1] + a.q0[1]*b.q0[0],a.q0[0]*b.q0[2] + a.q0[2]*b.q0[0],a.q0[0]*b.q0[3] + a.q0[1]*b.q0[2] - a.q0[2]*b.q0[1] + a.q0[3]*b.q0[0])
);
}

Geo g(Geo a, Geo b){
return Geo(
	vec4(a.q0[0]*b.q0[0] - a.q0[1]*b.q0[1] - a.q0[2]*b.q0[2] - a.q0[3]*b.q0[3],a.q0[0]*b.q0[1] + a.q0[1]*b.q0[0] + a.q0[2]*b.q0[3] - a.q0[3]*b.q0[2],a.q0[0]*b.q0[2] - a.q0[1]*b.q0[3] + a.q0[2]*b.q0[0] + a.q0[3]*b.q0[1],a.q0[0]*b.q0[3] + a.q0[1]*b.q0[2] - a.q0[2]*b.q0[1] + a.q0[3]*b.q0[0])
);
}

Geo set(Geo a, int i, float x){

    switch(i) {     case 0 : a.q0[0]=x; break;     case 1 : a.q0[1]=x; break;     case 2 : a.q0[2]=x; break;     case 3 : a.q0[3]=x; break;
    }
    return a;
}

float get(Geo a, int i){
    switch(i){     case 0 : return a.q0[0]; break;     case 1 : return a.q0[1]; break;     case 2 : return a.q0[2]; break;     case 3 : return a.q0[3]; break;}
}

float getPosition(int i){
    switch(i){     case 0 : return position1; break;     case 1 : return position2; break;     case 2 : return position3; break;     case 3 : return position4; break;}
}
Geo loadPositions(Geo g){

    for(int i = 0; i<4; i++) {
        g = set(g,i,getPosition(i));
    }
    return g;
}
    Geo addFrame(Geo g, vec3 p){

    if(frame.x == frame.y || frame.y == frame.z || frame.x == frame.z) {
        return g; //error, please set frame indices to be different
    }
    for(int i = 0; i<4; i++) {
        if (i == frame.x-1) { g = set(g,i,p.x); }
        else if (i == frame.y-1) { g = set(g,i,p.y); }
        else if (i == frame.z-1) { g = set(g,i,p.z); }
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

Geo mutate(Geo A,int[N] perm,bool inv) {
    Geo permutated = Geo0();
    for(int i = 0; i < N; i++) {
        if(!inv) {
            permutated = set(permutated,i,get(A,perm[i]));
        } else {
            permutated = set(permutated,perm[i],get(A,i));
        }
    }
    return permutated;
}

Geo aGeo(float a, Geo b){
return Geo(
	vec4(a*b.q0[0],a*b.q0[1],a*b.q0[2],a*b.q0[3])
);
}

Geo rev(Geo a){
return Geo(
	vec4(a.q0[0],a.q0[1],a.q0[2],-a.q0[3])
);
}

Geo invo(Geo a){
return aGeo(pow(-1,4),a);
}

Geo cong(Geo a){
return invo(rev(a));
}



Geo g3(Geo a,Geo b, Geo c) {
	return g(a,g(b,c));
}

Geo g4(Geo a, Geo b, Geo c, Geo d) {
	return g(a,g3(b,c,d));
}

Geo gpwr(Geo a,int n) {
	Geo r = a;
	for (int i=0;i<n-1;i++){
	r = g(r,a);
}
return r;
}

Geo add(Geo a, Geo b) {
    return Geo(a.q0 + b.q0);
}float geoNorm(Geo a){
return get(inner(a,rev(a)),0);
}


Geo O = Geo0();
void init(){
    // 'a is for ..., ..., 'O' is for origin, ...'
    O = loadPositions(O);
		P1 = permutation(Permutation1);
		P2 = permutation(Permutation2);
		P3 = permutation(Permutation3);
		P4 = permutation(Permutation4);
}


Geo dual(Geo a) {
	return g(I,a);
}



Geo iter(Geo z, int iter) {
	//if(iter%3 ==0) {
		return 	g3(mutate(z,P1,false),
					mutate(z,P2,false),
					mutate(z,P3,false)
					//,mutate(z,P4,false)
					);
	//} else if (iter%3==1) {
	//	return g(mutate(z,P2,false),z);
	//} else {
	//	return g(mutate(z,P3,false),z);
	//}
}

bool inside(vec3 pt) {
    Geo z = addFrame(O,pt);
    Geo z0 = z;
	float r;
	int i=0;
	r=abs(geoNorm(z));
Geo JuliaGeo = Geo(
	vec4(JuliaG1,JuliaG2,JuliaG3,JuliaG4)
);

        while(r<Bailout && (i<Iterations)) {
        Geo zprev;
        if (usePrevious) { zprev = z; } else { zprev = z0; }
		z = iter(z,i);
		z = add(z,aGeo(weight1,(Julia ? JuliaGeo : zprev)));
		r=geoNorm(z);
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

#preset hmm
FOV = 0.4
Eye = 0.923887,-1.93196,0.907554
Target = -3.67744,5.4724,-3.99177
Up = 0.151185,0.616697,0.772546
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
Far = 5
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
frame = 1,2,3
position1 = 0
position2 = 0
position3 = 0
position4 = 0
Permutation = 14
Iterations = 81
Bailout = 10.7298
Julia = false
usePrevious = true
JuliaG1 = 0
JuliaG2 = 0
JuliaG3 = 0
JuliaG4 = 0
#endpreset

#preset recenter
position1 = 0.0
position2 = 0.0
position3 = 0.0
position4 = 0.0
#endpreset
