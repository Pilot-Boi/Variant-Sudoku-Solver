"""PuzzleMadness Between Lines Sudoku — 2025-01-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 7, 0, 0, 0, 0, 0],
        [8, 2, 0, 6, 0, 0, 1, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 2, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 5), (3, 4), (3, 5), (4, 6), (3, 6), (4, 7)])
    puzzle.add_between_line([(1, 7), (1, 8), (2, 7), (2, 6), (1, 6)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 0), (6, 1), (6, 2)])
    puzzle.add_between_line([(7, 6), (6, 7), (6, 8), (7, 8), (7, 7)])
    puzzle.add_between_line([(7, 5), (8, 4), (7, 3), (7, 2)])
    puzzle.add_between_line([(1, 1), (2, 1), (3, 0), (4, 1)])
    puzzle.add_between_line([(5, 3), (4, 3), (5, 2), (6, 3)])
    puzzle.add_between_line([(5, 1), (5, 0), (4, 0)])
    puzzle.add_between_line([(0, 2), (1, 3), (0, 3)])
    puzzle.add_between_line([(0, 6), (0, 5), (0, 4)])
    puzzle.add_between_line([(5, 8), (4, 8), (3, 7)])

    return puzzle
