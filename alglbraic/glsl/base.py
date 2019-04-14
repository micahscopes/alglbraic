from inspect import getmembers, signature
from alglbraic.util import get_arguments, MetaString
from typing import List, Union
from types import FunctionType
import inspect

class GlslBaseType(object):
    pass


class GLSL(MetaString):
    depends_on: list = []
    glsl_type = GlslBaseType
    pass


class GlslBundler(GlslBaseType):
    
    def glsl_methods(self):
        members = getmembers(self)
        glsl_methods = [
            getattr(self, name) for name, func in members if is_glsl_method(func)
        ]

        return list(sort_glsl_dependencies(glsl_methods))

    def glsl_helpers(self):
        return list(func for func in self.glsl_methods() if is_glsl_helper(func))

    def glsl_snippets(self):
        return list(func for func in self.glsl_methods() if is_glsl_snippet(func))

    @staticmethod
    def compile(*snippet_lists):
        snippets = sort_glsl_dependencies(sum((list(l) for l in snippet_lists), []))
        return "\n\n".join(s() for s in snippets)

    def bundle(self):
        return self.compile(self.glsl_snippets())


def meta_glsl(*args, **kwargs):
    from alglbraic.util import Callable

    def meta_glsl_decorator(func):
        sig = inspect.signature(func)
        MetaGLSL_type = GLSL(*args, **kwargs)
        MetaGLSL_type.special = False

        if issubclass(sig.return_annotation, GLSL):
            MetaGLSL_type = sig.return_annotation(*args, special=True, **kwargs)

        def wrapper(*gl_args, **gl_kwargs) -> MetaGLSL_type:
            return MetaGLSL_type(func(*gl_args, **gl_kwargs))

        class MetaCallable(Callable):
            def __init__(self, *args, **kwargs):
                self.meta_glsl = MetaGLSL_type
                super().__init__(*args, **kwargs)

            def __set_name__(self, cls, name):
                MetaGLSL_type.glsl_type = cls

        wrapper = MetaCallable(wrapper)
        wrapper.__signature__ = sig.replace(return_annotation=MetaGLSL_type)
        wrapper.__name__ = func.__name__

        return wrapper

    return meta_glsl_decorator


def get_meta_glsl(func):
    try:
        meta_glsl = signature(func).return_annotation
        if issubclass(meta_glsl, GLSL):
            return meta_glsl
    except (TypeError, ValueError):
        return None


def is_glsl_method(func):
    return get_meta_glsl(func) is not None


def is_glsl_helper(func):
    return is_glsl_method(func) and len(get_arguments(func)) > 1


def is_glsl_snippet(func):
    return is_glsl_method(func) and len(get_arguments(func)) == 0


def sort_glsl_dependencies(glsl_nodes: List[Union[str, FunctionType]]):
    """
        Parameters
        ----------
        glsl_nodes :
            A set of functions, each of which has a `GLSL` return type containing
            a `depends_on` attribute defining its dependencies.
    """
    from toposort import toposort

    def get_deps(node):
        try:
            return get_meta_glsl(node).depends_on + [get_meta_glsl(node).glsl_type]
        except AttributeError:
            return node.mro()

    def key(node):
        try:
            return str(len(node.mro()))
        except AttributeError:
            return (
                str(len(get_meta_glsl(node).glsl_type.mro()))
                + "."
                + str.lower(node.__name__)
            )

    glsl_types = set(sum([get_meta_glsl(n).glsl_type.mro() for n in glsl_nodes], []))

    def fn_name(str_or_fn) -> str:
        try:
            return str_or_fn.__name__
        except AttributeError:
            return str_or_fn

    nodes = list(glsl_types) + glsl_nodes

    fn_lookup = {fn_name(node): node for node in nodes}

    graph = {node: set(fn_lookup[fn_name(d)] for d in get_deps(node)) for node in nodes}

    graph_toposorted = toposort(graph)
    graph_sorted = (
        sorted((n for n in layer if type(n) is not type), key=key)
        for layer in graph_toposorted
    )
    graph_sorted_flattened = sum(graph_sorted, [])

    return graph_sorted_flattened
