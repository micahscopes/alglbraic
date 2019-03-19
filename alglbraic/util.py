import inspect


def get_arguments(fn):
    return [
        x
        for i, x in inspect.signature(fn).parameters.items()
        if x.default == inspect._empty
    ]


class MetaString(str):
    def __new__(cls, *args, _prefix="Meta", **kwargs):
        if len(args) > 0:
            return str.__new__(cls, *args, **kwargs)
        else:
            MetaStringClass = type(_prefix + cls.__name__, (cls,), kwargs)
            return MetaStringClass
