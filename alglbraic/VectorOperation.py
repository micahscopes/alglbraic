from fragments import *
from GLSLPrinter import *
from sympy import Symbol, symbols

# Usage:
# Pass in an operation in terms of float u[N] and float v[N].
#

class VectorOperation(Fragment):
    def __init__(self, name, vectors, results, symbols=['u','v','w','x','y','z','a','b','c']):
        Fragment.__init__(self)
        # HOLD ON TO YOUR HORSE VERY TIGHT
        self.operation = name
        self.vectors = vectors
        self.results = squash([results])
        self.symbols = symbols
        self._functionTemplate = Template("""
$rtype $func($args) {
    return $result;
}
""")

    def compile(self,name,vectors,results,symbols):
        rtype = "float[N]" if len(results)>1 else "float"
        symbols = map(lambda i: symbols[i]+"[%s]",range(len(vectors)))
        #print(symbols)
        args = ", ".join(map(lambda s: "float "+s % "N",symbols))
        symbols = zip(vectors,symbols)
        component = lambda i, symbol: Symbol(symbol % i)
        subs = []
        for s in symbols:
            subs += zip(s[0],[component(i,s[1]) for i in range(len(s[0]))])
        #print subs
        subs = dict(subs)
        results = map(lambda c: self.makeGL(c.subs(subs)), results)
        result = "float[N](%s)" if len(results)>1 else "return %s"
        result = result % ", ".join(results)
        return self._functionTemplate.substitute(func=name,rtype=rtype,args=args,result=result)

    def body(self):
        return self.compile(self.operation,self.vectors,self.results,self.symbols)
