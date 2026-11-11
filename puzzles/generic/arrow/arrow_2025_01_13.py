"""PuzzleMadness Arrow Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [4, 0, 0, 0, 0, 7, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 3)], [(1, 2), (2, 2), (2, 1)])
    puzzle.add_arrow([(4, 6)], [(5, 7), (6, 8)])
    puzzle.add_arrow([(6, 4)], [(5, 3), (4, 2)])
    puzzle.add_arrow([(2, 6)], [(2, 7), (3, 7)])
    puzzle.add_arrow([(7, 4)], [(6, 5), (5, 6)])
    puzzle.add_arrow([(3, 6)], [(4, 5), (4, 4)])
    puzzle.add_arrow([(7, 3)], [(7, 2), (6, 1)])
    puzzle.add_arrow([(2, 3)], [(1, 4), (0, 4), (0, 3)])
    puzzle.add_arrow([(5, 0)], [(4, 0), (3, 0), (3, 1)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (8, 7)])
    puzzle.add_arrow([(2, 8)], [(1, 7), (0, 6), (0, 5)])
    puzzle.add_arrow([(8, 1)], [(7, 1), (6, 2)])
    puzzle.add_arrow([(6, 7)], [(5, 8), (4, 7), (3, 8)])
    puzzle.add_arrow([(3, 3)], [(3, 2), (4, 3)])
    puzzle.add_arrow([(5, 4)], [(6, 3), (5, 2)])
    puzzle.add_arrow([(7, 7)], [(7, 6), (7, 5)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (2, 0)])
    puzzle.add_arrow([(0, 8)], [(0, 7), (1, 6)])

    return puzzle
