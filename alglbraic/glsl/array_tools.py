from string import Template
from sympy.tensor import IndexedBase
from alglbraic.glsl import GLSL


class BuildFromArray(object):
    @GLSL(depends_on=["definition"])
    def zero_array(self, name="zero", separator=";\n    "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
void $fn_name(inout $base_type X[$size]){
    $assignments;
}"""
        )

        x = IndexedBase("X")

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

    @GLSL(depends_on=["definition"])
    def build_from_array(self, name="fromArray", separator=", "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
$type_name $fn_name($base_type X[$size]){
    return $type_name($array_members);
}"""
        )

        x = IndexedBase("X")
        array_members = separator.join([str(x[i]) for i in range(len(self))])
        return template.substitute(
            fn_name=name,
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            array_members=array_members,
            size=len(self),
        )


    @GLSL(depends_on=["definition"])
    def export_to_array(self, name="toArray", separator=";\n    "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
void $fn_name($type_name X, inout $base_type X_ary[$size]){
    $assignments;
}"""
        )

        assignments = separator.join(
            ("X_ary[%i] = %s" % (i, x))
            for (i, x) in enumerate(self.symbols_vector_for("X"))
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
        @GLSL
        def into_array_from_subarray(self, separator=";\n    "):
            from sympy.tensor import IndexedBase

            template = Template(
                """\
/* Inject array V at the indices for $member_names in array U */
void ${fn_name}Array(inout $base_type U[$struct_size], $base_type V[$injection_size]){
    $injection
}"""
            )

            u = IndexedBase("U")
            v = IndexedBase("V")
            i_u = IndexedBase("i_U")

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

        @GLSL
        def into_struct_from_subarray(self):
            template = Template(
                """\
/* Inject array V into $member_names of struct U */
$type_name $fn_name($type_name U, $base_type V[$injection_size]){
    $base_type U_ary[$struct_size];
    toArray(U, U_ary);
    ${fn_name}Array(U_ary, V);
    return fromArray(U_ary);
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

        @GLSL
        def into_struct_from_float_subarray(self):
            template = Template(
                """\
/* Inject array V into $member_names of struct U */
$type_name $fn_name($type_name U, float V[$injection_size]){
    $base_type U_ary[$struct_size];
    toArray(U, U_ary);
    ${fn_name}Array(U_ary, V);
    return fromArray(U_ary);
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
