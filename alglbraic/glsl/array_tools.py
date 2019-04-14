from string import Template
from sympy.tensor import IndexedBase
from alglbraic.glsl import meta_glsl


class BuildFromArray(object):
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
    def export_to_array(self, name="toArray", separator=", "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
$base_type[$size] $fn_name($type_name x){
    return $base_type[$size]($array_members);
}"""
        )

        array_members = separator.join(str(x) for x in self.symbols_vector_for('x'))

        return template.substitute(
            fn_name=name,
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            array_members=array_members,
            size=len(self),
        )


from .struct import GlslBundler

def struct_injections(struct, size, inject_fn_name="inject"):
    class Injections(GlslBundler):
        @meta_glsl(depends_on=[struct.build_from_array])
        def into_array_from_subarray_at_indices(self):
            from sympy.tensor import IndexedBase

            template = Template(
                """\
/* Inject coordinates i_v of array v into coordinates i_u of array u */
float[$base_size] $fn_name(inout $base_type u[$base_size], int i_u[$size], $base_type v[$size], int i_v[$size]){
    $injection
    return u;
}"""
            )

            sep = ";\n    "

            u = IndexedBase("u")
            v = IndexedBase("v")

            i_u = IndexedBase("i_u")
            i_v = IndexedBase("i_v")

            injection = (
                sep.join("%s = %s" % (u[i_u[i]], v[i_v[i]]) for i in range(size)) + ";"
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                size=size,
                base_size=len(struct),
                injection=injection,
            )

        @meta_glsl(depends_on=[into_array_from_subarray_at_indices])
        def into_array_from_subarray(self):
            from sympy.tensor import IndexedBase

            template = Template(
                """\
/* Inject array v into coordinates i_u of array u */
$base_type float[$base_size] $fn_name(inout $base_type u[$size], int i_u[$size], $base_type v[$base_size]){
    $fn_name(u, i_u, v);
    return u;
}"""
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                size=size,
                base_size=len(struct),
            )

        @meta_glsl(depends_on=["build_from_array", into_array_from_subarray])
        def into_struct_from_subarray_at_indices(self):
            template = Template(
                """\
/* Inject coordinates i_v of array v into coordinates i_u of struct u */
$type_name $fn_name(inout $base_type u[$size], int i_u[$size], $base_type v[$base_size], int i_v[$size]){
    return fromArray(inject(u, i_u, v, i_v));
}"""
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                size=size,
                base_size=len(struct),
            )

        @meta_glsl(depends_on=[into_struct_from_subarray_at_indices])
        def into_struct_from_subarray(self):
            template = Template(
                """\
/* Inject coordinates i_v of array v into coordinates i_u of struct u */
$type_name $fn_name(inout $base_type u[$size], int i_u[$size], $base_type v[$base_size]){
    return inject(u, i_u, v));
}"""
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                size=size,
                base_size=len(struct),
            )

    return Injections