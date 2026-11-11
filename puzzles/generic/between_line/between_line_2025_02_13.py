"""PuzzleMadness Between Lines Sudoku — 2025-02-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 7, 5, 0, 2, 0, 0, 0],
        [0, 0, 0, 7, 9, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 4, 2, 0, 0, 0, 0],
        [1, 0, 9, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 5), (1, 4), (1, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_between_line([(5, 6), (4, 7), (5, 8), (5, 7), (6, 8)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 8), (2, 7), (3, 7)])
    puzzle.add_between_line([(4, 1), (4, 2), (5, 3), (4, 4), (4, 5)])
    puzzle.add_between_line([(6, 5), (7, 4), (8, 4), (7, 3), (6, 4)])
    puzzle.add_between_line([(8, 0), (7, 1), (7, 2), (6, 3)])
    puzzle.add_between_line([(5, 5), (6, 6), (6, 7), (7, 7)])
    puzzle.add_between_line([(1, 0), (1, 1), (2, 1), (2, 2)])
    puzzle.add_between_line([(2, 5), (2, 6), (3, 5), (4, 6)])
    puzzle.add_between_line([(4, 0), (5, 0), (6, 1)])
    puzzle.add_between_line([(8, 5), (8, 6), (7, 6)])
    puzzle.add_between_line([(5, 1), (6, 2), (5, 2)])
    puzzle.add_between_line([(3, 2), (4, 3), (3, 3)])

    return puzzle
