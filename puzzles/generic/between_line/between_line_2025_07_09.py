"""PuzzleMadness Between Lines Sudoku — 2025-07-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [2, 0, 0, 9, 0, 1, 7, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 2, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 3],
        [0, 0, 0, 0, 5, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (3, 5), (2, 4), (3, 3), (3, 2), (4, 1)])
    puzzle.add_between_line([(8, 7), (8, 6), (7, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(6, 4), (7, 3), (6, 2), (6, 1), (7, 1)])
    puzzle.add_between_line([(6, 7), (6, 6), (5, 5), (4, 4), (4, 3)])
    puzzle.add_between_line([(6, 5), (5, 4), (5, 3), (4, 2), (5, 1)])
    puzzle.add_between_line([(1, 2), (2, 2), (2, 1), (1, 0)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0), (3, 1)])
    puzzle.add_between_line([(4, 7), (3, 6), (3, 7), (2, 8)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(5, 6), (4, 6), (5, 7)])
    puzzle.add_between_line([(1, 6), (1, 7), (2, 7)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 0)])

    return puzzle
