"""PuzzleMadness Arrow Sudoku — 2025-05-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-05-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/5/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(2, 2)], [(1, 1), (2, 0), (3, 1)])
    puzzle.add_arrow([(5, 4)], [(5, 3), (5, 2)])
    puzzle.add_arrow([(8, 6)], [(7, 5), (8, 4), (8, 5), (7, 6)])
    puzzle.add_arrow([(2, 4)], [(1, 4), (2, 5), (3, 4), (3, 3)])
    puzzle.add_arrow([(7, 2)], [(6, 1), (7, 0), (8, 1)])
    puzzle.add_arrow([(5, 7)], [(4, 7), (4, 6), (4, 5)])
    puzzle.add_arrow([(1, 6)], [(1, 5), (0, 6)])
    puzzle.add_arrow([(8, 8)], [(7, 7), (6, 8)])
    puzzle.add_arrow([(4, 1)], [(5, 1), (4, 0)])
    puzzle.add_arrow([(0, 4)], [(1, 3), (0, 2)])
    puzzle.add_arrow([(2, 8)], [(1, 8), (1, 7), (0, 8)])
    puzzle.add_arrow([(5, 5)], [(6, 6), (6, 5)])
    puzzle.add_arrow([(1, 0)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(3, 5)], [(3, 6), (3, 7)])
    puzzle.add_arrow([(7, 4)], [(8, 3), (8, 2)])

    return puzzle
