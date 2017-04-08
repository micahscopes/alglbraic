#version 130
#define providesInside
#define providesInit
#define SubframeMax 9
#define IterationsBetweenRedraws 4

#info Clifford Algebra with signature [1,1,1,1,-1]
#include "Brute-Raytracer.frag"
#group Algebraic
    
// the default p-norm power (p).
uniform float NormPower; slider[0.000000001,2,100]
const int N = 32;
uniform float JuliaVect1; slider[-2,0,2]
uniform float JuliaVect2; slider[-2,0,2]
uniform float JuliaVect3; slider[-2,0,2]
uniform float JuliaVect4; slider[-2,0,2]
uniform float JuliaVect5; slider[-2,0,2]
uniform float JuliaVect6; slider[-2,0,2]
uniform float JuliaVect7; slider[-2,0,2]
uniform float JuliaVect8; slider[-2,0,2]
uniform float JuliaVect9; slider[-2,0,2]
uniform float JuliaVect10; slider[-2,0,2]
uniform float JuliaVect11; slider[-2,0,2]
uniform float JuliaVect12; slider[-2,0,2]
uniform float JuliaVect13; slider[-2,0,2]
uniform float JuliaVect14; slider[-2,0,2]
uniform float JuliaVect15; slider[-2,0,2]
uniform float JuliaVect16; slider[-2,0,2]
uniform float JuliaVect17; slider[-2,0,2]
uniform float JuliaVect18; slider[-2,0,2]
uniform float JuliaVect19; slider[-2,0,2]
uniform float JuliaVect20; slider[-2,0,2]
uniform float JuliaVect21; slider[-2,0,2]
uniform float JuliaVect22; slider[-2,0,2]
uniform float JuliaVect23; slider[-2,0,2]
uniform float JuliaVect24; slider[-2,0,2]
uniform float JuliaVect25; slider[-2,0,2]
uniform float JuliaVect26; slider[-2,0,2]
uniform float JuliaVect27; slider[-2,0,2]
uniform float JuliaVect28; slider[-2,0,2]
uniform float JuliaVect29; slider[-2,0,2]
uniform float JuliaVect30; slider[-2,0,2]
uniform float JuliaVect31; slider[-2,0,2]
uniform float JuliaVect32; slider[-2,0,2]

uniform float Position1; slider[-2,0,2]
uniform float Position2; slider[-2,0,2]
uniform float Position3; slider[-2,0,2]
uniform float Position4; slider[-2,0,2]
uniform float Position5; slider[-2,0,2]
uniform float Position6; slider[-2,0,2]
uniform float Position7; slider[-2,0,2]
uniform float Position8; slider[-2,0,2]
uniform float Position9; slider[-2,0,2]
uniform float Position10; slider[-2,0,2]
uniform float Position11; slider[-2,0,2]
uniform float Position12; slider[-2,0,2]
uniform float Position13; slider[-2,0,2]
uniform float Position14; slider[-2,0,2]
uniform float Position15; slider[-2,0,2]
uniform float Position16; slider[-2,0,2]
uniform float Position17; slider[-2,0,2]
uniform float Position18; slider[-2,0,2]
uniform float Position19; slider[-2,0,2]
uniform float Position20; slider[-2,0,2]
uniform float Position21; slider[-2,0,2]
uniform float Position22; slider[-2,0,2]
uniform float Position23; slider[-2,0,2]
uniform float Position24; slider[-2,0,2]
uniform float Position25; slider[-2,0,2]
uniform float Position26; slider[-2,0,2]
uniform float Position27; slider[-2,0,2]
uniform float Position28; slider[-2,0,2]
uniform float Position29; slider[-2,0,2]
uniform float Position30; slider[-2,0,2]
uniform float Position31; slider[-2,0,2]
uniform float Position32; slider[-2,0,2]

uniform int FrameX; slider[1,1,32]
uniform int FrameY; slider[1,2,32]
uniform int FrameZ; slider[1,3,32]

// sign involutions
uniform int flipperA; slider[0,0,4294967296]
uniform int flipperB; slider[0,0,4294967296]
uniform int flipperC; slider[0,0,4294967296]



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
    

float[N] product(float u[N], float v[N]) {
    return float[N](u[0]*v[0] - u[10]*v[10] - u[11]*v[11] - u[12]*v[12] + u[13]*v[13] - u[14]*v[14] + u[15]*v[15] + u[16]*v[16] + u[17]*v[17] - u[18]*v[18] - u[19]*v[19] + u[1]*v[1] - u[20]*v[20] + u[21]*v[21] - u[22]*v[22] + u[23]*v[23] + u[24]*v[24] + u[25]*v[25] - u[26]*v[26] + u[27]*v[27] + u[28]*v[28] + u[29]*v[29] - u[2]*v[2] + u[30]*v[30] - u[31]*v[31] - u[3]*v[3] + u[4]*v[4] - u[5]*v[5] - u[6]*v[6] - u[7]*v[7] - u[8]*v[8] + u[9]*v[9], u[0]*v[1] + u[10]*v[25] - u[11]*v[26] + u[12]*v[27] + u[13]*v[28] + u[14]*v[29] + u[15]*v[30] - u[16]*v[31] - u[17]*v[2] - u[18]*v[3] + u[19]*v[4] + u[1]*v[0] - u[20]*v[5] - u[21]*v[6] - u[22]*v[7] - u[23]*v[8] + u[24]*v[9] - u[25]*v[10] - u[26]*v[11] - u[27]*v[12] + u[28]*v[13] - u[29]*v[14] + u[2]*v[17] + u[30]*v[15] + u[31]*v[16] - u[3]*v[18] - u[4]*v[19] - u[5]*v[20] + u[6]*v[21] - u[7]*v[22] + u[8]*v[23] + u[9]*v[24], u[0]*v[2] - u[10]*v[18] - u[11]*v[19] - u[12]*v[20] + u[13]*v[21] - u[14]*v[22] + u[15]*v[23] + u[16]*v[24] - u[17]*v[1] + u[18]*v[10] + u[19]*v[11] + u[1]*v[17] + u[20]*v[12] - u[21]*v[13] + u[22]*v[14] - u[23]*v[15] - u[24]*v[16] + u[25]*v[3] - u[26]*v[4] + u[27]*v[5] + u[28]*v[6] + u[29]*v[7] + u[2]*v[0] + u[30]*v[8] - u[31]*v[9] + u[3]*v[25] - u[4]*v[26] + u[5]*v[27] + u[6]*v[28] + u[7]*v[29] + u[8]*v[30] - u[9]*v[31], u[0]*v[3] - u[10]*v[17] + u[11]*v[22] - u[12]*v[23] - u[13]*v[24] + u[14]*v[19] + u[15]*v[20] - u[16]*v[21] - u[17]*v[10] + u[18]*v[1] - u[19]*v[14] + u[1]*v[18] + u[20]*v[15] + u[21]*v[16] - u[22]*v[11] - u[23]*v[12] + u[24]*v[13] + u[25]*v[2] + u[26]*v[7] + u[27]*v[8] - u[28]*v[9] - u[29]*v[4] + u[2]*v[25] + u[30]*v[5] + u[31]*v[6] + u[3]*v[0] + u[4]*v[29] + u[5]*v[30] - u[6]*v[31] - u[7]*v[26] + u[8]*v[27] + u[9]*v[28], u[0]*v[4] - u[10]*v[22] + u[11]*v[17] + u[12]*v[24] + u[13]*v[23] + u[14]*v[18] - u[15]*v[21] + u[16]*v[20] - u[17]*v[11] + u[18]*v[14] - u[19]*v[1] + u[1]*v[19] - u[20]*v[16] - u[21]*v[15] - u[22]*v[10] + u[23]*v[13] - u[24]*v[12] + u[25]*v[7] + u[26]*v[2] - u[27]*v[9] + u[28]*v[8] - u[29]*v[3] + u[2]*v[26] - u[30]*v[6] - u[31]*v[5] + u[3]*v[29] + u[4]*v[0] - u[5]*v[31] + u[6]*v[30] - u[7]*v[25] - u[8]*v[28] - u[9]*v[27], u[0]*v[5] - u[10]*v[23] + u[11]*v[24] - u[12]*v[17] - u[13]*v[22] + u[14]*v[21] + u[15]*v[18] - u[16]*v[19] - u[17]*v[12] + u[18]*v[15] - u[19]*v[16] + u[1]*v[20] + u[20]*v[1] + u[21]*v[14] - u[22]*v[13] - u[23]*v[10] + u[24]*v[11] + u[25]*v[8] + u[26]*v[9] + u[27]*v[2] - u[28]*v[7] - u[29]*v[6] + u[2]*v[27] + u[30]*v[3] + u[31]*v[4] + u[3]*v[30] + u[4]*v[31] + u[5]*v[0] - u[6]*v[29] - u[7]*v[28] + u[8]*v[25] + u[9]*v[26], u[0]*v[6] - u[10]*v[24] + u[11]*v[23] + u[12]*v[22] + u[13]*v[17] + u[14]*v[20] - u[15]*v[19] + u[16]*v[18] - u[17]*v[13] + u[18]*v[16] - u[19]*v[15] + u[1]*v[21] - u[20]*v[14] - u[21]*v[1] - u[22]*v[12] + u[23]*v[11] - u[24]*v[10] + u[25]*v[9] + u[26]*v[8] - u[27]*v[7] + u[28]*v[2] - u[29]*v[5] + u[2]*v[28] - u[30]*v[4] - u[31]*v[3] + u[3]*v[31] + u[4]*v[30] - u[5]*v[29] + u[6]*v[0] - u[7]*v[27] - u[8]*v[26] - u[9]*v[25], u[0]*v[7] - u[10]*v[19] - u[11]*v[18] + u[12]*v[21] - u[13]*v[20] - u[14]*v[17] - u[15]*v[24] - u[16]*v[23] - u[17]*v[14] + u[18]*v[11] + u[19]*v[10] + u[1]*v[22] - u[20]*v[13] + u[21]*v[12] + u[22]*v[1] + u[23]*v[16] + u[24]*v[15] + u[25]*v[4] - u[26]*v[3] - u[27]*v[6] - u[28]*v[5] + u[29]*v[2] + u[2]*v[29] - u[30]*v[9] + u[31]*v[8] + u[3]*v[26] - u[4]*v[25] - u[5]*v[28] - u[6]*v[27] + u[7]*v[0] - u[8]*v[31] + u[9]*v[30], u[0]*v[8] - u[10]*v[20] - u[11]*v[21] - u[12]*v[18] + u[13]*v[19] - u[14]*v[24] + u[15]*v[17] + u[16]*v[22] - u[17]*v[15] + u[18]*v[12] + u[19]*v[13] + u[1]*v[23] + u[20]*v[10] - u[21]*v[11] + u[22]*v[16] - u[23]*v[1] - u[24]*v[14] + u[25]*v[5] - u[26]*v[6] + u[27]*v[3] + u[28]*v[4] + u[29]*v[9] + u[2]*v[30] + u[30]*v[2] - u[31]*v[7] + u[3]*v[27] - u[4]*v[28] + u[5]*v[25] + u[6]*v[26] + u[7]*v[31] + u[8]*v[0] - u[9]*v[29], u[0]*v[9] - u[10]*v[21] - u[11]*v[20] + u[12]*v[19] - u[13]*v[18] - u[14]*v[23] - u[15]*v[22] - u[16]*v[17] - u[17]*v[16] + u[18]*v[13] + u[19]*v[12] + u[1]*v[24] - u[20]*v[11] + u[21]*v[10] + u[22]*v[15] + u[23]*v[14] + u[24]*v[1] + u[25]*v[6] - u[26]*v[5] - u[27]*v[4] - u[28]*v[3] + u[29]*v[8] + u[2]*v[31] - u[30]*v[7] + u[31]*v[2] + u[3]*v[28] - u[4]*v[27] - u[5]*v[26] - u[6]*v[25] + u[7]*v[30] - u[8]*v[29] + u[9]*v[0], u[0]*v[10] + u[10]*v[0] + u[11]*v[29] + u[12]*v[30] - u[13]*v[31] - u[14]*v[26] + u[15]*v[27] + u[16]*v[28] - u[17]*v[3] - u[18]*v[2] - u[19]*v[7] + u[1]*v[25] - u[20]*v[8] + u[21]*v[9] + u[22]*v[4] - u[23]*v[5] - u[24]*v[6] - u[25]*v[1] + u[26]*v[14] - u[27]*v[15] - u[28]*v[16] + u[29]*v[11] + u[2]*v[18] + u[30]*v[12] - u[31]*v[13] - u[3]*v[17] + u[4]*v[22] - u[5]*v[23] - u[6]*v[24] + u[7]*v[19] + u[8]*v[20] - u[9]*v[21], u[0]*v[11] + u[10]*v[29] + u[11]*v[0] - u[12]*v[31] + u[13]*v[30] - u[14]*v[25] - u[15]*v[28] - u[16]*v[27] - u[17]*v[4] - u[18]*v[7] - u[19]*v[2] + u[1]*v[26] + u[20]*v[9] - u[21]*v[8] + u[22]*v[3] + u[23]*v[6] + u[24]*v[5] - u[25]*v[14] + u[26]*v[1] + u[27]*v[16] + u[28]*v[15] + u[29]*v[10] + u[2]*v[19] - u[30]*v[13] + u[31]*v[12] - u[3]*v[22] + u[4]*v[17] + u[5]*v[24] + u[6]*v[23] + u[7]*v[18] - u[8]*v[21] + u[9]*v[20], u[0]*v[12] + u[10]*v[30] + u[11]*v[31] + u[12]*v[0] - u[13]*v[29] - u[14]*v[28] + u[15]*v[25] + u[16]*v[26] - u[17]*v[5] - u[18]*v[8] - u[19]*v[9] + u[1]*v[27] - u[20]*v[2] + u[21]*v[7] + u[22]*v[6] - u[23]*v[3] - u[24]*v[4] - u[25]*v[15] + u[26]*v[16] - u[27]*v[1] - u[28]*v[14] + u[29]*v[13] + u[2]*v[20] + u[30]*v[10] - u[31]*v[11] - u[3]*v[23] + u[4]*v[24] - u[5]*v[17] - u[6]*v[22] + u[7]*v[21] + u[8]*v[18] - u[9]*v[19], u[0]*v[13] + u[10]*v[31] + u[11]*v[30] - u[12]*v[29] + u[13]*v[0] - u[14]*v[27] - u[15]*v[26] - u[16]*v[25] - u[17]*v[6] - u[18]*v[9] - u[19]*v[8] + u[1]*v[28] + u[20]*v[7] - u[21]*v[2] + u[22]*v[5] + u[23]*v[4] + u[24]*v[3] - u[25]*v[16] + u[26]*v[15] + u[27]*v[14] + u[28]*v[1] + u[29]*v[12] + u[2]*v[21] - u[30]*v[11] + u[31]*v[10] - u[3]*v[24] + u[4]*v[23] + u[5]*v[22] + u[6]*v[17] + u[7]*v[20] - u[8]*v[19] + u[9]*v[18], u[0]*v[14] + u[10]*v[26] - u[11]*v[25] - u[12]*v[28] - u[13]*v[27] + u[14]*v[0] - u[15]*v[31] + u[16]*v[30] - u[17]*v[7] - u[18]*v[4] + u[19]*v[3] + u[1]*v[29] + u[20]*v[6] + u[21]*v[5] - u[22]*v[2] + u[23]*v[9] - u[24]*v[8] - u[25]*v[11] - u[26]*v[10] + u[27]*v[13] - u[28]*v[12] - u[29]*v[1] + u[2]*v[22] - u[30]*v[16] - u[31]*v[15] - u[3]*v[19] - u[4]*v[18] + u[5]*v[21] - u[6]*v[20] - u[7]*v[17] - u[8]*v[24] - u[9]*v[23], u[0]*v[15] + u[10]*v[27] - u[11]*v[28] + u[12]*v[25] + u[13]*v[26] + u[14]*v[31] + u[15]*v[0] - u[16]*v[29] - u[17]*v[8] - u[18]*v[5] + u[19]*v[6] + u[1]*v[30] - u[20]*v[3] - u[21]*v[4] - u[22]*v[9] - u[23]*v[2] + u[24]*v[7] - u[25]*v[12] - u[26]*v[13] - u[27]*v[10] + u[28]*v[11] - u[29]*v[16] + u[2]*v[23] + u[30]*v[1] + u[31]*v[14] - u[3]*v[20] - u[4]*v[21] - u[5]*v[18] + u[6]*v[19] - u[7]*v[24] + u[8]*v[17] + u[9]*v[22], u[0]*v[16] + u[10]*v[28] - u[11]*v[27] - u[12]*v[26] - u[13]*v[25] + u[14]*v[30] - u[15]*v[29] + u[16]*v[0] - u[17]*v[9] - u[18]*v[6] + u[19]*v[5] + u[1]*v[31] + u[20]*v[4] + u[21]*v[3] - u[22]*v[8] + u[23]*v[7] - u[24]*v[2] - u[25]*v[13] - u[26]*v[12] + u[27]*v[11] - u[28]*v[10] - u[29]*v[15] + u[2]*v[24] - u[30]*v[14] - u[31]*v[1] - u[3]*v[21] - u[4]*v[20] + u[5]*v[19] - u[6]*v[18] - u[7]*v[23] - u[8]*v[22] - u[9]*v[17], u[0]*v[17] + u[10]*v[3] - u[11]*v[4] + u[12]*v[5] + u[13]*v[6] + u[14]*v[7] + u[15]*v[8] - u[16]*v[9] + u[17]*v[0] + u[18]*v[25] - u[19]*v[26] + u[1]*v[2] + u[20]*v[27] + u[21]*v[28] + u[22]*v[29] + u[23]*v[30] - u[24]*v[31] - u[25]*v[18] - u[26]*v[19] - u[27]*v[20] + u[28]*v[21] - u[29]*v[22] - u[2]*v[1] + u[30]*v[23] + u[31]*v[24] + u[3]*v[10] + u[4]*v[11] + u[5]*v[12] - u[6]*v[13] + u[7]*v[14] - u[8]*v[15] - u[9]*v[16], u[0]*v[18] + u[10]*v[2] + u[11]*v[7] + u[12]*v[8] - u[13]*v[9] - u[14]*v[4] + u[15]*v[5] + u[16]*v[6] + u[17]*v[25] + u[18]*v[0] + u[19]*v[29] + u[1]*v[3] + u[20]*v[30] - u[21]*v[31] - u[22]*v[26] + u[23]*v[27] + u[24]*v[28] - u[25]*v[17] + u[26]*v[22] - u[27]*v[23] - u[28]*v[24] + u[29]*v[19] - u[2]*v[10] + u[30]*v[20] - u[31]*v[21] + u[3]*v[1] - u[4]*v[14] + u[5]*v[15] + u[6]*v[16] - u[7]*v[11] - u[8]*v[12] + u[9]*v[13], u[0]*v[19] + u[10]*v[7] + u[11]*v[2] - u[12]*v[9] + u[13]*v[8] - u[14]*v[3] - u[15]*v[6] - u[16]*v[5] + u[17]*v[26] + u[18]*v[29] + u[19]*v[0] + u[1]*v[4] - u[20]*v[31] + u[21]*v[30] - u[22]*v[25] - u[23]*v[28] - u[24]*v[27] - u[25]*v[22] + u[26]*v[17] + u[27]*v[24] + u[28]*v[23] + u[29]*v[18] - u[2]*v[11] - u[30]*v[21] + u[31]*v[20] + u[3]*v[14] - u[4]*v[1] - u[5]*v[16] - u[6]*v[15] - u[7]*v[10] + u[8]*v[13] - u[9]*v[12], u[0]*v[20] + u[10]*v[8] + u[11]*v[9] + u[12]*v[2] - u[13]*v[7] - u[14]*v[6] + u[15]*v[3] + u[16]*v[4] + u[17]*v[27] + u[18]*v[30] + u[19]*v[31] + u[1]*v[5] + u[20]*v[0] - u[21]*v[29] - u[22]*v[28] + u[23]*v[25] + u[24]*v[26] - u[25]*v[23] + u[26]*v[24] - u[27]*v[17] - u[28]*v[22] + u[29]*v[21] - u[2]*v[12] + u[30]*v[18] - u[31]*v[19] + u[3]*v[15] - u[4]*v[16] + u[5]*v[1] + u[6]*v[14] - u[7]*v[13] - u[8]*v[10] + u[9]*v[11], u[0]*v[21] + u[10]*v[9] + u[11]*v[8] - u[12]*v[7] + u[13]*v[2] - u[14]*v[5] - u[15]*v[4] - u[16]*v[3] + u[17]*v[28] + u[18]*v[31] + u[19]*v[30] + u[1]*v[6] - u[20]*v[29] + u[21]*v[0] - u[22]*v[27] - u[23]*v[26] - u[24]*v[25] - u[25]*v[24] + u[26]*v[23] + u[27]*v[22] + u[28]*v[17] + u[29]*v[20] - u[2]*v[13] - u[30]*v[19] + u[31]*v[18] + u[3]*v[16] - u[4]*v[15] - u[5]*v[14] - u[6]*v[1] - u[7]*v[12] + u[8]*v[11] - u[9]*v[10], u[0]*v[22] + u[10]*v[4] - u[11]*v[3] - u[12]*v[6] - u[13]*v[5] + u[14]*v[2] - u[15]*v[9] + u[16]*v[8] + u[17]*v[29] + u[18]*v[26] - u[19]*v[25] + u[1]*v[7] - u[20]*v[28] - u[21]*v[27] + u[22]*v[0] - u[23]*v[31] + u[24]*v[30] - u[25]*v[19] - u[26]*v[18] + u[27]*v[21] - u[28]*v[20] - u[29]*v[17] - u[2]*v[14] - u[30]*v[24] - u[31]*v[23] + u[3]*v[11] + u[4]*v[10] - u[5]*v[13] + u[6]*v[12] + u[7]*v[1] + u[8]*v[16] + u[9]*v[15], u[0]*v[23] + u[10]*v[5] - u[11]*v[6] + u[12]*v[3] + u[13]*v[4] + u[14]*v[9] + u[15]*v[2] - u[16]*v[7] + u[17]*v[30] + u[18]*v[27] - u[19]*v[28] + u[1]*v[8] + u[20]*v[25] + u[21]*v[26] + u[22]*v[31] + u[23]*v[0] - u[24]*v[29] - u[25]*v[20] - u[26]*v[21] - u[27]*v[18] + u[28]*v[19] - u[29]*v[24] - u[2]*v[15] + u[30]*v[17] + u[31]*v[22] + u[3]*v[12] + u[4]*v[13] + u[5]*v[10] - u[6]*v[11] + u[7]*v[16] - u[8]*v[1] - u[9]*v[14], u[0]*v[24] + u[10]*v[6] - u[11]*v[5] - u[12]*v[4] - u[13]*v[3] + u[14]*v[8] - u[15]*v[7] + u[16]*v[2] + u[17]*v[31] + u[18]*v[28] - u[19]*v[27] + u[1]*v[9] - u[20]*v[26] - u[21]*v[25] + u[22]*v[30] - u[23]*v[29] + u[24]*v[0] - u[25]*v[21] - u[26]*v[20] + u[27]*v[19] - u[28]*v[18] - u[29]*v[23] - u[2]*v[16] - u[30]*v[22] - u[31]*v[17] + u[3]*v[13] + u[4]*v[12] - u[5]*v[11] + u[6]*v[10] + u[7]*v[15] + u[8]*v[14] + u[9]*v[1], u[0]*v[25] - u[10]*v[1] + u[11]*v[14] - u[12]*v[15] - u[13]*v[16] + u[14]*v[11] + u[15]*v[12] - u[16]*v[13] + u[17]*v[18] - u[18]*v[17] + u[19]*v[22] + u[1]*v[10] - u[20]*v[23] - u[21]*v[24] + u[22]*v[19] + u[23]*v[20] - u[24]*v[21] + u[25]*v[0] + u[26]*v[29] + u[27]*v[30] - u[28]*v[31] - u[29]*v[26] - u[2]*v[3] + u[30]*v[27] + u[31]*v[28] - u[3]*v[2] - u[4]*v[7] - u[5]*v[8] + u[6]*v[9] + u[7]*v[4] - u[8]*v[5] - u[9]*v[6], u[0]*v[26] - u[10]*v[14] + u[11]*v[1] + u[12]*v[16] + u[13]*v[15] + u[14]*v[10] - u[15]*v[13] + u[16]*v[12] + u[17]*v[19] - u[18]*v[22] + u[19]*v[17] + u[1]*v[11] + u[20]*v[24] + u[21]*v[23] + u[22]*v[18] - u[23]*v[21] + u[24]*v[20] + u[25]*v[29] + u[26]*v[0] - u[27]*v[31] + u[28]*v[30] - u[29]*v[25] - u[2]*v[4] - u[30]*v[28] - u[31]*v[27] - u[3]*v[7] - u[4]*v[2] + u[5]*v[9] - u[6]*v[8] + u[7]*v[3] + u[8]*v[6] + u[9]*v[5], u[0]*v[27] - u[10]*v[15] + u[11]*v[16] - u[12]*v[1] - u[13]*v[14] + u[14]*v[13] + u[15]*v[10] - u[16]*v[11] + u[17]*v[20] - u[18]*v[23] + u[19]*v[24] + u[1]*v[12] - u[20]*v[17] - u[21]*v[22] + u[22]*v[21] + u[23]*v[18] - u[24]*v[19] + u[25]*v[30] + u[26]*v[31] + u[27]*v[0] - u[28]*v[29] - u[29]*v[28] - u[2]*v[5] + u[30]*v[25] + u[31]*v[26] - u[3]*v[8] - u[4]*v[9] - u[5]*v[2] + u[6]*v[7] + u[7]*v[6] - u[8]*v[3] - u[9]*v[4], u[0]*v[28] - u[10]*v[16] + u[11]*v[15] + u[12]*v[14] + u[13]*v[1] + u[14]*v[12] - u[15]*v[11] + u[16]*v[10] + u[17]*v[21] - u[18]*v[24] + u[19]*v[23] + u[1]*v[13] + u[20]*v[22] + u[21]*v[17] + u[22]*v[20] - u[23]*v[19] + u[24]*v[18] + u[25]*v[31] + u[26]*v[30] - u[27]*v[29] + u[28]*v[0] - u[29]*v[27] - u[2]*v[6] - u[30]*v[26] - u[31]*v[25] - u[3]*v[9] - u[4]*v[8] + u[5]*v[7] - u[6]*v[2] + u[7]*v[5] + u[8]*v[4] + u[9]*v[3], u[0]*v[29] - u[10]*v[11] - u[11]*v[10] + u[12]*v[13] - u[13]*v[12] - u[14]*v[1] - u[15]*v[16] - u[16]*v[15] + u[17]*v[22] - u[18]*v[19] - u[19]*v[18] + u[1]*v[14] + u[20]*v[21] - u[21]*v[20] - u[22]*v[17] - u[23]*v[24] - u[24]*v[23] + u[25]*v[26] - u[26]*v[25] - u[27]*v[28] - u[28]*v[27] + u[29]*v[0] - u[2]*v[7] - u[30]*v[31] + u[31]*v[30] - u[3]*v[4] + u[4]*v[3] + u[5]*v[6] + u[6]*v[5] - u[7]*v[2] + u[8]*v[9] - u[9]*v[8], u[0]*v[30] - u[10]*v[12] - u[11]*v[13] - u[12]*v[10] + u[13]*v[11] - u[14]*v[16] + u[15]*v[1] + u[16]*v[14] + u[17]*v[23] - u[18]*v[20] - u[19]*v[21] + u[1]*v[15] - u[20]*v[18] + u[21]*v[19] - u[22]*v[24] + u[23]*v[17] + u[24]*v[22] + u[25]*v[27] - u[26]*v[28] + u[27]*v[25] + u[28]*v[26] + u[29]*v[31] - u[2]*v[8] + u[30]*v[0] - u[31]*v[29] - u[3]*v[5] + u[4]*v[6] - u[5]*v[3] - u[6]*v[4] - u[7]*v[9] - u[8]*v[2] + u[9]*v[7], u[0]*v[31] - u[10]*v[13] - u[11]*v[12] + u[12]*v[11] - u[13]*v[10] - u[14]*v[15] - u[15]*v[14] - u[16]*v[1] + u[17]*v[24] - u[18]*v[21] - u[19]*v[20] + u[1]*v[16] + u[20]*v[19] - u[21]*v[18] - u[22]*v[23] - u[23]*v[22] - u[24]*v[17] + u[25]*v[28] - u[26]*v[27] - u[27]*v[26] - u[28]*v[25] + u[29]*v[30] - u[2]*v[9] - u[30]*v[29] + u[31]*v[0] - u[3]*v[6] + u[4]*v[5] + u[5]*v[4] + u[6]*v[3] - u[7]*v[8] + u[8]*v[7] - u[9]*v[2]);
}


float pNormSq(float u[N], float p) {
    float normSq = 0;
    for(int i=0; i<N; i++){
        normSq = normSq + pow(abs(u[i]),p);
    }
    return normSq;
}

float pNorm(float u[N], float p) {
    return pow(pNormSq(u,p),1.0/p);
}

float norm(float u[N]) {
    return pNorm(u,NormPower);
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
    u[0] = JuliaVect1; u[1] = JuliaVect2; u[2] = JuliaVect3; u[3] = JuliaVect4; u[4] = JuliaVect5; u[5] = JuliaVect6; u[6] = JuliaVect7; u[7] = JuliaVect8; u[8] = JuliaVect9; u[9] = JuliaVect10; u[10] = JuliaVect11; u[11] = JuliaVect12; u[12] = JuliaVect13; u[13] = JuliaVect14; u[14] = JuliaVect15; u[15] = JuliaVect16; u[16] = JuliaVect17; u[17] = JuliaVect18; u[18] = JuliaVect19; u[19] = JuliaVect20; u[20] = JuliaVect21; u[21] = JuliaVect22; u[22] = JuliaVect23; u[23] = JuliaVect24; u[24] = JuliaVect25; u[25] = JuliaVect26; u[26] = JuliaVect27; u[27] = JuliaVect28; u[28] = JuliaVect29; u[29] = JuliaVect30; u[30] = JuliaVect31; u[31] = JuliaVect32; 
    return u;
}


float[N] loadParamsPosition(out float u[N]){
    u[0] = Position1; u[1] = Position2; u[2] = Position3; u[3] = Position4; u[4] = Position5; u[5] = Position6; u[6] = Position7; u[7] = Position8; u[8] = Position9; u[9] = Position10; u[10] = Position11; u[11] = Position12; u[12] = Position13; u[13] = Position14; u[14] = Position15; u[15] = Position16; u[16] = Position17; u[17] = Position18; u[18] = Position19; u[19] = Position20; u[20] = Position21; u[21] = Position22; u[22] = Position23; u[23] = Position24; u[24] = Position25; u[25] = Position26; u[26] = Position27; u[27] = Position28; u[28] = Position29; u[29] = Position30; u[30] = Position31; u[31] = Position32; 
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

void iter(inout float z[N]) {
    
    z = mul(
        pwr(flipA(z),pow1),
        pwr(flipB(z),pow2)
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
	return ((r < Bailout && r > Bailin) || BailInvert);
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
