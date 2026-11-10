
import unittest
from unittest.mock import patch

from puzzles.generic.killer.killer_001 import CAGES, create_puzzle
from sudoku.constraints import KillerCageConstraint

class TestKillerPuzzle(unittest.TestCase):

    def test_cage_layout(self):
        self.assertEqual(len(CAGES), 20)

        occupied = set()

        for target_sum, cells in CAGES:
            self.assertTrue(cells)

            n = len(cells)
            minimum = sum(range(1, n + 1))
            maximum = sum(range(10 - n, 10))

            self.assertGreaterEqual(target_sum, minimum)
            self.assertLessEqual(target_sum, maximum)

            for row, col in cells:
                self.assertTrue(0 <= row < 9)
                self.assertTrue(0 <= col < 9)

                self.assertNotIn(
                    (row, col),
                    occupied,
                    "Overlapping Killer cages"
                )

                occupied.add((row, col))

        # This puzzle has 15 uncaged cells.
        self.assertEqual(len(occupied), 64)

    def test_create_puzzle(self):
        puzzle = create_puzzle()

        # 27 standard Sudoku constraints
        # plus 20 Killer cages.
        self.assertEqual(len(puzzle.constraints), 47)
    def test_nine_cell_cage_skips_support_search(self):
        cells = [(0, c) for c in range(9)]
        cage = KillerCageConstraint(cells, 45)

        domains = {
            cell: set(range(1, 10))
            for cell in cells
        }

        domains[(0, 0)] = {1}

        with patch.object(
            KillerCageConstraint,
            "_find_supports",
            side_effect=AssertionError(
                "Full-digit cage should not enumerate assignments"
            ),
        ):
            cage.propagate(domains)

        for cell in cells[1:]:
            self.assertNotIn(1, domains[cell])

if __name__ == "__main__":
    unittest.main()
