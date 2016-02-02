float[N] loadPositions(float u[N]){
    for(int i = 0; i<N; i++) {
        u[i] = getPosition(i);
    }
    return u;
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

Vect permutate(Vect A,bool conj) {
    Vect permutated = Vect0();
    for(int i = 0; i < N; i++) {
        if(!conj) {
            permutated = set(permutated,i,get(A,P[i]));
        } else {
            permutated = set(permutated,P[i],get(A,i));
        }
    }
    return permutated;
}

bool inside(vec3 pt) {
    P = permutation(Permutation);
    float z[N] = addFrame(O,pt);
    float z0[N] = z;
  	float r;
  	int i=0;
  	r=abs(norm(z));

    while(r<Bailout && (i<Iterations)) {
      Vect zprev;
      if (usePrevious) { zprev = z; } else { zprev = z0; }
  		z = iter(z);
  		z = add(z,(Julia ? JuliaVect : zprev));
  		r=norm(z);
  		i++;
  	}
	return (r<Bailout);
}
