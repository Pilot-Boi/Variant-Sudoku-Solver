"""PuzzleMadness Arrow Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 7, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 1)], [(4, 0), (5, 0)])
    puzzle.add_arrow([(5, 5)], [(6, 4), (5, 4)])
    puzzle.add_arrow([(2, 0)], [(3, 0), (3, 1), (4, 2)])
    puzzle.add_arrow([(6, 0)], [(7, 0), (8, 0), (8, 1)])
    puzzle.add_arrow([(4, 8)], [(3, 8), (4, 7), (3, 6), (2, 7)])
    puzzle.add_arrow([(3, 5)], [(4, 5), (5, 6)])
    puzzle.add_arrow([(1, 0)], [(0, 1), (0, 0)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (7, 7), (6, 8)])
    puzzle.add_arrow([(6, 5)], [(6, 6), (7, 5)])
    puzzle.add_arrow([(2, 3)], [(1, 3), (2, 2), (2, 1)])
    puzzle.add_arrow([(6, 2)], [(5, 3), (4, 4)])
    puzzle.add_arrow([(8, 2)], [(7, 2), (8, 3)])
    puzzle.add_arrow([(1, 5)], [(0, 4), (1, 4)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (1, 2)])
    puzzle.add_arrow([(1, 8)], [(0, 7), (1, 6)])
    puzzle.add_arrow([(3, 7)], [(2, 6), (2, 5)])
    puzzle.add_arrow([(6, 7)], [(5, 7), (5, 8)])

    return puzzle
