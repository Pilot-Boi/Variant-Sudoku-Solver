"""PuzzleMadness Between Lines Sudoku — 2025-09-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 5, 0, 2, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 1, 0],
        [8, 0, 0, 0, 0, 0, 3, 0, 7],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (5, 2), (5, 1), (5, 0), (6, 1), (6, 2)])
    puzzle.add_between_line([(1, 2), (2, 1), (3, 2), (3, 3), (4, 3)])
    puzzle.add_between_line([(6, 8), (7, 7), (8, 6), (8, 7), (7, 8)])
    puzzle.add_between_line([(6, 6), (6, 7), (7, 6), (7, 5), (6, 5)])
    puzzle.add_between_line([(0, 7), (1, 7), (2, 8), (3, 7), (2, 7)])
    puzzle.add_between_line([(0, 5), (0, 4), (1, 3), (0, 3)])
    puzzle.add_between_line([(5, 4), (5, 3), (4, 2), (4, 1)])
    puzzle.add_between_line([(3, 5), (4, 6), (5, 5), (4, 4)])
    puzzle.add_between_line([(4, 7), (4, 8), (3, 8)])
    puzzle.add_between_line([(2, 6), (1, 6), (0, 6)])
    puzzle.add_between_line([(1, 4), (2, 3), (2, 4)])

    return puzzle
