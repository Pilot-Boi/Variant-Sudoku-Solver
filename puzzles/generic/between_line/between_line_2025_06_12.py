"""PuzzleMadness Between Lines Sudoku — 2025-06-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [9, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 1, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 2, 0, 0, 0, 0],
        [0, 4, 0, 7, 5, 9, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 5), (3, 5), (3, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_between_line([(2, 3), (3, 2), (2, 2), (1, 2), (1, 3)])
    puzzle.add_between_line([(7, 1), (6, 0), (7, 0), (8, 1), (8, 0)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 8), (5, 7), (4, 6)])
    puzzle.add_between_line([(1, 6), (0, 6), (0, 7), (1, 7)])
    puzzle.add_between_line([(4, 4), (4, 3), (5, 3), (5, 4)])
    puzzle.add_between_line([(6, 1), (6, 2), (5, 1), (5, 0)])
    puzzle.add_between_line([(6, 7), (5, 6), (6, 6), (6, 5)])
    puzzle.add_between_line([(8, 4), (7, 3), (7, 4)])
    puzzle.add_between_line([(1, 1), (0, 2), (0, 1)])
    puzzle.add_between_line([(8, 7), (7, 7), (8, 8)])
    puzzle.add_between_line([(6, 4), (6, 3), (7, 2)])

    return puzzle
