from string import Template
from sympy.tensor import IndexedBase
from alglbraic.glsl import meta_glsl


class BuildFromArray(object):
    @meta_glsl(depends_on=["definition"])
    def zero_array(self, name="zero", separator=";\n    "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
void $fn_name(inout $base_type x[$size]){
    $assignments;
}"""
        )

        x = IndexedBase("x")

        assignments = separator.join(
            "%s = %s" % (x[i], self.base_zero()) for i in range(len(self))
        )

        return template.substitute(
            fn_name=name,
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            size=len(self),
            assignments=assignments,
        )

    @meta_glsl(depends_on=["definition"])
    def build_from_array(self, name="fromArray", separator=", "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
$type_name $fn_name($base_type x[$size]){
    return $type_name($array_members);
}"""
        )

        x = IndexedBase("x")
        array_members = separator.join([str(x[i]) for i in range(len(self))])
        return template.substitute(
            fn_name=name,
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            array_members=array_members,
            size=len(self),
        )

    @meta_glsl(depends_on=["definition"])
    def export_to_array(self, name="toArray", separator=";\n    "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
void $fn_name($type_name x, inout $base_type x_ary[$size]){
    $assignments;
}"""
        )

        assignments = separator.join(
            ("x_ary[%i] = %s" % (i, x))
            for (i, x) in enumerate(self.symbols_vector_for("x"))
        )

        return template.substitute(
            fn_name=name,
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            assignments=assignments,
            size=len(self),
        )


from .struct import GlslBundler


def struct_injections(struct, size, inject_fn_name="inject", separator=";\n    "):
    class Injections(GlslBundler):
        @meta_glsl()
        def into_array_from_subarray_at_indices(self):
            from sympy.tensor import IndexedBase

            template = Template(
                """\
/* Inject coordinates i_v of array v into coordinates i_u of array u */
void ${fn_name}ArrayWithCoords(inout $base_type u[$struct_size], int i_u[$injection_size], $base_type v[$injection_size], int i_v[$injection_size]){
    $injection
}"""
            )

            u = IndexedBase("u")
            v = IndexedBase("v")
            i_u = IndexedBase("i_u")
            i_v = IndexedBase("i_v")

            injection = (
                separator.join("%s = %s" % (u[i_u[i]], v[i_v[i]]) for i in range(size)) + ";"
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                injection_size=size,
                struct_size=len(struct),
                injection=injection,
            )

        @meta_glsl()
        def into_array_from_subarray(self, separator=";\n    "):
            from sympy.tensor import IndexedBase

            template = Template(
                """\
/* Inject array v into coordinates i_u of array u */
void ${fn_name}Array(inout $base_type u[$struct_size], int i_u[$injection_size], $base_type v[$injection_size]){
    $injection
}"""
            )

            u = IndexedBase("u")
            v = IndexedBase("v")
            i_u = IndexedBase("i_u")

            injection = (
                separator.join("%s = %s" % (u[i_u[i]], v[i]) for i in range(size)) + ";"
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                injection_size=size,
                struct_size=len(struct),
                injection=injection,
            )

        @meta_glsl(depends_on=[struct.build_from_array, into_array_from_subarray])
        def into_struct_from_subarray_at_indices(self):
            template = Template(
                """\
/* Inject coordinates i_v of array v into coordinates i_u of struct u */
$type_name ${fn_name}($type_name u, int i_u[$injection_size], $base_type v[$injection_size], int i_v[$injection_size]){
    $base_type u_ary[$struct_size];
    toArray(u, u_ary);
    ${fn_name}ArrayWithCoords(u_ary, i_u, v, i_v);
    return fromArray(u_ary);
}"""
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                injection_size=size,
                struct_size=len(struct),
            )

        @meta_glsl(depends_on=[into_struct_from_subarray_at_indices])
        def into_struct_from_subarray(self):
            template = Template(
                """\
/* Inject array v into coordinates i_u of struct u */
$type_name $fn_name($type_name u, int i_u[$injection_size], $base_type v[$injection_size]){
    $base_type u_ary[$struct_size];
    toArray(u, u_ary);
    ${fn_name}Array(u_ary, i_u, v);
    return fromArray(u_ary);
}"""
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                injection_size=size,
                struct_size=len(struct),
            )

        @staticmethod
        def glsl_snippets():
            return [
                Injections.into_array_from_subarray_at_indices,
                Injections.into_array_from_subarray,
                Injections.into_struct_from_subarray_at_indices,
                Injections.into_struct_from_subarray,
            ]

        @staticmethod
        def bundle():
            return "\n\n".join(s() for s in Injections.glsl_snippets())

    return Injections
