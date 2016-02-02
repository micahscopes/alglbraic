from pkg_resources import resource_string
from string import Template

squash = lambda L: reduce(lambda x,y: x+y,
        map(lambda k: squash(k) if isinstance(k,(list,tuple)) else [k], L), [])

class Fragment:
    def __init__(self,head=None,body=None,feet=None):
        self._head = head
        self._body = body
        self._feet = feet

    def head(self):
        return self._head
    def body(self):
        return self._body
    def feet(self):
        return self._feet
    def parts(self):
        parts = [self.head(),self.body(),self.feet()]
        return parts;
    def gl(self):
        parts =  [p for p in squash(self.parts()) if p is not None]
        return "\n".join(parts)

    def __add__(self,other):
        """Compose this fragment with another one"""
        h,b,f = zip(self.parts(),other.parts())
        return Fragment(h,b,f)

    @classmethod
    def get(self,name):
        """Get a glsl snippet or template from the fragments/ directory"""
        return resource_string(__name__,name)
