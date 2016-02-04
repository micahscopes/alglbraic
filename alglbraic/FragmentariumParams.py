from fragments import *

class FragmentariumParams(Fragment):
    """This is a hack attack way of generating a bunch Fragmentarium uniforms
    to control glsl arrays (e.g. a 16 dimensional float array)."""
    def __init__(self,var_name,size,var_type="float",size_const=None,rng="[-2,0,2]",declare_size=False):
        Fragment.__init__(self)
        self._upper = ""
        self._lower = ""
        if not isinstance(size_const,str):
            declare_size = True
            size_const="N_"+var_name.upper()
        if declare_size:
            t = Template('const int $N = $size;\n')
            d = t.substitute(N=size_const,size=size)
            self._upper += d
        load = ''
        for i in range(size):
            varN=var_name+str(i+1)
            t = Template("uniform $var_type $var; slider$rng\n")
            self._upper += t.substitute(var_type=var_type,var=varN,N=size_const,rng=str(rng))
            load += Template("u[$i] = $var; ").substitute(var=varN,i=str(i))
        t = Template("""
$var_type[$N] loadParams$var(out $var_type u[$N]){
    $loaders
    return u;
}
""")
        self._lower = t.substitute(var=var_name,loaders=load,var_type=var_type,N=size_const)