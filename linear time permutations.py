from math import factorial

def ithPerm(n,elems):#with n from 0
    if(len(elems) == 1):
        return elems[0]
    sizeGroup = factorial(len(elems)-1)
    q,r = divmod(n,sizeGroup)
    v = elems[q]
    elems.remove(v)
    return v + ", " + ithPerm(r,elems)


function nth_permutation($atoms, $index, $size) {
    for ($i = 0; $i < $size; $i++) {
        $item = $index % count($atoms);
        $index = floor($index / count($atoms));
        $result[] = $atoms[$item];
        array_splice($atoms, $item, 1);
    }
    return $result;
}

from math import floor
def nthPermutation(n,N):
    result = range(N)
    working = range(N)
    for i in range(N):
        item = int(n % (N - i))
        n = floor(n / (N - i))
        result[i] = working[item]
        j = 0
        found = False
        while j < N - i - 1:
            if working[j] == result[i]:
                found = True
            if found:
                working[j] = working[j+1]
            j+=1
    return result


int[N] nth_permutation(int n, int N) {
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
