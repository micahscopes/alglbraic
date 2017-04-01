from fragments import *
from GLSLPrinter import *
from sympy import Symbol, symbols, sympify

# Usage:
# Pass in an operation in terms of float u[N] and float v[N].
#

class VectorOperation(Fragment):
    def __init__(self, name, vectors, results, symbols=['u','v','w','x','y','z','a','b','c'], result_size_const = "N", input_size_consts = None, functionTemplate=None):
        Fragment.__init__(self)
        self.N = result_size_const
        self.N_inputs = input_size_consts if input_size_consts else [result_size_const]*len(vectors)
        s = sympify
        # HOLD ON TO YOUR HORSE VERY TIGHT
        self.operation = name
        self.vectors = [s(v) for v in vectors]
        self.results = squash([s(results)])
        self.symbols = symbols
        self._functionTemplate = functionTemplate if functionTemplate else Template("""
$rtype $func($args) {
    return $result;
}
""")

    def compile(self,name,vectors,results,symbols):
        rtype = "float[%s]" % self.N if len(results)>1 else "float"
        symbols = map(lambda i: symbols[i]+"[%s]",range(len(vectors)))
        #print(symbols)
        args = ", ".join(map(lambda (i,s): "float "+s % self.N_inputs[i],enumerate(symbols)))

        symbols = zip(vectors,symbols)
        component = lambda i, symbol: Symbol(symbol % i)
        subs = []
        for s in symbols:
            subs += zip(s[0],[component(i,s[1]) for i in range(len(s[0]))])
        #print subs
        subs = dict(subs)
        results = map(lambda c: self.makeGL(c.subs(subs)), results)
        if len(results)>1:
            result = "float[%s](%s)" % (self.N, ", ".join(results))
        else:
            result = results[0]
        return self._functionTemplate.substitute(func=name,rtype=rtype,args=args,result=result)

    def lower(self):
        return self.compile(self.operation,self.vectors,self.results,self.symbols)
