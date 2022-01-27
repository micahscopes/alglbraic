from snapshottest import TestCase
from click.testing import CliRunner
from alglbraic.util.cli import build_cli



class TestCLI(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_complex_numbers(self):
        result = self.runner.invoke(build_cli(), ["complex-numbers"])
        # assert result.exit_code == 0
        self.assert_match_snapshot(result.output)

    def test_dual_numbers(self):
        result = self.runner.invoke(build_cli(), ["dual-numbers"])
        # assert result.exit_code == 0
        self.assert_match_snapshot(result.output)
