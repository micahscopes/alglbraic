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


def struct_injections(struct, members, inject_fn_name="inject", separator=";\n    "):
    class Injections(GlslBundler):
        @meta_glsl()
        def into_array_from_subarray(self, separator=";\n    "):
            from sympy.tensor import IndexedBase

            template = Template(
                """\
/* Inject array v at the indices for $member_names in array u */
void ${fn_name}Array(inout $base_type u[$struct_size], $base_type v[$injection_size]){
    $injection
}"""
            )

            u = IndexedBase("u")
            v = IndexedBase("v")
            i_u = IndexedBase("i_u")

            injection = (
                separator.join(
                    "%s = %s" % (u[struct.member_index_const(member)], v[i])
                    for (i, member) in enumerate(members)
                )
                + ";"
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                injection_size=len(members),
                struct_size=len(struct),
                injection=injection,
                member_names=', '.join(members)
            )

        @meta_glsl()
        def into_struct_from_subarray(self):
            template = Template(
                """\
/* Inject array v into $member_names of struct u */
$type_name $fn_name($type_name u, $base_type v[$injection_size]){
    $base_type u_ary[$struct_size];
    toArray(u, u_ary);
    ${fn_name}Array(u_ary, v);
    return fromArray(u_ary);
}"""
            )

            return template.substitute(
                fn_name=inject_fn_name,
                type_name=struct.type_name,
                base_type=struct.uniform_member_type,
                injection_size=len(members),
                struct_size=len(struct),
                member_names=', '.join(members)
            )

        @staticmethod
        def glsl_snippets():
            return [
                # Injections.into_array_from_subarray_at_indices,
                Injections.into_array_from_subarray,
                # Injections.into_struct_from_subarray_at_indices,
                Injections.into_struct_from_subarray,
            ]

        @staticmethod
        def bundle():
            return "\n\n".join(s() for s in Injections.glsl_snippets())

    return Injections
