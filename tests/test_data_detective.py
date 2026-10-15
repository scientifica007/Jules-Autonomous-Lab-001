import importlib.util
import tempfile
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "experiments/data_detective/analyze.py"
spec = importlib.util.spec_from_file_location("data_detective", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DataDetectiveTests(unittest.TestCase):
    def from_csv(self, content):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.csv"
            path.write_text(content, encoding="utf-8")
            return module.load_rows(path)

    def test_summary(self):
        rows = self.from_csv("id,group,value\na,a,10\nb,a,20\nc,b,30\n")
        self.assertEqual(module.summarize(rows)["median"], 20)
        self.assertEqual(module.summarize(rows)["groups"], ["a", "b"])

    def test_empty_csv(self):
        self.assertEqual(module.summarize(self.from_csv("id,group,value\n"))["count"], 0)

    def test_reject_duplicate(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.from_csv("id,group,value\na,a,1\na,b,3\n")

    def test_reject_nonfinite(self):
        with self.assertRaisesRegex(ValueError, "non-finite"):
            self.from_csv("id,group,value\na,a,nan\n")

    def test_reject_incomplete_row(self):
        with self.assertRaises(ValueError):
            self.from_csv("id,group,value\na,a\n")

    def test_reject_bad_header(self):
        with self.assertRaisesRegex(ValueError, "columns"):
            self.from_csv("other,group,value\na,a,1\n")


if __name__ == "__main__":
    unittest.main()
