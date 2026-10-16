"""Check specification expectations and CLI exit codes in both supported folder layouts."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "study_stats.py"
if not SCRIPT.is_file():
    SCRIPT = HERE.parent / "src" / "study_stats.py"
spec = importlib.util.spec_from_file_location("study_stats", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class StudyStatsTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True, text=True, encoding="utf-8", timeout=10,
        )

    def test_normal_summary(self):
        self.assertEqual(module.summarize([25, 50]), (2, 75, 37.5))

    def test_zero_boundary(self):
        self.assertEqual(module.summarize([0]), (1, 0, 0.0))

    def test_upper_boundary(self):
        self.assertEqual(module.summarize([1440]), (1, 1440, 1440.0))

    def test_empty_summary(self):
        with self.assertRaises(ValueError):
            module.summarize([])

    def test_invalid_values(self):
        for values in ([-1], [1441], [1.5], ["25"], [True]):
            with self.subTest(values=values), self.assertRaises(ValueError):
                module.summarize(values)

    def test_cli_normal(self):
        result = self.run_cli("25", "50")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Count: 2 / Total: 75 min / Average: 37.5 min")
        self.assertEqual(result.stderr, "")

    def test_cli_boundaries(self):
        for argument, output in (
            ("0", "Count: 1 / Total: 0 min / Average: 0.0 min"),
            ("1440", "Count: 1 / Total: 1440 min / Average: 1440.0 min"),
        ):
            with self.subTest(argument=argument):
                result = self.run_cli(argument)
                self.assertEqual(result.returncode, 0)
                self.assertEqual(result.stdout.strip(), output)

    def test_cli_invalid(self):
        for arguments in ([], ["-1"], ["1441"], ["1.5"], ["abc"], ["25", "abc"]):
            with self.subTest(arguments=arguments):
                result = self.run_cli(*arguments)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Error:", result.stderr)
                self.assertEqual(result.stdout, "")

    def test_cli_repeatable(self):
        self.assertEqual(self.run_cli("25", "50").stdout, self.run_cli("25", "50").stdout)


if __name__ == "__main__":
    unittest.main()
