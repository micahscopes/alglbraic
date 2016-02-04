from pkg_resources import resource_string
from string import Template
from ..GLSLPrinter import *

squash = lambda L: reduce(lambda x,y: list(x)+list(y),
        map(lambda k: squash(k) if isinstance(k,(list,tuple,set)) else [k], L), [])
def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

class Fragment:
    def __init__(self,upper=None,lower=None,bottom=None,top=None):
        self._top = top
        self._upper = upper
        self._lower = lower
        self._bottom = bottom
        self._printer = None

    def glPrinter(self):
        printer = self._printer
        if(printer == None):
            printer = GLSLPrinter()
        return printer

    def makeGL(self,*args,**kwargs):
        return self.glPrinter().makeGL(*args,**kwargs)
    def setPrinter(self,printer):
        self._printer = printer
    def top(self):
        return self._top
    def upper(self):
        return self._upper
    def lower(self):
        return self._lower
    def bottom(self):
        return self._bottom
    def parts(self):
        parts = [self.top(),self.upper(),self.lower(),self.bottom()]
        return parts;

    def gl(self,printer=None):
        self.setPrinter(printer)
        parts = [p for p in squash(self.parts()) if p is not None]
        return "\n".join(parts)

    def __add__(self,other):
        """Compose this fragment with another one"""
        return Composition(self,other,included=False)

    @classmethod
    def get(self,name):
        """Get a glsl snippet or template from the fragments/ directory"""
        return resource_string(__name__,name)

class Composition(Fragment):
    def __init__(self,left=None,right=None,unique=True,included=True,last=True):
        Fragment.__init__(self)
        self.unique = unique
        self.included = included
        self.last = last #include the self's parts last
        # if isinstance(left, Composition): left = left.members()
        # if isinstance(right, Composition): right = right.members()
        self._members = squash([left]+[right])
        self._members = [m for m in self._members if m is not None]

    def members(self):
        members = self._members
        # if (self.included): members += [self]
        if (self.unique): members = uniq(members)
        return members

    def setPrinter(self,printer):
        for m in self.members():
            m.setPrinter(printer)

    def parts(self):
        parts = [self.top(),self.upper(),self.lower(),self.bottom()]
        parts = zip(self.memberParts(),parts)
        #parts = [p for p in squash(parts) if p is not None]
        return parts;

    def memberParts(self):
        parts = reduce(zip,[m.parts() for m in self.members() if m != self])
        return parts
    #
    # def gl(self,printer=None):
    #     parts = [p for p in squash(self.parts()) if p is not None]
    #     return "\n".join(self.parts())
