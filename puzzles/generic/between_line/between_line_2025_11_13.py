"""PuzzleMadness Between Lines Sudoku — 2025-11-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 4, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 4, 8, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 8, 0, 0],
        [0, 6, 0, 0, 2, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (7, 3), (8, 2), (8, 3), (8, 4), (7, 5)])
    puzzle.add_between_line([(0, 6), (1, 7), (1, 6), (2, 5), (3, 4)])
    puzzle.add_between_line([(2, 6), (3, 5), (4, 6), (5, 7), (5, 8)])
    puzzle.add_between_line([(7, 8), (6, 8), (6, 7), (7, 7), (8, 8)])
    puzzle.add_between_line([(1, 5), (0, 4), (1, 3), (1, 2)])
    puzzle.add_between_line([(2, 0), (1, 1), (2, 2), (2, 3)])
    puzzle.add_between_line([(2, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_between_line([(6, 4), (7, 4), (6, 5)])
    puzzle.add_between_line([(8, 1), (7, 0), (7, 1)])
    puzzle.add_between_line([(4, 4), (4, 3), (5, 3)])

    return puzzle
