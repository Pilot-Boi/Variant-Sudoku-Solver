"""PuzzleMadness Between Lines Sudoku — 2025-09-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 3, 5, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 8],
        [0, 3, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 4, 2, 0, 5],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 7, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 6), (6, 5), (5, 4), (4, 5), (3, 4), (3, 5)])
    puzzle.add_between_line([(0, 0), (1, 1), (0, 1), (1, 2), (2, 2)])
    puzzle.add_between_line([(8, 7), (7, 6), (7, 5), (8, 6), (8, 5)])
    puzzle.add_between_line([(1, 3), (2, 4), (1, 5), (0, 6), (1, 6)])
    puzzle.add_between_line([(7, 2), (6, 1), (5, 2), (4, 3)])
    puzzle.add_between_line([(4, 6), (3, 6), (4, 7), (5, 8)])
    puzzle.add_between_line([(7, 3), (7, 4), (8, 4), (8, 3)])
    puzzle.add_between_line([(4, 0), (5, 1), (4, 2), (3, 1)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 7)])
    puzzle.add_between_line([(4, 8), (3, 7), (3, 8)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 4)])
    puzzle.add_between_line([(1, 0), (2, 1), (3, 2)])

    return puzzle
