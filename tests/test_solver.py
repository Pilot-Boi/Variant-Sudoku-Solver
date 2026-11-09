
import unittest

from csp.solver import CSPSolver
from sudoku.puzzle import SudokuPuzzle
from sudoku.constraints import (
    AllDifferentConstraint,
    ThermometerConstraint,
    KillerCageConstraint
)


class TestSudokuSolver(unittest.TestCase):

    def test_standard_sudoku(self):
        grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]

        puzzle = SudokuPuzzle(grid)
        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 81)

        for constraint in puzzle.constraints:
            self.assertTrue(constraint.is_satisfied(solution))

    def test_invalid_sudoku(self):
        grid = [[0] * 9 for _ in range(9)]

        # Duplicate 5 in the first row
        grid[0][0] = 5
        grid[0][1] = 5

        puzzle = SudokuPuzzle(grid)
        solution, solver = puzzle.solve()

        self.assertIsNone(solution)

    def test_all_different(self):
        constraint = AllDifferentConstraint(
            [(0, 0), (0, 1), (0, 2)]
        )

        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 1): 2,
                (0, 2): 3
            })
        )

        self.assertFalse(
            constraint.is_satisfied({
                (0, 0): 1,
                (0, 1): 2,
                (0, 2): 1
            })
        )

        # Partial assignments should be valid
        self.assertTrue(
            constraint.is_satisfied({
                (0, 0): 1
            })
        )
        

    def test_valid_thermometer(self):
        cells = [(0, i) for i in range(4)]
        thermo = ThermometerConstraint(cells)

        assignment = {
            cells[0]: 2,
            cells[1]: 4,
            cells[2]: 6,
            cells[3]: 8
        }

        self.assertTrue(thermo.is_satisfied(assignment))

    def test_invalid_thermometer(self):
        cells = [(0, i) for i in range(4)]
        thermo = ThermometerConstraint(cells)

        assignment = {
            cells[0]: 2,
            cells[1]: 6,
            cells[2]: 4,
            cells[3]: 8
        }

        self.assertFalse(thermo.is_satisfied(assignment))

    def test_partial_thermometer(self):
        cells = [(0, i) for i in range(4)]
        thermo = ThermometerConstraint(cells)

        assignment = {
            cells[0]: 2,
            cells[2]: 6
        }

        self.assertTrue(thermo.is_satisfied(assignment))

    def test_impossible_partial_thermometer(self):
        cells = [(0, i) for i in range(4)]
        thermo = ThermometerConstraint(cells)

        assignment = {
            cells[0]: 5,
            cells[2]: 3
        }

        self.assertFalse(thermo.is_satisfied(assignment))

    def test_thermometer_position_bounds(self):
        cells = [(0, i) for i in range(5)]
        thermo = ThermometerConstraint(cells)

        # The bulb cannot be 6 on a 5-cell thermo.
        self.assertFalse(
            thermo.is_satisfied({cells[0]: 6})
        )

        # The tip cannot be 4.
        self.assertFalse(
            thermo.is_satisfied({cells[4]: 4})
        )

    def test_thermometer_too_long(self):
        cells = [(i, 0) for i in range(10)]
        thermo = ThermometerConstraint(cells)

        # No 10-cell strictly increasing sequence
        # can fit into digits 1-9.
        self.assertFalse(
            thermo.is_satisfied({})
        )


    def test_additional_constraint(self):
        variables = ["A", "B"]
        domains = {
            "A": {1, 2, 3},
            "B": {1, 2, 3}
        }

        constraint = AllDifferentConstraint(variables)

        solver = CSPSolver(
            variables,
            domains,
            [constraint]
        )

        solution = solver.solve()

        self.assertIsNotNone(solution)
        self.assertNotEqual(
            solution["A"],
            solution["B"]
        )

    def test_invalid_grid_size(self):
        grid = [[0] * 8 for _ in range(9)]

        with self.assertRaises(ValueError):
            SudokuPuzzle(grid)
            
    
    def test_diagonal_sudoku(self):
        grid = [[0] * 9 for _ in range(9)]

        puzzle = SudokuPuzzle(grid)
        puzzle.add_diagonal_constraints()

        solution, solver = puzzle.solve()

        self.assertIsNotNone(solution)

        main_diagonal = [
            solution[(i, i)] for i in range(9)
        ]

        anti_diagonal = [
            solution[(i, 8 - i)] for i in range(9)
        ]

        self.assertEqual(
            set(main_diagonal), set(range(1, 10))
        )

        self.assertEqual(
            set(anti_diagonal), set(range(1, 10))
        )

        for constraint in puzzle.constraints:
            self.assertTrue(
                constraint.is_satisfied(solution)
            )

    def test_thermometer_propagation(self):
        cells = [(0, i) for i in range(5)]
        thermo = ThermometerConstraint(cells)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        changed = thermo.propagate(domains)

        self.assertTrue(changed)

        expected = [
            {1, 2, 3, 4, 5},
            {2, 3, 4, 5, 6},
            {3, 4, 5, 6, 7},
            {4, 5, 6, 7, 8},
            {5, 6, 7, 8, 9}
        ]

        for cell, values in zip(cells, expected):
            self.assertEqual(domains[cell], values)

    def test_thermometer_propagation_with_given(self):
        cells = [(0, i) for i in range(4)]
        thermo = ThermometerConstraint(cells)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        # Force the tip to be 6.
        domains[cells[3]] = {6}

        thermo.propagate(domains)

        self.assertEqual(domains[cells[0]], {1, 2, 3})
        self.assertEqual(domains[cells[1]], {2, 3, 4})
        self.assertEqual(domains[cells[2]], {3, 4, 5})
        self.assertEqual(domains[cells[3]], {6})

    def test_all_different_propagation(self):
        cells = ["A", "B", "C"]
        constraint = AllDifferentConstraint(cells)

        domains = {
            "A": {1},
            "B": {1, 2},
            "C": {1, 2, 3}
        }

        constraint.propagate(domains)

        self.assertEqual(domains["A"], {1})
        self.assertEqual(domains["B"], {2})
        self.assertEqual(domains["C"], {2, 3})

        # A second pass propagates B's singleton.
        constraint.propagate(domains)

        self.assertEqual(domains["C"], {3})

    def test_propagation_contradiction(self):
        cells = ["A", "B"]
        constraint = AllDifferentConstraint(cells)

        domains = {
            "A": {5},
            "B": {5}
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_solver_without_search(self):
        variables = ["A", "B"]
        domains = {
            "A": {1},
            "B": {1, 2}
        }

        solver = CSPSolver(
            variables,
            domains,
            [AllDifferentConstraint(variables)]
        )

        solution = solver.solve()

        self.assertEqual(solution, {"A": 1, "B": 2})
        self.assertEqual(solver.nodes, 0)


    def test_unique_solution(self):
        grid = [
            [5, 3, 0, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ]

        puzzle = SudokuPuzzle(grid)
        status, solutions, solver = puzzle.check_uniqueness()

        self.assertEqual(status, "unique")
        self.assertEqual(len(solutions), 1)

    def test_multiple_solutions(self):
        variables = ["A", "B"]
        domains = {
            "A": {1, 2, 3},
            "B": {1, 2, 3}
        }

        solver = CSPSolver(
            variables,
            domains,
            [AllDifferentConstraint(variables)]
        )

        solutions = solver.solve_all(limit=2)

        self.assertEqual(len(solutions), 2)
        self.assertNotEqual(solutions[0], solutions[1])

    def test_no_solutions(self):
        variables = ["A", "B"]
        domains = {
            "A": {1},
            "B": {1}
        }

        solver = CSPSolver(
            variables,
            domains,
            [AllDifferentConstraint(variables)]
        )

        solutions = solver.solve_all(limit=2)

        self.assertEqual(len(solutions), 0)

    def test_hidden_single(self):
        variables = ["A", "B", "C"]

        constraint = AllDifferentConstraint(
            variables,
            required_values={1, 2, 3}
        )

        domains = {
            "A": {1, 2},
            "B": {1, 2},
            "C": {2, 3}
        }

        constraint.propagate(domains)

        self.assertEqual(domains["C"], {3})

    
    def test_hidden_single_not_applied_without_required_values(self):
        variables = ["A", "B", "C"]

        constraint = AllDifferentConstraint(variables)

        domains = {
            "A": {1, 2, 4},
            "B": {1, 2, 4},
            "C": {2, 3, 4}
        }

        constraint.propagate(domains)

        # Without required_values, the solver cannot
        # assume that every digit must appear.
        #
        # No naked pairs exist either, so the
        # domains should remain unchanged.
        self.assertEqual(domains["A"], {1, 2, 4})
        self.assertEqual(domains["B"], {1, 2, 4})
        self.assertEqual(domains["C"], {2, 3, 4})

    def test_missing_required_value(self):
        variables = ["A", "B", "C"]

        constraint = AllDifferentConstraint(
            variables,
            required_values={1, 2, 3}
        )

        domains = {
            "A": {1, 2},
            "B": {1, 2},
            "C": {1, 2}
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_required_values_restriction(self):
        variables = ["A", "B", "C"]

        constraint = AllDifferentConstraint(
            variables,
            required_values={1, 2, 3}
        )

        domains = {
            "A": {1, 4},
            "B": {2},
            "C": {3}
        }

        constraint.propagate(domains)

        self.assertEqual(domains["A"], {1})

    def test_naked_pair(self):
        variables = ["A", "B", "C", "D"]

        constraint = AllDifferentConstraint(variables)

        domains = {
            "A": {2, 7},
            "B": {2, 7},
            "C": {2, 5, 7},
            "D": {1, 7, 9}
        }

        changed = constraint.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains["A"], {2, 7})
        self.assertEqual(domains["B"], {2, 7})
        self.assertEqual(domains["C"], {5})
        self.assertEqual(domains["D"], {1, 9})

    def test_naked_pair_contradiction(self):
        variables = ["A", "B", "C"]

        constraint = AllDifferentConstraint(variables)

        domains = {
            "A": {2, 7},
            "B": {2, 7},
            "C": {2, 7}
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_no_naked_pair(self):
        variables = ["A", "B", "C"]

        constraint = AllDifferentConstraint(variables)

        domains = {
            "A": {1, 2},
            "B": {1, 3},
            "C": {2, 3}
        }

        changed = constraint.propagate(domains)

        self.assertFalse(changed)
        self.assertEqual(domains["A"], {1, 2})
        self.assertEqual(domains["B"], {1, 3})
        self.assertEqual(domains["C"], {2, 3})

    def test_naked_pair_with_required_values(self):
        variables = ["A", "B", "C", "D"]

        constraint = AllDifferentConstraint(
            variables,
            required_values={1, 2, 3, 4}
        )

        domains = {
            "A": {1, 2},
            "B": {1, 2},
            "C": {1, 2, 3},
            "D": {3, 4}
        }

        constraint.propagate(domains)

        self.assertEqual(domains["C"], {3})
        self.assertEqual(domains["D"], {4})
    
    
    def test_naked_triple(self):
        constraint = AllDifferentConstraint(
            ["A", "B", "C", "D"]
        )

        domains = {
            "A": {1, 4},
            "B": {1, 4, 7},
            "C": {4, 7},
            "D": {1, 3, 7, 9}
        }

        # Repeat until no more changes occur.
        while constraint.propagate(domains):
            pass

        self.assertEqual(domains["D"], {3, 9})

    def test_naked_quadruple(self):
        constraint = AllDifferentConstraint(
            ["A", "B", "C", "D", "E"]
        )

        domains = {
            "A": {1, 2},
            "B": {2, 3},
            "C": {3, 4},
            "D": {1, 4},
            "E": {1, 2, 3, 4, 5}
        }

        while constraint.propagate(domains):
            pass

        self.assertEqual(domains["E"], {5})

    def test_naked_subset_disabled(self):
        constraint = AllDifferentConstraint(
            ["A", "B", "C", "D"],
            max_subset_size=2
        )

        domains = {
            "A": {1, 4},
            "B": {1, 4, 7},
            "C": {4, 7},
            "D": {1, 3, 7, 9}
        }

        constraint.propagate(domains)

        self.assertEqual(domains["D"], {1, 3, 7, 9})

    def test_naked_subset_contradiction(self):
        constraint = AllDifferentConstraint(
            ["A", "B", "C", "D"]
        )

        domains = {
            "A": {1, 2},
            "B": {1, 2},
            "C": {1, 2},
            "D": {3, 4}
        }

        with self.assertRaises(ValueError):
            constraint.propagate(domains)


    def test_killer_cage_valid(self):
        cage = KillerCageConstraint(["A", "B"], 10)

        self.assertTrue(
            cage.is_satisfied({"A": 4, "B": 6})
        )

        self.assertFalse(
            cage.is_satisfied({"A": 4, "B": 5})
        )

        self.assertFalse(
            cage.is_satisfied({"A": 5, "B": 5})
        )

    def test_killer_cage_propagation(self):
        cage = KillerCageConstraint(["A", "B"], 3)

        domains = {
            "A": {1, 2, 3, 4},
            "B": {1, 2, 3, 4}
        }

        changed = cage.propagate(domains)

        self.assertTrue(changed)
        self.assertEqual(domains["A"], {1, 2})
        self.assertEqual(domains["B"], {1, 2})

    def test_killer_cage_with_given(self):
        cage = KillerCageConstraint(["A", "B"], 10)

        domains = {
            "A": {4},
            "B": set(range(1, 10))
        }

        cage.propagate(domains)

        self.assertEqual(domains["B"], {6})

    def test_killer_cage_contradiction(self):
        cage = KillerCageConstraint(["A", "B"], 3)

        domains = {
            "A": {3},
            "B": {4}
        }

        with self.assertRaises(ValueError):
            cage.propagate(domains)

    def test_killer_cage_invalid_sum(self):
        with self.assertRaises(ValueError):
            KillerCageConstraint(["A", "B"], 20)

    def test_killer_cage_no_repeated_digits(self):
        cage = KillerCageConstraint(["A", "B"], 10)

        domains = {
            "A": {5},
            "B": {5}
        }

        with self.assertRaises(ValueError):
            cage.propagate(domains)


    def test_killer_cage_cache(self):
        cage = KillerCageConstraint(["A", "B"], 10)

        domains1 = {
            "A": {1, 2, 3, 4, 5, 6, 7, 8, 9},
            "B": {1, 2, 3, 4, 5, 6, 7, 8, 9}
        }

        cage.propagate(domains1)

        cache_size = len(cage._support_cache)

        # Same starting domains should reuse the cache.
        domains2 = {
            "A": set(range(1, 10)),
            "B": set(range(1, 10))
        }

        cage.propagate(domains2)

        self.assertEqual(
            len(cage._support_cache),
            cache_size
        )

        self.assertGreater(cache_size, 0)

    def test_killer_cage_cache_contradiction(self):
        cage = KillerCageConstraint(["A", "B"], 3)

        domains = {
            "A": {3},
            "B": {4}
        }

        for _ in range(2):
            with self.assertRaises(ValueError):
                cage.propagate({
                    var: values.copy()
                    for var, values in domains.items()
                })
    def test_full_digit_killer_cage(self):
        cells = [(0, c) for c in range(9)]

        constraint = KillerCageConstraint(cells, 45)

        self.assertTrue(constraint.full_digit_cage)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        domains[(0, 0)] = {1}

        changed = constraint.propagate(domains)

        self.assertTrue(changed)

        for cell in cells[1:]:
            self.assertNotIn(1, domains[cell])

    def test_full_digit_killer_cage_contradiction(self):
        cells = [(0, c) for c in range(9)]

        constraint = KillerCageConstraint(cells, 45)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        domains[(0, 0)] = {5}
        domains[(0, 1)] = {5}

        with self.assertRaises(ValueError):
            constraint.propagate(domains)

    def test_full_digit_killer_cage_naked_pair(self):
        cells = [(0, c) for c in range(9)]

        constraint = KillerCageConstraint(cells, 45)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        domains[(0, 0)] = {2, 7}
        domains[(0, 1)] = {2, 7}
        domains[(0, 2)] = {2, 3, 7, 9}

        constraint.propagate(domains)

        self.assertEqual(domains[(0, 2)], {3, 9})
        
if __name__ == "__main__":
    unittest.main()
