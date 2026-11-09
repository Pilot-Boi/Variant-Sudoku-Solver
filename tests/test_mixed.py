
import unittest

from puzzles.thermo_killer_001 import create_puzzle as create_mixed_001
from puzzles.thermo_killer_002 import create_puzzle as create_mixed_002
from puzzles.anti_king_anti_knight_001 import (
    create_puzzle as create_anti_king_knight
)
from sudoku.validator import validate_solution


class TestMixedPuzzles(unittest.TestCase):

    def check_mixed_puzzle(self, create_puzzle, expected_constraints=None):
        puzzle = create_puzzle()

        if expected_constraints is not None:
            self.assertEqual(
                len(puzzle.constraints),
                expected_constraints
            )

        status, solutions, solver = puzzle.check_uniqueness()

        self.assertEqual(status, "unique")
        self.assertEqual(len(solutions), 1)

        errors = validate_solution(puzzle, solutions[0])

        self.assertEqual(
            errors,
            [],
            f"Solution validation failed: {errors}"
        )

    def test_thermo_killer_001_unique_and_valid(self):
        self.check_mixed_puzzle(create_mixed_001)

    def test_thermo_killer_002_unique_and_valid(self):
        self.check_mixed_puzzle(create_mixed_002)

    def test_anti_king_anti_knight_001_unique_and_valid(self):
        self.check_mixed_puzzle(
            create_anti_king_knight,
            expected_constraints=379
        )


if __name__ == "__main__":
    unittest.main()