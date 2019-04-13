from functools import update_wrapper
import inspect


def get_arguments(fn):
    return [
        x
        for i, x in inspect.signature(fn).parameters.items()
        if x.kind == x.POSITIONAL_OR_KEYWORD
        and x.default == inspect._empty
        and x.name != "self"
    ]


class MetaString(str):
    def __new__(cls, *args, _prefix="Meta", **kwargs):
        if len(args) > 0:
            return str.__new__(cls, *args, **kwargs)
        else:
            MetaStringClass = type(_prefix + cls.__name__, (cls,), kwargs)
            return MetaStringClass


class Callable(object):
    def __init__(self, func):
        self.__func__ = func
        update_wrapper(self, func)

    def __repr__(self):
        return self.__func__.__repr__()

    def __call__(self, *args, **kwargs):
        return self.__func__(*args, **kwargs)

    def __get__(self, instance, owner):
        from functools import partial

        bound = partial(self.__func__, instance)
        bound = update_wrapper(bound, self)
        setattr(bound, 'meta_glsl', self.meta_glsl)
        return bound
