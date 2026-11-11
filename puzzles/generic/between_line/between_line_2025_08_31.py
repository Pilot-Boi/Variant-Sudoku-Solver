"""PuzzleMadness Between Lines Sudoku — 2025-08-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 4],
        [6, 0, 0, 3, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 8), (7, 8), (6, 8), (5, 7), (6, 7), (7, 6)])
    puzzle.add_between_line([(4, 1), (5, 1), (4, 2), (4, 3), (3, 4)])
    puzzle.add_between_line([(5, 2), (6, 1), (6, 2), (6, 3), (5, 3)])
    puzzle.add_between_line([(3, 7), (4, 7), (3, 6), (3, 5), (4, 5)])
    puzzle.add_between_line([(0, 6), (1, 7), (2, 7), (1, 6), (0, 5)])
    puzzle.add_between_line([(4, 6), (5, 5), (5, 4), (6, 5)])
    puzzle.add_between_line([(2, 3), (2, 2), (1, 1), (1, 2)])
    puzzle.add_between_line([(7, 3), (7, 4), (7, 5), (8, 5)])
    puzzle.add_between_line([(2, 4), (3, 3), (3, 2), (2, 1)])
    puzzle.add_between_line([(0, 1), (0, 2), (1, 3)])
    puzzle.add_between_line([(3, 0), (4, 0), (5, 0)])
    puzzle.add_between_line([(1, 8), (0, 7), (0, 8)])

    return puzzle
