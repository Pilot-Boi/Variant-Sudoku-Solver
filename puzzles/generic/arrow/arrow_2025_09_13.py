"""PuzzleMadness Arrow Sudoku — 2025-09-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-09-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/9/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 3, 0, 0, 0, 7, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(0, 5)], [(1, 4), (2, 3), (3, 3)])
    puzzle.add_arrow([(1, 6)], [(2, 6), (3, 5), (3, 6)])
    puzzle.add_arrow([(6, 6)], [(7, 7), (6, 7), (5, 6)])
    puzzle.add_arrow([(0, 2)], [(1, 3), (0, 3)])
    puzzle.add_arrow([(3, 7)], [(4, 8), (5, 8)])
    puzzle.add_arrow([(7, 2)], [(8, 3), (7, 3)])
    puzzle.add_arrow([(6, 2)], [(5, 1), (5, 2), (4, 1)])
    puzzle.add_arrow([(3, 2)], [(2, 2), (1, 2)])
    puzzle.add_arrow([(7, 1)], [(6, 1), (7, 0)])
    puzzle.add_arrow([(0, 0)], [(0, 1), (1, 1)])
    puzzle.add_arrow([(8, 4)], [(8, 5), (7, 5), (6, 5)])
    puzzle.add_arrow([(2, 7)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(8, 7)], [(7, 8), (6, 8)])
    puzzle.add_arrow([(2, 5)], [(2, 4), (3, 4)])
    puzzle.add_arrow([(4, 3)], [(5, 4), (5, 3)])

    return puzzle
