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
    def __init__(self,head=None,body=None,feet=None):
        self._head = head
        self._body = body
        self._feet = feet
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

    def head(self):
        return self._head
    def body(self):
        return self._body
    def feet(self):
        f = self._feet
        return self._feet
    def parts(self):
        parts = [self.head(),self.body(),self.feet()]
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
        parts = [self.head(),self.body(),self.feet()]
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
