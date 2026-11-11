"""PuzzleMadness Between Lines Sudoku — 2025-09-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 4, 0, 0, 0, 0],
        [0, 0, 1, 0, 9, 0, 0, 0, 2],
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 3), (5, 2), (6, 3), (7, 2), (8, 3), (7, 4)])
    puzzle.add_between_line([(0, 2), (1, 2), (1, 1), (1, 0), (2, 1)])
    puzzle.add_between_line([(2, 2), (3, 3), (2, 4), (1, 4), (0, 3)])
    puzzle.add_between_line([(2, 6), (2, 7), (1, 6), (0, 6), (1, 7)])
    puzzle.add_between_line([(7, 8), (7, 7), (6, 6), (5, 5)])
    puzzle.add_between_line([(1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_between_line([(6, 2), (6, 1), (5, 1), (5, 0)])
    puzzle.add_between_line([(8, 8), (8, 7), (7, 6), (8, 6)])
    puzzle.add_between_line([(7, 1), (7, 0), (8, 1)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 2)])
    puzzle.add_between_line([(4, 2), (3, 1), (4, 1)])

    return puzzle
