"""PuzzleMadness Arrow Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(8, 1)], [(7, 0), (6, 1), (5, 0)])
    puzzle.add_arrow([(6, 3)], [(5, 2), (4, 3), (3, 3), (4, 2)])
    puzzle.add_arrow([(6, 6)], [(6, 5), (6, 4)])
    puzzle.add_arrow([(2, 6)], [(3, 5), (2, 5), (1, 6)])
    puzzle.add_arrow([(3, 7)], [(3, 6), (4, 6), (4, 7)])
    puzzle.add_arrow([(7, 6)], [(6, 7), (5, 6)])
    puzzle.add_arrow([(7, 2)], [(7, 1), (6, 2)])
    puzzle.add_arrow([(3, 2)], [(2, 1), (1, 1), (0, 2)])
    puzzle.add_arrow([(1, 5)], [(0, 6), (1, 7)])
    puzzle.add_arrow([(8, 7)], [(8, 8), (7, 8)])
    puzzle.add_arrow([(7, 3)], [(7, 4), (8, 4)])
    puzzle.add_arrow([(1, 3)], [(2, 3), (1, 2)])
    puzzle.add_arrow([(3, 1)], [(2, 0), (1, 0)])
    puzzle.add_arrow([(2, 8)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (3, 4)])
    puzzle.add_arrow([(5, 7)], [(5, 8), (6, 8), (7, 7)])

    return puzzle
