
import unittest

from sudoku.constraints import (
    NonConsecutiveConstraint,
    generate_orthogonal_pairs,
)
from sudoku.puzzle import SudokuPuzzle
from puzzles.nonconsecutive_001 import create_puzzle
from sudoku.validator import validate_solution


class TestNonConsecutive(unittest.TestCase):

    def test_pair_count(self):
        self.assertEqual(
            len(generate_orthogonal_pairs()),
            144
        )

    def test_no_duplicate_pairs(self):
        pairs = generate_orthogonal_pairs()

        self.assertEqual(len(pairs), len(set(pairs)))

    def test_all_pairs_are_orthogonal(self):
        for a, b in generate_orthogonal_pairs():
            distance = (
                abs(a[0] - b[0])
                + abs(a[1] - b[1])
            )

            self.assertEqual(distance, 1)

    def test_constraint_count(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_nonconsecutive_constraints()

        self.assertEqual(len(puzzle.constraints), 171)

    def test_consecutive_digits_rejected(self):
        constraint = NonConsecutiveConstraint(
            (0, 0), (0, 1)
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 4,
                (0, 1): 5,
            })
        )

    def test_nonconsecutive_digits_allowed(self):
        constraint = NonConsecutiveConstraint(
            (0, 0), (0, 1)
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 4,
                (0, 1): 7,
            })
        )

    def test_equal_digits_allowed_by_constraint(self):
        constraint = NonConsecutiveConstraint(
            (0, 0), (0, 1)
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 5,
                (0, 1): 5,
            })
        )

    def test_propagation(self):
        constraint = NonConsecutiveConstraint(
            (0, 0), (0, 1)
        )

        domains = {
            (0, 0): {3, 4, 7},
            (0, 1): {4},
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 0)], {4, 7})

    def test_propagation_contradiction(self):
        constraint = NonConsecutiveConstraint(
            (0, 0), (0, 1)
        )

        domains = {
            (0, 0): {3},
            (0, 1): {4},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_validator_detects_violation(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_nonconsecutive_constraints()

        assignment = {
            (0, 0): 4,
            (0, 1): 5,
        }

        errors = validate_solution(puzzle, assignment)

        self.assertTrue(
            any(
                "Nonconsecutive violation" in error
                for error in errors
            )
        )

class TestNonConsecutivePuzzle(unittest.TestCase):

    def test_constraint_count(self):
        puzzle = create_puzzle()
        self.assertEqual(len(puzzle.constraints), 171)

    def test_unique_solution(self):
        puzzle = create_puzzle()

        status, solutions, solver = puzzle.check_uniqueness()

        self.assertEqual(status, "unique")
        self.assertEqual(len(solutions), 1)

        errors = validate_solution(puzzle, solutions[0])
        self.assertEqual(errors, [])

if __name__ == "__main__":
    unittest.main()
