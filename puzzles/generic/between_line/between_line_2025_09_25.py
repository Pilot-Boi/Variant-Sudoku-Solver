"""PuzzleMadness Between Lines Sudoku — 2025-09-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 2, 3, 0, 0, 4, 0, 0],
        [6, 4, 9, 0, 7, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 4, 7, 0, 0, 0],
        [0, 8, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 1)])
    puzzle.add_between_line([(5, 4), (5, 3), (5, 2), (4, 1), (3, 1)])
    puzzle.add_between_line([(7, 8), (8, 7), (7, 7), (6, 8), (5, 8)])
    puzzle.add_between_line([(6, 0), (6, 1), (5, 1), (4, 0), (5, 0)])
    puzzle.add_between_line([(4, 8), (3, 7), (2, 8), (3, 8)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 6), (0, 7)])
    puzzle.add_between_line([(0, 8), (1, 7), (2, 7), (2, 6)])
    puzzle.add_between_line([(1, 3), (1, 4), (1, 5), (2, 4)])
    puzzle.add_between_line([(1, 2), (2, 1), (3, 0)])
    puzzle.add_between_line([(7, 0), (7, 1), (8, 0)])
    puzzle.add_between_line([(8, 6), (7, 5), (6, 4)])

    return puzzle
