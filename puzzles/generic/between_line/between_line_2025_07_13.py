"""PuzzleMadness Between Lines Sudoku — 2025-07-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 2, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 3, 0, 9, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 4), (8, 3), (7, 2), (6, 1), (6, 0), (5, 1)])
    puzzle.add_between_line([(7, 6), (7, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_between_line([(2, 4), (3, 3), (3, 2), (2, 1), (1, 0)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 5), (7, 4), (6, 4)])
    puzzle.add_between_line([(2, 2), (1, 3), (0, 2), (0, 1), (1, 2)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 7), (2, 7)])
    puzzle.add_between_line([(3, 4), (4, 5), (4, 6), (5, 6)])
    puzzle.add_between_line([(2, 6), (1, 6), (1, 5), (0, 5)])
    puzzle.add_between_line([(5, 7), (4, 7), (4, 8), (3, 7)])
    puzzle.add_between_line([(0, 4), (1, 4), (0, 3)])
    puzzle.add_between_line([(6, 6), (5, 5), (5, 4)])
    puzzle.add_between_line([(5, 0), (4, 1), (4, 2)])

    return puzzle
