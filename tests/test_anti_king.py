import unittest

from puzzles.generic.anti_king.anti_king_001 import create_puzzle
from sudoku.constraints import (
    NotEqualConstraint,
    generate_king_pairs,
)
from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution


class TestAntiKing(unittest.TestCase):

    def test_pair_count(self):
        pairs = generate_king_pairs()
        self.assertEqual(len(pairs), 128)

    def test_no_duplicate_pairs(self):
        pairs = generate_king_pairs()
        self.assertEqual(len(pairs), len(set(pairs)))

    def test_all_pairs_are_diagonal(self):
        for a, b in generate_king_pairs():
            dr = abs(a[0] - b[0])
            dc = abs(a[1] - b[1])

            self.assertEqual((dr, dc), (1, 1))

    def test_center_has_four_diagonal_neighbors(self):
        center = (4, 4)

        neighbors = set()

        for a, b in generate_king_pairs():
            if a == center:
                neighbors.add(b)
            elif b == center:
                neighbors.add(a)

        self.assertEqual(
            neighbors,
            {(3, 3), (3, 5), (5, 3), (5, 5)}
        )

    def test_corner_has_one_diagonal_neighbor(self):
        corner = (0, 0)

        neighbors = set()

        for a, b in generate_king_pairs():
            if a == corner:
                neighbors.add(b)
            elif b == corner:
                neighbors.add(a)

        self.assertEqual(neighbors, {(1, 1)})

    def test_constraint_count(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_anti_king_constraints()

        self.assertEqual(len(puzzle.constraints), 155)

    def test_diagonal_duplicate_rejected(self):
        constraint = NotEqualConstraint((0, 0), (1, 1))

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 5,
                (1, 1): 5,
            })
        )

    def test_different_digits_allowed(self):
        constraint = NotEqualConstraint((0, 0), (1, 1))

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 5,
                (1, 1): 7,
            })
        )

    def test_validator_detects_king_conflict(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_anti_king_constraints()

        assignment = {
            (0, 2): 5,
            (1, 3): 5,
        }

        errors = validate_solution(puzzle, assignment)

        self.assertTrue(
            any(
                "Not-equal constraint violation" in error
                for error in errors
            )
        )

class TestAntiKingPuzzle(unittest.TestCase):

    def test_constraint_count(self):
        puzzle = create_puzzle()

        self.assertEqual(
            len(puzzle.constraints),
            155
        )

    def test_unique_solution(self):
        puzzle = create_puzzle()

        status, solutions, solver = puzzle.check_uniqueness()

        self.assertEqual(status, "unique")
        self.assertEqual(len(solutions), 1)

        errors = validate_solution(puzzle, solutions[0])

        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()