"""PuzzleMadness Between Lines Sudoku — 2025-11-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 4, 1, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 8, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 4), (8, 5), (8, 6), (7, 6), (6, 5), (5, 6)])
    puzzle.add_between_line([(7, 3), (6, 2), (6, 1), (5, 2), (5, 1)])
    puzzle.add_between_line([(5, 7), (4, 6), (3, 7), (3, 6), (4, 5)])
    puzzle.add_between_line([(4, 0), (4, 1), (4, 2), (4, 3), (3, 3)])
    puzzle.add_between_line([(1, 5), (0, 4), (0, 3), (1, 3), (2, 4)])
    puzzle.add_between_line([(5, 0), (6, 0), (7, 0), (7, 1)])
    puzzle.add_between_line([(0, 5), (0, 6), (1, 7), (0, 8)])
    puzzle.add_between_line([(7, 8), (8, 7), (7, 7), (6, 8)])
    puzzle.add_between_line([(6, 7), (5, 8), (4, 8)])
    puzzle.add_between_line([(5, 5), (6, 4), (5, 4)])
    puzzle.add_between_line([(2, 8), (2, 7), (3, 8)])

    return puzzle
