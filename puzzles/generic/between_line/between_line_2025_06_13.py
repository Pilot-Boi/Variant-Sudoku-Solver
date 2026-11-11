"""PuzzleMadness Between Lines Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [7, 0, 0, 4, 0, 9, 0, 0, 0],
        [4, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [2, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 7, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 4), (2, 5), (3, 5), (4, 5), (3, 6), (4, 6)])
    puzzle.add_between_line([(5, 6), (5, 7), (6, 8), (7, 7), (8, 8)])
    puzzle.add_between_line([(6, 7), (6, 6), (6, 5), (5, 5), (6, 4)])
    puzzle.add_between_line([(8, 4), (7, 3), (8, 2), (7, 1), (8, 0)])
    puzzle.add_between_line([(5, 4), (6, 3), (5, 3), (5, 2)])
    puzzle.add_between_line([(3, 0), (3, 1), (4, 2), (3, 3)])
    puzzle.add_between_line([(1, 6), (2, 7), (3, 8), (4, 7)])
    puzzle.add_between_line([(8, 6), (8, 5), (7, 5)])
    puzzle.add_between_line([(2, 1), (1, 0), (2, 0)])
    puzzle.add_between_line([(6, 2), (7, 2), (6, 1)])
    puzzle.add_between_line([(4, 3), (4, 4), (3, 4)])

    return puzzle
