import unittest

from puzzles.anti_knight_001 import create_puzzle
from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution
from sudoku.constraints import (
    generate_knight_pairs,
    NotEqualConstraint
)


class TestAntiKnight(unittest.TestCase):

    def test_knight_pair_count(self):
        pairs = generate_knight_pairs()

        self.assertEqual(len(pairs), 224)

    def test_no_duplicate_pairs(self):
        pairs = generate_knight_pairs()

        self.assertEqual(len(pairs), len(set(pairs)))

    def test_center_cell_has_eight_neighbors(self):
        pairs = generate_knight_pairs()
        center = (4, 4)

        neighbors = {
            b if a == center else a
            for a, b in pairs
            if center in (a, b)
        }

        self.assertEqual(len(neighbors), 8)

    def test_corner_has_two_neighbors(self):
        pairs = generate_knight_pairs()
        corner = (0, 0)

        neighbors = {
            b if a == corner else a
            for a, b in pairs
            if corner in (a, b)
        }

        self.assertEqual(
            neighbors,
            {(1, 2), (2, 1)}
        )


class TestNotEqualConstraint(unittest.TestCase):

    def test_valid_assignment(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        assignment = {
            (0, 0): 5,
            (1, 2): 7,
        }

        self.assertTrue(
            constraint.is_satisfied(assignment)
        )

    def test_invalid_assignment(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        assignment = {
            (0, 0): 5,
            (1, 2): 5,
        }

        self.assertFalse(
            constraint.is_satisfied(assignment)
        )

    def test_partial_assignment(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        self.assertTrue(
            constraint.is_satisfied({(0, 0): 5})
        )

    def test_propagation(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        domains = {
            (0, 0): {5},
            (1, 2): {2, 5, 8},
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(1, 2)], {2, 8})

    def test_reverse_propagation(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        domains = {
            (0, 0): {2, 5, 8},
            (1, 2): {5},
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 0)], {2, 8})

    def test_no_change(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        domains = {
            (0, 0): {2, 5},
            (1, 2): {3, 7},
        }

        self.assertFalse(
            constraint.propagate(domains)
        )

    def test_contradiction(self):
        constraint = NotEqualConstraint((0, 0), (1, 2))

        domains = {
            (0, 0): {5},
            (1, 2): {5},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_same_cell_rejected(self):
        with self.assertRaises(ValueError):
            NotEqualConstraint((0, 0), (0, 0))


class TestAntiKnightIntegration(unittest.TestCase):

    def test_constraint_count(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        puzzle.add_anti_knight_constraints()

        self.assertEqual(len(puzzle.constraints), 251)

    def test_knight_conflict_detected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_anti_knight_constraints()

        # These two cells are a knight's move apart.
        solution = {
            (0, 0): 5,
            (1, 2): 5,
        }

        knight_constraints = [
            constraint
            for constraint in puzzle.constraints
            if isinstance(constraint, NotEqualConstraint)
        ]

        self.assertTrue(
            any(
                not constraint.is_satisfied(solution)
                for constraint in knight_constraints
            )
        )

    def test_knight_propagation(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_anti_knight_constraints()

        domains = {
            cell: set(range(1, 10))
            for cell in puzzle.variables
        }

        domains[(0, 0)] = {5}

        knight_constraints = [
            constraint
            for constraint in puzzle.constraints
            if isinstance(constraint, NotEqualConstraint)
        ]

        for constraint in knight_constraints:
            constraint.propagate(domains)

        self.assertNotIn(5, domains[(1, 2)])
        self.assertNotIn(5, domains[(2, 1)])

    def test_validator_detects_knight_conflict(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_anti_knight_constraints()

        # A valid standard Sudoku, but not Anti-Knight.
        grid = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]

        solution = {
            (r, c): grid[r][c]
            for r in range(9)
            for c in range(9)
        }

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any("Not-equal constraint violation" in error for error in errors)
        )


class TestAntiKnightPuzzle(unittest.TestCase):

    def test_unique_solution(self):
        puzzle = create_puzzle()

        status, solutions, solver = puzzle.check_uniqueness()

        self.assertEqual(status, "unique")
        self.assertEqual(len(solutions), 1)

        errors = validate_solution(puzzle, solutions[0])
        self.assertEqual(errors, [])

    def test_constraint_count(self):
        puzzle = create_puzzle()

        self.assertEqual(len(puzzle.constraints), 251)


if __name__ == "__main__":
    unittest.main()