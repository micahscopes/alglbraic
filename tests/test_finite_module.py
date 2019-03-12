import unittest
import snapshottest
from alglbraic.finite_module import FiniteModule
from sympy import glsl_code

from alglbraic.struct import GlslStruct

class TestFiniteModule(snapshottest.TestCase):

    def setUp(self):
        self.module = FiniteModule(
            'ComplexCl2', 'C',
            'ONE',
            'e1',
            'e2',
            'e12',
            unit='ONE'
        )

    def test_finite_module(self):
        module = self.module

        self.assert_match_snapshot(
            str(module.definition())
        )

        self.assert_match_snapshot(
            str(module.zero())
        )

        self.assert_match_snapshot(
            str(module.one())
        )

        self.assert_match_snapshot(
            str(module.add())
        )

        self.assert_match_snapshot(
            str(module.sub())
        )

        self.assert_match_snapshot(
            str(module.scalar_mul())
        )

    def test_algebraic_product(self):
        module = self.module
        from galgebra.ga import Ga
        from functools import reduce
        (Cl,_e1,_e2) = Ga.build('e1 e2', g=[1,1])

        u_co, v_co = module.argument_pair()
        u = Cl.mv(reduce(lambda u,v: u+v, [a*x for a,x in zip(u_co, Cl.blades_lst0)],0))
        v = Cl.mv(reduce(lambda u,v: u+v, [a*x for a,x in zip(v_co, Cl.blades_lst0)],0))

        result = (u*v).blade_coefs()
        print(result)

        gl = module.binary_operation('mul', result, use_operators=True)

        self.assert_match_snapshot(
            gl
        )
