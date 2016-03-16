from alglbraic import *
import sys

class FractalQuest(Composition):
    def __init__(self,vectorspace,info="mystery fractal",mutations=None,presets=None,formula=None,windowDimensions=3):
        Composition.__init__(self)
        is2d = windowDimensions == 2
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
        header = self.header2d if is2d else self.header3d
        self._top = header.substitute(info=info)
        inits = self.inits
        if is2d:
            inits += self.inits2d
        self._upper = inits
        if(mutations):
            initMutations = "initMutations();"
        else:
            initMutations = ""
        self.vectorspace = vectorspace
        frames = ["X","Y"] if is2d else ["X","Y","Z"]
        window = Window(vectorspace.N,frames)
        julia = FragmentariumParams("JuliaVect",vectorspace.N,size_const="N")
        position = FragmentariumParams("Position",vectorspace.N,size_const="N")
        flippers = SignFlipper(vectorspace.N)
        self._members = [vectorspace,julia,position,window,mutations,flippers]
        self._lower = self.fractalizer.substitute(iterate=self.iterationFormula,initMutations=initMutations)
        self._lower += self.inside2d if is2d else self.inside3d
        if is2d:
            presets = self.presets2d
        if presets == None:
            self._bottom = Fragment.get("purplePreset.frag")
        else:
            self._bottom = presets

    # templates: ##############################################################

    iterationFormula = """
    z = mul(
        pwr(flipA(z),pow1),
        pwr(flipB(z),pow2)
    );
    """

    header3d = Template("""#version 130
#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 4

#info $info
#include "Brute-Raytracer.frag"
#group Algebraic
    """)

    header2d = Template("""#version 130
#define providesInit
#include "Progressive2D.frag"
#info $info
#group Algebraic
    """)

    inits = """
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
    """

    inits2d = """
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
    """)

    inside3d= """
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
"""

    inside2d = """
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

    """

    feet = """ """
    presets2d = """
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
    """
    @staticmethod
    def askToContinue():
        # raw_input returns the empty string for "enter"
        yes = set(['yes','y','ye'])
        no = set(['no','n',''])
        sys.stdout.write("Initiate fractal quest? [y/N]   ")
        choice = raw_input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            return askToContinue()
