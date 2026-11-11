"""PuzzleMadness Between Lines Sudoku — 2025-06-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 9, 7],
        [9, 7, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 8, 9, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 8), (6, 8), (5, 8), (6, 7), (7, 7), (7, 6)])
    puzzle.add_between_line([(6, 6), (5, 5), (4, 4), (5, 3), (6, 3)])
    puzzle.add_between_line([(2, 7), (2, 6), (3, 6), (4, 7), (3, 7)])
    puzzle.add_between_line([(2, 2), (3, 2), (3, 1), (2, 1), (1, 0)])
    puzzle.add_between_line([(4, 6), (5, 6), (5, 7), (4, 8)])
    puzzle.add_between_line([(1, 7), (1, 6), (0, 5), (0, 6)])
    puzzle.add_between_line([(4, 2), (5, 1), (6, 2), (6, 1)])
    puzzle.add_between_line([(8, 5), (7, 4), (8, 3)])
    puzzle.add_between_line([(2, 3), (1, 2), (0, 1)])
    puzzle.add_between_line([(0, 8), (1, 8), (0, 7)])

    return puzzle
