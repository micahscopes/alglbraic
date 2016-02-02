from pkg_resources import resource_string
from string import Template

class Fragment:
    def __init__(self,head,body,feet):
        self._head = head
        self._body = body
        self._feet = feet

    def head(self):
        return self._head
    def body(self):
        return self._body
    def feet(self):
        return self._feet

    def embodiment(self):
        return "\n".join([self.head(),self.body(),self.feet()])

    @classmethod
    def get(self,name):
        return resource_string(__name__,'fragments/'+name)
