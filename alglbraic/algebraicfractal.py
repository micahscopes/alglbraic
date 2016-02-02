from pkg_resources import resource_string
from string import Template

class Fragment:
    def head(self):
        return ""
    def body(self):
        return ""
    def feet(self):
        return ""

    @classmethod
    def get(self,name):
        return resource_string(__name__,'fragments/'+name)
