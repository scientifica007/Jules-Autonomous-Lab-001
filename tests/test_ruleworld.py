import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "experiments/ruleworld/ruleworld.py"
spec = importlib.util.spec_from_file_location("ruleworld", PATH)
ruleworld = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ruleworld)


class RuleworldTests(unittest.TestCase):
    def test_block_is_stable(self):
        live = set(ruleworld.PATTERNS["block"])
        self.assertEqual(ruleworld.evolve(live, 8, 8), live)

    def test_blinker_period_two(self):
        start = set(ruleworld.PATTERNS["blinker"])
        once = ruleworld.evolve(start, 8, 8)
        self.assertNotEqual(once, start)
        self.assertEqual(ruleworld.evolve(once, 8, 8), start)

    def test_empty_stays_empty(self):
        self.assertEqual(ruleworld.evolve(set(), 5, 5), set())

    def test_default_has_no_horizontal_wrap(self):
        # Boundary-adjacent cells do not interact through left/right edges.
        live = {(0, 0), (0, 1), (4, 0)}
        self.assertNotIn((4, 1), ruleworld.evolve(live, 5, 5))

    def test_negative_steps_are_rejected(self):
        with self.assertRaises(ValueError):
            ruleworld.simulate("block", 8, 8, -1)

    def test_pattern_too_large(self):
        with self.assertRaises(ValueError):
            ruleworld.simulate("glider", 2, 2, 1)


if __name__ == "__main__":
    unittest.main()
