from alglbraic import *
forehead = Template("""#version 130
#define providesInside
#define providesInit

#info $info
#include "Brute-Raytracer.frag"
#group Algebraic
""")
header = """
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
"""

body = """
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
    loadParamsJuliaVect(O)
	M1 = permutation(mutation1);
	M2 = permutation(mutation2);
	M3 = permutation(mutation3);
	M4 = permutation(mutation4);
}

iter(inout float z[N]) {
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
}"""
feet = """ """
dim = 8

vs = VectorSpace(dim,Fragment("","PRODUCT!!!"))
frag = (
    Fragment(forehead.substitute(info="TEST RUN"))
    + vs
    + FragmentariumParams("JuliaVect",dim,size_const="N")
    + FragmentariumParams("Position",dim,size_const="N")
    + Fragment(header,body,Fragment.get('purplePreset.frag'))
)
print frag.gl()
