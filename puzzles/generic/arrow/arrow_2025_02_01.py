"""PuzzleMadness Arrow Sudoku — 2025-02-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 5, 3, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 2)], [(4, 1), (3, 2)])
    puzzle.add_arrow([(0, 1)], [(1, 2), (0, 3), (1, 4)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (7, 8), (8, 7)])
    puzzle.add_arrow([(5, 1)], [(6, 1), (5, 0), (6, 0)])
    puzzle.add_arrow([(6, 4)], [(7, 5), (8, 6)])
    puzzle.add_arrow([(1, 6)], [(2, 7), (3, 7), (4, 6)])
    puzzle.add_arrow([(4, 4)], [(3, 4), (2, 4), (3, 3)])
    puzzle.add_arrow([(8, 4)], [(7, 3), (7, 2), (8, 1)])
    puzzle.add_arrow([(0, 7)], [(0, 8), (1, 8)])
    puzzle.add_arrow([(2, 6)], [(1, 5), (0, 5), (0, 4)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (2, 2)])
    puzzle.add_arrow([(4, 5)], [(5, 4), (6, 5)])
    puzzle.add_arrow([(3, 1)], [(4, 2), (4, 3)])
    puzzle.add_arrow([(4, 8)], [(5, 7), (5, 8)])
    puzzle.add_arrow([(4, 0)], [(3, 0), (2, 1)])

    return puzzle
