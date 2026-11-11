"""PuzzleMadness Between Lines Sudoku — 2025-05-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 8, 0, 0, 6, 0, 0, 0, 2],
        [0, 0, 6, 0, 0, 4, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 5, 0],
        [0, 0, 4, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 5), (3, 5), (4, 4), (5, 5), (4, 6), (4, 5)])
    puzzle.add_between_line([(1, 7), (1, 8), (2, 7), (3, 6), (3, 7)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4), (1, 3), (2, 4)])
    puzzle.add_between_line([(2, 1), (1, 0), (0, 0), (0, 1), (1, 1)])
    puzzle.add_between_line([(1, 2), (2, 2), (3, 3), (3, 4)])
    puzzle.add_between_line([(8, 5), (7, 4), (6, 3), (5, 2)])
    puzzle.add_between_line([(5, 7), (6, 7), (7, 7), (7, 6)])
    puzzle.add_between_line([(2, 8), (3, 8), (4, 7), (4, 8)])
    puzzle.add_between_line([(8, 8), (8, 7), (7, 8)])
    puzzle.add_between_line([(8, 1), (7, 0), (6, 0)])
    puzzle.add_between_line([(5, 0), (5, 1), (4, 2)])

    return puzzle
