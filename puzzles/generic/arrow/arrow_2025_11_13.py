"""PuzzleMadness Arrow Sudoku — 2025-11-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-11-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/11/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(5, 0)], [(6, 1), (7, 2)])
    puzzle.add_arrow([(3, 4)], [(2, 3), (3, 3), (3, 2), (2, 1)])
    puzzle.add_arrow([(2, 6)], [(2, 5), (2, 4), (3, 5)])
    puzzle.add_arrow([(6, 3)], [(6, 4), (5, 3), (5, 2)])
    puzzle.add_arrow([(7, 5)], [(7, 6), (6, 5), (5, 6)])
    puzzle.add_arrow([(0, 6)], [(0, 7), (1, 8)])
    puzzle.add_arrow([(2, 2)], [(3, 1), (4, 1)])
    puzzle.add_arrow([(8, 6)], [(7, 7), (8, 7), (8, 8)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (4, 6)])
    puzzle.add_arrow([(1, 2)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(3, 0)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(6, 6)], [(6, 7), (5, 8)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (2, 7)])
    puzzle.add_arrow([(1, 3)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(8, 0)], [(7, 0), (8, 1)])
    puzzle.add_arrow([(8, 5)], [(7, 4), (8, 3)])
    puzzle.add_arrow([(4, 3)], [(4, 4), (5, 4)])

    return puzzle
