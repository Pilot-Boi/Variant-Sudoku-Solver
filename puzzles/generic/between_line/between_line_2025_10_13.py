"""PuzzleMadness Between Lines Sudoku — 2025-10-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 9, 0, 5, 2],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 4, 0, 0, 3, 0, 0],
        [8, 6, 0, 0, 7, 0, 0, 0, 0],
        [4, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (1, 5), (2, 4), (2, 3), (3, 3), (4, 2)])
    puzzle.add_between_line([(7, 3), (6, 3), (5, 3), (4, 4), (3, 4)])
    puzzle.add_between_line([(3, 5), (4, 6), (5, 6), (6, 7), (7, 7)])
    puzzle.add_between_line([(7, 1), (6, 2), (5, 2), (6, 1), (5, 0)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_between_line([(5, 7), (4, 7), (3, 7), (2, 7)])
    puzzle.add_between_line([(2, 2), (1, 1), (1, 2), (0, 3)])
    puzzle.add_between_line([(1, 4), (1, 3), (0, 4), (0, 5)])
    puzzle.add_between_line([(7, 4), (7, 5), (7, 6), (6, 5)])
    puzzle.add_between_line([(4, 1), (3, 0), (2, 1)])
    puzzle.add_between_line([(6, 0), (7, 0), (8, 0)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 8)])

    return puzzle
