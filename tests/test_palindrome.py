import unittest
from itertools import product

from sudoku.constraints import PalindromeConstraint
from sudoku.puzzle import SudokuPuzzle
from sudoku.validator import validate_solution


SOLVED_GRID = [
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


def solved_assignment():
    return {
        (r, c): SOLVED_GRID[r][c]
        for r in range(9)
        for c in range(9)
    }


class TestPalindromeConstraint(unittest.TestCase):

    def test_valid_complete_odd_length(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 3,
                (1, 1): 7,
                (2, 2): 9,
                (3, 3): 7,
                (4, 4): 3,
            })
        )

    def test_valid_complete_even_length(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 2,
                (1, 1): 8,
                (2, 2): 8,
                (3, 3): 2,
            })
        )

    def test_invalid_complete_palindrome(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 3,
                (1, 1): 7,
                (2, 2): 4,
            })
        )

    def test_valid_partial_assignment(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 3,
                (1, 1): 7,
            })
        )

    def test_conflicting_partial_assignment(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        )

        self.assertFalse(
            constraint.is_satisfied({
                (1, 1): 7,
                (3, 3): 6,
            })
        )

    def test_unassigned_pairs_do_not_violate(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2), (3, 3)]
        )

        self.assertTrue(constraint.is_satisfied({}))

        self.assertTrue(
            constraint.is_satisfied({(1, 1): 5})
        )

    def test_center_cell_unrestricted(self):
        constraint = PalindromeConstraint(
            [(0, 0), (1, 1), (2, 2)]
        )

        # The center can be anything, including a value
        # equal to the mirrored endpoints.
        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 4,
                (1, 1): 9,
                (2, 2): 4,
            })
        )

    def test_single_cell_rejected(self):
        with self.assertRaises(ValueError):
            PalindromeConstraint([(0, 0)])

    def test_duplicate_cells_rejected(self):
        with self.assertRaises(ValueError):
            PalindromeConstraint([(0, 0), (1, 1), (0, 0)])


class TestPalindromePropagation(unittest.TestCase):

    def test_domain_intersection_example(self):
        constraint = PalindromeConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {1, 2, 3},
            (0, 1): {4, 5},
            (0, 2): {2, 3, 6},
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains[(0, 0)], {2, 3})
        self.assertEqual(domains[(0, 1)], {4, 5})
        self.assertEqual(domains[(0, 2)], {2, 3})

    def test_bidirectional_propagation(self):
        constraint = PalindromeConstraint(
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        )

        domains = {
            (0, 0): {7},
            (0, 1): set(range(1, 10)),
            (0, 2): {2, 3},
            (0, 3): set(range(1, 10)),
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)

        # Forward: the fixed first cell restricts the last.
        self.assertEqual(domains[(0, 3)], {7})

        # Backward: the restricted third cell restricts
        # the second.
        self.assertEqual(domains[(0, 1)], {2, 3})

    def test_center_cell_not_restricted(self):
        constraint = PalindromeConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {1},
            (0, 1): set(range(1, 10)),
            (0, 2): {1, 2},
        }

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 1)], set(range(1, 10)))
        self.assertEqual(domains[(0, 2)], {1})

    def test_contradiction_raises(self):
        constraint = PalindromeConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {1, 2},
            (0, 1): {5},
            (0, 2): {3, 4},
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_contradiction_does_not_mutate_domains(self):
        constraint = PalindromeConstraint(
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        )

        domains = {
            (0, 0): {1, 2},
            (0, 1): {3, 4},
            (0, 2): {4, 5},
            (0, 3): {8, 9},
        }

        snapshot = {
            cell: set(values)
            for cell, values in domains.items()
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

        self.assertEqual(domains, snapshot)

    def test_no_change_returns_false(self):
        constraint = PalindromeConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        domains = {
            (0, 0): {2, 3},
            (0, 1): {4, 5},
            (0, 2): {2, 3},
        }

        self.assertFalse(
            constraint.propagate(domains)
        )

    def test_propagation_preserves_supported_values(self):
        cells = [(0, 0), (0, 1), (0, 2), (0, 3)]
        constraint = PalindromeConstraint(cells)

        domains = {
            (0, 0): {1, 2, 5},
            (0, 1): {3, 4, 6},
            (0, 2): {4, 6, 7},
            (0, 3): {2, 5, 8},
        }

        # Brute force every complete assignment that is a
        # palindrome by definition.
        supported = {cell: set() for cell in cells}

        for values in product(*(domains[cell] for cell in cells)):
            n = len(values)

            if any(
                values[i] != values[n - 1 - i]
                for i in range(n // 2)
            ):
                continue

            for cell, value in zip(cells, values):
                supported[cell].add(value)

        self.assertTrue(
            any(supported.values()),
            "Test setup must admit at least one assignment"
        )

        constraint.propagate(domains)

        for cell in cells:
            self.assertTrue(
                supported[cell] <= domains[cell],
                f"Supported values removed from {cell}"
            )


class TestPalindromeIntegration(unittest.TestCase):

    def test_constraint_registration(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_palindrome([(0, 0), (1, 1), (2, 2)])

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 1
        )

        self.assertIsInstance(
            puzzle.constraints[-1],
            PalindromeConstraint
        )

    def test_overlapping_lines_allowed(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        baseline = len(puzzle.constraints)

        puzzle.add_palindrome([(0, 1), (1, 2), (2, 3)])
        puzzle.add_palindrome([(2, 1), (1, 2), (0, 3)])

        self.assertEqual(
            len(puzzle.constraints),
            baseline + 2
        )

    def test_line_longer_than_nine_cells(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        cells = [(0, c) for c in range(9)]
        cells += [(1, 8), (2, 7)]

        puzzle.add_palindrome(cells)

        self.assertEqual(
            len(puzzle.constraints[-1].variables),
            11
        )

    def test_non_adjacent_cells_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_palindrome([(0, 0), (0, 2)])

    def test_repeated_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_palindrome([(0, 0), (0, 1), (0, 0)])

    def test_out_of_bounds_cell_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_palindrome([(8, 8), (9, 8)])

    def test_single_cell_line_rejected(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        with self.assertRaises(ValueError):
            puzzle.add_palindrome([(0, 0)])

    def test_mirrored_pair_in_same_row_unsolvable(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C1 and R1C3 would need equal digits in one row.
        puzzle.add_palindrome([(0, 0), (0, 1), (0, 2)])

        solution, solver = puzzle.solve()

        self.assertIsNone(solution)

    def test_mirrored_pair_in_same_column_unsolvable(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        puzzle.add_palindrome([(0, 0), (1, 0), (2, 0)])

        solution, solver = puzzle.solve()

        self.assertIsNone(solution)

    def test_mirrored_pair_in_same_box_unsolvable(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C1 and R2C2 share a box and must be equal.
        puzzle.add_palindrome([(0, 0), (1, 1)])

        solution, solver = puzzle.solve()

        self.assertIsNone(solution)


class TestPalindromeValidation(unittest.TestCase):

    def test_validator_accepts_valid_line(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C3 = 4, R2C4 = 1, R3C5 = 4: a palindrome.
        puzzle.add_palindrome([(0, 2), (1, 3), (2, 4)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(errors, [])

    def test_validator_detects_mismatch(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # R1C1 = 5 and R3C3 = 8 differ.
        puzzle.add_palindrome([(0, 0), (1, 1), (2, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertTrue(
            any(
                "Palindrome mismatch: R1C1 and R3C3" in error
                for error in errors
            )
        )

    def test_validator_detects_incomplete_line(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])
        puzzle.add_palindrome([(0, 2), (1, 3), (2, 4)])

        solution = solved_assignment()
        del solution[(1, 3)]

        errors = validate_solution(puzzle, solution)

        self.assertTrue(
            any(
                "Palindrome line is incomplete" in error
                for error in errors
            )
        )

    def test_validator_handles_overlapping_lines(self):
        puzzle = SudokuPuzzle([[0] * 9 for _ in range(9)])

        # Both lines cross at their free center R2C4.
        puzzle.add_palindrome([(0, 2), (1, 3), (2, 4)])
        puzzle.add_palindrome([(0, 0), (1, 1), (2, 2)])

        errors = validate_solution(puzzle, solved_assignment())

        self.assertEqual(
            [
                error for error in errors
                if "Palindrome" in error
            ],
            ["Palindrome mismatch: R1C1 and R3C3"]
        )


if __name__ == "__main__":
    unittest.main()
