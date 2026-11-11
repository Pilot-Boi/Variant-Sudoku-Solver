"""PuzzleMadness Between Lines Sudoku — 2025-08-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 8, 0, 0, 3, 0, 0],
        [1, 0, 0, 6, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 7],
        [9, 0, 3, 0, 8, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 3), (5, 3), (4, 4), (5, 4), (6, 5), (6, 4)])
    puzzle.add_between_line([(5, 2), (4, 1), (3, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(8, 8), (7, 7), (7, 8), (6, 7), (5, 8)])
    puzzle.add_between_line([(7, 0), (6, 0), (6, 1), (7, 2), (8, 1)])
    puzzle.add_between_line([(6, 6), (5, 5), (4, 6), (4, 5)])
    puzzle.add_between_line([(3, 3), (2, 3), (1, 4), (2, 4)])
    puzzle.add_between_line([(2, 2), (1, 1), (0, 1), (0, 2)])
    puzzle.add_between_line([(1, 2), (0, 3), (0, 4), (1, 3)])
    puzzle.add_between_line([(8, 3), (7, 3), (7, 4)])
    puzzle.add_between_line([(1, 5), (1, 6), (2, 7)])
    puzzle.add_between_line([(4, 7), (3, 6), (3, 5)])
    puzzle.add_between_line([(5, 6), (5, 7), (4, 8)])

    return puzzle
