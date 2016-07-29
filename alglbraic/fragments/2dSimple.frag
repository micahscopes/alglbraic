#include "Progressive2D.frag"
#info Mandelbrot
#group Mandelbrot

// Number of iterations

uniform float R; slider[0,0,1]
uniform float G; slider[0,0.4,1]
uniform float B; slider[0,0.7,1]

vec2 mapCenter = vec2(0.5,0.5);
float mapRadius =0.4;
uniform bool ShowMap; checkbox[true]
uniform float MapZoom; slider[0.01,2.1,6]

vec3 getMapColor2D(vec2 c) {
	vec2 p =  (aaCoord-mapCenter)/(mapRadius);
	p*=MapZoom; p.x/=pixelSize.x/pixelSize.y;
	if (abs(p.x)<3.0*pixelSize.y*MapZoom) return vec3(0.0,0.0,0.0);
	if (abs(p.y)<3.0*pixelSize.x*MapZoom) return vec3(0.0,0.0,0.0);
	p +=vec2(JuliaX, JuliaY) ;

	float z[N] = frame(O,pt);
	float z0[N] = z;

	int i = 0;
	for (i = 0; i < Iterations; i++) {
		z = add(iter(z),z0);
		if (norm(z,z)> 200.0) break;
	}
	if (i < Iterations) {
		float co =  float( i) + 1.0 - log2(.5*log2(dot(z,z)));
		co = sqrt(co/256.0);
		return vec3( .5+.5*cos(6.2831*co),.5+.5*cos(6.2831*co),.5+.5*cos(6.2831*co) );
	}  else {
		return vec3(0.0);
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

	vec2 z = Julia ?  z : z0;
	int i = 0;
	float dist = 10000.0;
	for (i = 0; i < Iterations; i++) {
		float zprev[N];
		if (usePrevious) { zprev = z; } else { zprev = z0; }
		iter(z);
		z = add(z,(Julia ? JuliaVect : zprev));
		if (norm(z,z)> 100.0) break;
		dist = min(dist, norm(z)-Radius);
		i++;
	}

	if (i < Iterations) {
		// The color scheme here is based on one
		// from Inigo Quilez's Shader Toy:
		float co = float( i) + 1.0 - log2(.5*log2(dot(z,z)));
		co = sqrt(co/256.0);
		float  co2 = dist * Divider;
		//co += co2;
		float fac = clamp(1.0/pow(co2,Power),0.0,1.0);
		return fac*vec3( .5+.5*cos(6.2831*co+R),
			.5+.5*cos(6.2831*co+G),
			.5+.5*cos(6.2831*co+B) );
	}  else {
		return vec3(0.0);
	}

}

#preset Default
Gamma = 2.17595
ToneMapping = 3
Brightness = 1
Contrast = 1
Saturation = 1
Center = 0.135478,-0.0513789
Zoom = 0.854514
Exposure = 1
AARange = 2
AAExp = 1
GaussianAA = true
Julia = false
JuliaX = -0.6
JuliaY = 1.3
ShowMap = false
MapZoom = 2.1
powA = 3
powB = 0
R = 0.60656
G = 0.11957
B = 0.3388
Iterations = 328
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
