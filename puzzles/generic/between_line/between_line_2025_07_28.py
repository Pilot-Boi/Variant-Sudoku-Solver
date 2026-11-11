"""PuzzleMadness Between Lines Sudoku — 2025-07-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [4, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 0, 7, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 7, 8, 0, 0, 0, 0, 0, 3],
        [0, 0, 5, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (6, 4), (5, 5), (5, 6), (4, 7), (5, 8)])
    puzzle.add_between_line([(3, 2), (3, 3), (2, 3), (1, 2), (2, 1)])
    puzzle.add_between_line([(6, 1), (7, 1), (7, 2), (8, 3), (8, 4)])
    puzzle.add_between_line([(8, 5), (8, 6), (8, 7), (7, 6), (6, 7)])
    puzzle.add_between_line([(1, 4), (2, 5), (2, 6), (1, 7), (1, 6)])
    puzzle.add_between_line([(4, 2), (5, 3), (5, 4), (4, 4)])
    puzzle.add_between_line([(6, 2), (5, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(2, 4), (3, 4), (4, 5), (3, 5)])
    puzzle.add_between_line([(0, 6), (0, 5), (0, 4)])
    puzzle.add_between_line([(6, 6), (6, 5), (7, 4)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 3)])

    return puzzle
