"""PuzzleMadness Between Lines Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 9, 8, 0, 0, 0, 0],
        [8, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 4, 0, 0, 1, 7, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [7, 0, 0, 0, 0, 4, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 6), (0, 7), (0, 8), (1, 7), (2, 8), (3, 8)])
    puzzle.add_between_line([(6, 1), (7, 2), (6, 3), (5, 4), (6, 4)])
    puzzle.add_between_line([(5, 3), (6, 2), (5, 2), (4, 1), (5, 0)])
    puzzle.add_between_line([(2, 3), (2, 2), (3, 1), (2, 0), (1, 0)])
    puzzle.add_between_line([(8, 5), (8, 6), (7, 5), (7, 6), (8, 7)])
    puzzle.add_between_line([(0, 1), (1, 1), (2, 1), (1, 2)])
    puzzle.add_between_line([(6, 7), (5, 7), (5, 6), (4, 5)])
    puzzle.add_between_line([(6, 6), (7, 7), (8, 8), (7, 8)])
    puzzle.add_between_line([(2, 7), (3, 6), (2, 5), (2, 4)])
    puzzle.add_between_line([(5, 8), (4, 7), (4, 8)])
    puzzle.add_between_line([(1, 6), (1, 5), (0, 4)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 3)])

    return puzzle
