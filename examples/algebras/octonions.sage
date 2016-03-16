k_standard=QQ
#We denote the generators of an octonion by i, j, k and use the following basis:
gen_oct=['','i','j','ij','k','ik','jk','(ij)k']

#the class octonion_parent is the  class of octonion algebras over the field K such that i^2=a, j^2=b and k^2=c.
class octonion_parent():
    def __init__(self,K=k_standard,a=-1,b=-1,c=-1):
        if is_field(K):
            self.K=K
        else:
            raise TypeError("K should be a field")
        if a in K and b in K and c in K:
                self.a=a
                self.b=b
                self.c=c
        else:
            raise TypeError("a,b,c should be elements of K")

    def __repr__(self):
        return "Octonion algebra over field K with parameters %s %s %s" %(self.a, self.b, self.c)

    def __eq__(self, y):
        return (self.a==y.a and self.b==y.b and self.c==y.c)

    def one(self):
        return octonion([1,0,0,0,0,0,0,0],self)

    def zero(self):
        return octonion([0,0,0,0,0,0,0,0],self)

    #generates a random element of the octonion with coefficients in Q
    def random(self):
        return octonion( [QQ.random_element() for i in [0..7]],self)
    #generates a random skew element of the octonion with coefficients in Q
    def random_skew(self):
    	ret=[0]
        ret.extend([QQ.random_element() for i in [0..6]])
        return octonion(ret,self)

    #elements of octonion can be constructed by calling self with an element of the field or with a list of 8 elements
    def __call__(self,L):
        if L in self.K:
            return octonion([L,0,0,0,0,0,0,0],self)
        elif len(L)==8:
            return octonion(L,self)
        else:
           raise TypeError("input should either be in K or a list of 8 elements")

#the class of elements of an octonion algebra, input is an instance of octonion_parent and a list of 8 elements in K
class octonion():
    def __init__(self,L,parent):
        self.L=L
        self.par=parent

    #addition and substraction
    def __add__(self,y):
        if self.par==y.par:
           return octonion([self.L[i]+y.L[i] for i in [0..7]],self.par)
        raise TypeError("In __add__ in octonion: Elements should be in the same algebra.")
    def __sub__(self,y):
        if self.par==y.par:
            return octonion([self.L[i]-y.L[i] for i in [0..7]],self.par)
        raise TypeError("In __sub__ in octonion: Elements should be in the same algebra.")

    def __neg__(self):
           return octonion([-self.L[i] for i in [0..7]],self.par)

    #multiplication as defined in section 1.3
    def __mul__(self,y):
       if y in self.par.K:
           return octonion([(y*self.L[i]) for i in [0..7]],self.par)
       if self.par==y.par:
           return octonion([(self.par.a)*(self.par.b)*(self.par.c)*(self.L[7])*(y.L[7]) - (self.par.a)*(self.par.b)*(self.L[3])*(y.L[3]) - (self.par.a)*(self.par.c)*(self.L[5])*(y.L[5]) - (self.par.b)*(self.par.c)*(self.L[6])*(y.L[6]) + (self.par.a)*(self.L[1])*(y.L[1]) + (self.par.b)*(self.L[2])*(y.L[2]) +
(self.par.c)*(self.L[4])*(y.L[4]) + (self.L[0])*(y.L[0]), (self.par.b)*(self.par.c)*(self.L[7])*(y.L[6]) - (self.par.b)*(self.par.c)*(self.L[6])*(y.L[7]) + (self.par.b)*(self.L[3])*(y.L[2]) - (self.par.b)*(self.L[2])*(y.L[3]) + (self.par.c)*(self.L[5])*(y.L[4]) -
(self.par.c)*(self.L[4])*(y.L[5]) + (self.L[1])*(y.L[0]) + (self.L[0])*(y.L[1]), -(self.par.a)*(self.par.c)*(self.L[7])*(y.L[5]) + (self.par.a)*(self.par.c)*(self.L[5])*(y.L[7]) - (self.par.a)*(self.L[3])*(y.L[1]) + (self.par.a)*(self.L[1])*(y.L[3]) +
(self.par.c)*(self.L[6])*(y.L[4]) - (self.par.c)*(self.L[4])*(y.L[6]) + (self.L[2])*(y.L[0]) + (self.L[0])*(y.L[2]), (self.par.c)*(self.L[7])*(y.L[4]) - (self.par.c)*(self.L[6])*(y.L[5]) + (self.par.c)*(self.L[5])*(y.L[6]) - (self.par.c)*(self.L[4])*(y.L[7])
+ (self.L[3])*(y.L[0]) - (self.L[2])*(y.L[1]) + (self.L[1])*(y.L[2]) + (self.L[0])*(y.L[3]), (self.par.a)*(self.par.b)*(self.L[7])*(y.L[3]) - (self.par.a)*(self.par.b)*(self.L[3])*(y.L[7]) - (self.par.a)*(self.L[5])*(y.L[1]) -
(self.par.b)*(self.L[6])*(y.L[2]) + (self.par.a)*(self.L[1])*(y.L[5]) + (self.par.b)*(self.L[2])*(y.L[6]) + (self.L[4])*(y.L[0]) + (self.L[0])*(y.L[4]), -(self.par.b)*(self.L[7])*(y.L[2]) + (self.par.b)*(self.L[6])*(y.L[3]) -
(self.par.b)*(self.L[3])*(y.L[6]) + (self.par.b)*(self.L[2])*(y.L[7]) + (self.L[5])*(y.L[0]) - (self.L[4])*(y.L[1]) + (self.L[1])*(y.L[4]) + (self.L[0])*(y.L[5]), (self.par.a)*(self.L[7])*(y.L[1]) - (self.par.a)*(self.L[5])*(y.L[3]) +
(self.par.a)*(self.L[3])*(y.L[5]) - (self.par.a)*(self.L[1])*(y.L[7]) + (self.L[6])*(y.L[0]) - (self.L[4])*(y.L[2]) + (self.L[2])*(y.L[4]) + (self.L[0])*(y.L[6]), (self.L[7])*(y.L[0]) + (self.L[6])*(y.L[1]) - (self.L[5])*(y.L[2])
- (self.L[4])*(y.L[3]) + (self.L[3])*(y.L[4]) + (self.L[2])*(y.L[5]) - (self.L[1])*(y.L[6]) + (self.L[0])*(y.L[7])],self.par)
       raise TypeError("In __mul__ in octonion: Elements should be in the same algebra or one should be in K.")

    def __rmul__(self,y):
        return self*y

    #the standard involution
    def si(self):
        ret=[self.L[0]]
        ret.extend([-self.L[i] for i in [1..7]])
        return octonion(ret,self.par)

    #the norm of an octonion: norm(x)=x.si(x)
    def norm(self):
       return -(self.par.a)*(self.par.b)*(self.par.c)*(self.L[7])^2 + (self.par.a)*(self.par.b)*(self.L[3])^2 + (self.par.a)*(self.par.c)*(self.L[5])^2 + (self.par.b)*(self.par.c)*(self.L[6])^2 - (self.par.a)*(self.L[1])^2 - (self.par.b)*(self.L[2])^2 - (self.par.c)*(self.L[4])^2+ (self.L[0])^2

   #the inverse: x^{-1}=x^\si/N(x)
    def inv(self):
        return self.si()*(self.norm()^(-1))

    def __div__(self,y):
        if y in K:
           return octonion([((1/y)*self.L[i]) for i in [0..7]],self.par)
        if self.par==y.par:
           return self*y.inv()
        raise TypeError("In __div__ in octonion: Elements should be in the same algebra or one should be in K.")

    #power, should only be used to take small powers
    def __pow__(self,n):
        if n==0:
            return octonion([1,0,0,0,0,0,0,0],self.par)
        elif n>0:
            power=self
            k=1
            while(k<n):
                power=power*self
                k+=1
            return power
        else:
            return self.inv()^(-n)

    def __repr__(self):
        ret=""
        written=false
        for i in [0..7]:
            if self.L[i]!=0:
                if written:
                    ret+=' + '
                if self.L[i]==1 and i!=0:
                    ret+=gen_oct[i]
                else:
                    ret+='(%s) %s' %(self.L[i],gen_oct[i])
                written=true
        if not written:
            ret='0'
        return ret

    def __eq__(self,y):
        return (self.par==y.par and self.L==y.L)

    def __ne__(self,y):
        return (self.par!=y.par or self.L!=y.L)

    #if x=octonion([a0,...,a7],parent) , then x[0]=a0,...,x[7]=a7
    def __getitem__(self,i):
        return self.L[i]

    def __setitem__(self, i, value):
        self.L[i]=value
