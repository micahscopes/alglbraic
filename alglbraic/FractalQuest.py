from alglbraic import *

class FractalQuest(Composition):
    def __init__(self,vectorspace,info="mystery fractal",mutations=None,presets=None,formula=None):
        Composition.__init__(self)
        if formula != None:
            self.iterationFormula = formula
        elif(mutations):
            self.iterationFormula = """
float MzA[N] = mutate(z,MA);
float MzB[N] = mutate(z,MB);
z = mul(
    pwr(flipA(MzA),pow1),
    pwr(flipB(MzB),pow2)
);
            """
        self._top = self.header.substitute(info=info)
        self._upper = self.inits
        if(mutations):
            initMutations = "initMutations();"
        else:
            initMutations = ""
        self.vectorspace = vectorspace
        window = Window(vectorspace.N)
        julia = FragmentariumParams("JuliaVect",vectorspace.N,size_const="N")
        position = FragmentariumParams("Position",vectorspace.N,size_const="N")
        flippers = SignFlipper(vectorspace.N)
        self._members = [vectorspace,julia,position,window,mutations,flippers]

        self._lower = self.fractalizer.substitute(iterate=self.iterationFormula,initMutations=initMutations)
        if presets == None:
            self._bottom = Fragment.get("purplePreset.frag")

    # templates: ##############################################################

    iterationFormula = """
    z = mul(
        pwr(flipA(z),pow1),
        pwr(flipB(z),pow2)
    );
    """

    header = Template("""#version 130
#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 4

#info $info
#include "Brute-Raytracer.frag"
#group Algebraic
    """)
    inits = """
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
uniform float Bailout; slider[0,5,30]
uniform bool Julia; checkbox[false]

// instead of adding the Julia point or z(0), use z(i-1) (the last point)
uniform bool usePrevious; checkbox[false]

    """

    fractalizer = Template("""
float O[N];
float JuliaVect[N];

void init(){
    loadParamsPosition(O);
    loadParamsJuliaVect(JuliaVect);
    $initMutations
}

void iter(inout float z[N]) {
    $iterate
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
}""")
    feet = """ """
