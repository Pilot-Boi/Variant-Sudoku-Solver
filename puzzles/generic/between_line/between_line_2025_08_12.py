"""PuzzleMadness Between Lines Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 9, 0, 0, 5, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 8), (2, 7), (2, 6), (3, 6), (4, 5), (5, 4)])
    puzzle.add_between_line([(4, 2), (4, 1), (5, 2), (4, 3), (4, 4)])
    puzzle.add_between_line([(2, 5), (2, 4), (1, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(0, 5), (0, 6), (1, 6), (1, 7), (0, 7)])
    puzzle.add_between_line([(1, 0), (0, 1), (0, 2), (0, 3)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 0), (7, 1)])
    puzzle.add_between_line([(2, 1), (3, 0), (3, 1), (3, 2)])
    puzzle.add_between_line([(7, 5), (8, 5), (7, 4), (7, 3)])
    puzzle.add_between_line([(8, 8), (7, 7), (8, 7)])
    puzzle.add_between_line([(7, 8), (6, 7), (5, 7)])
    puzzle.add_between_line([(1, 2), (1, 1), (2, 0)])

    return puzzle
