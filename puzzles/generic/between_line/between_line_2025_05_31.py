"""PuzzleMadness Between Lines Sudoku — 2025-05-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 6, 0],
        [0, 2, 3, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 7, 0, 5, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 7), (3, 7), (3, 6), (2, 6), (1, 5), (0, 4)])
    puzzle.add_between_line([(6, 0), (5, 1), (5, 0), (4, 1), (3, 1)])
    puzzle.add_between_line([(4, 8), (5, 7), (6, 6), (6, 5), (7, 4)])
    puzzle.add_between_line([(4, 2), (3, 2), (3, 3), (4, 3), (4, 4)])
    puzzle.add_between_line([(1, 0), (0, 0), (1, 1), (2, 1)])
    puzzle.add_between_line([(8, 5), (7, 6), (7, 7), (8, 6)])
    puzzle.add_between_line([(4, 5), (4, 6), (3, 5), (3, 4)])
    puzzle.add_between_line([(2, 2), (1, 2), (1, 3), (2, 3)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 8)])
    puzzle.add_between_line([(8, 0), (7, 0), (6, 1)])
    puzzle.add_between_line([(2, 7), (2, 8), (3, 8)])

    return puzzle
