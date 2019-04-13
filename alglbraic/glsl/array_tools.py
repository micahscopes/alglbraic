from string import Template
from sympy.tensor import IndexedBase
from alglbraic.glsl import meta_glsl

class Mixin(object):
    @meta_glsl(depends_on=['definition'])
    def build_from_array(self, separator=", "):
        if not self.uniform_member_type:
            raise TypeError(
                "To generate an array constructor, GlslStruct must have members of\
                uniform type"
            )

        template = Template(
            """\
$type_name fromArray($base_type x[$size]){
    return $type_name($array_members);
}"""
        )

        x = IndexedBase("x")
        array_members = separator.join([str(x[i]) for i in range(len(self))])
        return template.substitute(
            type_name=self.type_name,
            base_type=self.uniform_member_type,
            array_members=array_members,
            size=len(self),
        )

