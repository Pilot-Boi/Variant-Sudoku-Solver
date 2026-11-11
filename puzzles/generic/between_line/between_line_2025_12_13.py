"""PuzzleMadness Between Lines Sudoku — 2025-12-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 1, 0, 0, 0, 8, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 7],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 6, 0, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 3), (3, 2), (2, 1), (3, 0), (4, 1), (4, 2)])
    puzzle.add_between_line([(1, 2), (0, 1), (0, 2), (1, 3), (1, 4)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 5), (0, 6), (1, 6)])
    puzzle.add_between_line([(7, 3), (7, 4), (8, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(8, 2), (7, 1), (7, 0), (8, 1)])
    puzzle.add_between_line([(7, 2), (6, 2), (5, 2), (4, 3)])
    puzzle.add_between_line([(2, 6), (3, 7), (4, 7), (5, 7)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 6)])
    puzzle.add_between_line([(2, 2), (1, 1), (1, 0)])
    puzzle.add_between_line([(6, 7), (5, 6), (5, 5)])

    return puzzle
