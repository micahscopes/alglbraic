from fragments import *
from GLSLPrinter import *
from sympy import Symbol, symbols, sympify

# Usage:
# Pass in an operation in terms of float u[N] and float v[N].
#

class VectorOperation(Fragment):
    def __init__(self, name, vectors, results, symbols=['u','v','w','x','y','z','a','b','c']):
        Fragment.__init__(self)
        s = sympify
        # HOLD ON TO YOUR HORSE VERY TIGHT
        self.operation = name
        self.vectors = [s(v) for v in vectors]
        self.results = squash([s(results)])
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
        if len(results)>1:
            result = "float[N](%s)" % ", ".join(results)
        else:
            result = results[0]
        return self._functionTemplate.substitute(func=name,rtype=rtype,args=args,result=result)

    def lower(self):
        return self.compile(self.operation,self.vectors,self.results,self.symbols)
