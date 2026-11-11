"""PuzzleMadness Arrow Sudoku — 2025-02-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-02-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/2/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [5, 0, 0, 3, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(1, 2)], [(0, 2), (1, 3), (2, 3), (2, 2)])
    puzzle.add_arrow([(6, 5)], [(6, 4), (7, 4)])
    puzzle.add_arrow([(5, 1)], [(5, 0), (6, 0)])
    puzzle.add_arrow([(7, 1)], [(8, 1), (7, 2), (8, 2)])
    puzzle.add_arrow([(7, 6)], [(7, 7), (7, 8), (8, 7)])
    puzzle.add_arrow([(5, 6)], [(4, 6), (5, 5), (4, 5)])
    puzzle.add_arrow([(4, 1)], [(3, 2), (3, 1)])
    puzzle.add_arrow([(2, 8)], [(2, 7), (1, 6), (1, 5)])
    puzzle.add_arrow([(5, 7)], [(6, 6), (6, 7)])
    puzzle.add_arrow([(0, 4)], [(1, 4), (0, 3)])
    puzzle.add_arrow([(4, 7)], [(3, 6), (2, 5)])
    puzzle.add_arrow([(6, 3)], [(5, 3), (5, 4)])
    puzzle.add_arrow([(2, 0)], [(2, 1), (3, 0)])
    puzzle.add_arrow([(1, 0)], [(1, 1), (0, 1)])
    puzzle.add_arrow([(8, 6)], [(7, 5), (8, 5)])
    puzzle.add_arrow([(1, 7)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(6, 2)], [(7, 3), (8, 3)])
    puzzle.add_arrow([(4, 8)], [(3, 7), (2, 6)])
    puzzle.add_arrow([(3, 5)], [(4, 4), (4, 3)])

    return puzzle
