const int N = $dim
$header

float[N] mul(float a[N], float b[N]) {
  return product(a,b);
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

$implementation

$presets
