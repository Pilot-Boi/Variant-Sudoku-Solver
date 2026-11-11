"""PuzzleMadness Between Lines Sudoku — 2025-03-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 5, 4, 0],
        [0, 0, 7, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 7],
        [0, 0, 4, 0, 5, 0, 0, 3, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 5, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 5), (1, 4), (1, 5), (0, 6), (0, 7), (1, 6)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4), (7, 5), (6, 4)])
    puzzle.add_between_line([(4, 3), (3, 4), (2, 3), (3, 2), (3, 1)])
    puzzle.add_between_line([(1, 8), (2, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_between_line([(0, 1), (0, 2), (1, 1), (0, 0)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1), (2, 2)])
    puzzle.add_between_line([(6, 6), (5, 5), (4, 6), (3, 7)])
    puzzle.add_between_line([(4, 4), (3, 5), (2, 6), (2, 5)])
    puzzle.add_between_line([(5, 6), (6, 7), (7, 8)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 1)])
    puzzle.add_between_line([(7, 6), (8, 7), (8, 8)])
    puzzle.add_between_line([(4, 5), (5, 4), (6, 5)])

    return puzzle
