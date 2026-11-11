"""PuzzleMadness Arrow Sudoku — 2025-10-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Arrow Sudoku — 2025-10-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/arrowsudoku/hard/2025/10/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 9, 0, 0],
        [0, 1, 0, 8, 6, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_arrow([(7, 4)], [(6, 4), (5, 3), (6, 3), (7, 2)])
    puzzle.add_arrow([(6, 7)], [(7, 7), (6, 6), (5, 7)])
    puzzle.add_arrow([(4, 2)], [(3, 2), (3, 1), (3, 0)])
    puzzle.add_arrow([(7, 0)], [(8, 0), (7, 1), (8, 2)])
    puzzle.add_arrow([(6, 8)], [(5, 8), (4, 7), (3, 7)])
    puzzle.add_arrow([(0, 2)], [(1, 1), (2, 2)])
    puzzle.add_arrow([(5, 4)], [(4, 4), (5, 5)])
    puzzle.add_arrow([(6, 2)], [(5, 1), (6, 0)])
    puzzle.add_arrow([(3, 3)], [(2, 3), (1, 4)])
    puzzle.add_arrow([(4, 6)], [(3, 5), (2, 4)])
    puzzle.add_arrow([(8, 5)], [(8, 6), (8, 7)])
    puzzle.add_arrow([(0, 7)], [(1, 8), (0, 8)])
    puzzle.add_arrow([(2, 6)], [(1, 7), (0, 6)])
    puzzle.add_arrow([(0, 5)], [(1, 5), (2, 5)])
    puzzle.add_arrow([(5, 6)], [(6, 5), (7, 5)])
    puzzle.add_arrow([(1, 2)], [(2, 1), (1, 0), (2, 0)])

    return puzzle
