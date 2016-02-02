from .fragments import Fragments

class VectorSpaceGL(Fragments):
    def __init__(self, dims):
        self.dims = dims

    def head():
        return "const int N = "+str(dims)
