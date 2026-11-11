"""PuzzleMadness Between Lines Sudoku — 2025-08-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 2, 0, 3],
        [0, 0, 0, 0, 8, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 2), (3, 1), (3, 2), (4, 3), (5, 3), (5, 4)])
    puzzle.add_between_line([(1, 4), (1, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_between_line([(2, 8), (1, 8), (2, 7), (3, 8), (3, 7)])
    puzzle.add_between_line([(2, 1), (1, 1), (0, 2), (1, 2), (2, 3)])
    puzzle.add_between_line([(1, 5), (2, 4), (3, 5), (4, 6)])
    puzzle.add_between_line([(3, 4), (4, 5), (5, 5), (5, 6)])
    puzzle.add_between_line([(2, 5), (3, 6), (4, 7), (5, 8)])
    puzzle.add_between_line([(7, 8), (8, 8), (7, 7), (6, 8)])
    puzzle.add_between_line([(7, 2), (8, 1), (8, 0)])
    puzzle.add_between_line([(6, 2), (5, 1), (4, 1)])
    puzzle.add_between_line([(6, 5), (6, 6), (5, 7)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 1)])

    return puzzle
