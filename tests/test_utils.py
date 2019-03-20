import snapshottest

from alglbraic.util import MetaString


class TestMetaString(snapshottest.TestCase):
    def test_meta_string(self):
        assert isinstance(MetaString("abc"), str)
        assert issubclass(MetaString(x=5), MetaString)

        class Wow(MetaString):
            pass

        MindBlown = Wow(a=1)(b=2)(c=3)
        assert MindBlown.__name__ == "MetaMetaMetaWow"
        assert MindBlown.a == 1
        assert MindBlown.b == 2
        assert MindBlown.c == 3

        assert issubclass(MindBlown, str)
