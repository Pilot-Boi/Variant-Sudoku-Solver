
import unittest

from puzzles.thermo_001 import create_puzzle


class TestThermoPuzzle(unittest.TestCase):

    def test_unique_solution(self):
        puzzle = create_puzzle()

        status, solutions, solver = puzzle.check_uniqueness()

        self.assertEqual(status, "unique")
        self.assertEqual(len(solutions), 1)

        solution = solutions[0]

        # Check every constraint.
        for constraint in puzzle.constraints:
            self.assertTrue(
                constraint.is_satisfied(solution)
            )


if __name__ == "__main__":
    unittest.main()