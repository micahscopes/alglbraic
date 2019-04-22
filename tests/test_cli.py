import snapshottest
from click.testing import CliRunner
from alglbraic.util.cli import cli


class TestCLI(snapshottest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_complex_numbers(self):
        result = self.runner.invoke(cli, ["complex-numbers"])
        # assert result.exit_code == 0
        self.assert_match_snapshot(result.output)

    def test_dual_numbers(self):
        result = self.runner.invoke(cli, ["dual-numbers"])
        # assert result.exit_code == 0
        self.assert_match_snapshot(result.output)
