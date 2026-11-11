"""PuzzleMadness Between Lines Sudoku — 2025-11-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 8, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 6, 0, 0, 5, 0, 0, 0, 9],
        [9, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 8), (0, 7), (1, 7), (2, 7), (3, 6), (4, 7)])
    puzzle.add_between_line([(4, 6), (5, 5), (5, 6), (6, 6), (5, 7)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 6), (7, 7), (6, 8)])
    puzzle.add_between_line([(8, 5), (7, 6), (7, 5), (6, 5), (7, 4)])
    puzzle.add_between_line([(7, 1), (6, 2), (5, 1), (4, 0), (5, 0)])
    puzzle.add_between_line([(7, 2), (8, 3), (8, 4), (7, 3)])
    puzzle.add_between_line([(0, 3), (1, 2), (2, 3), (3, 4)])
    puzzle.add_between_line([(5, 4), (4, 3), (5, 2), (5, 3)])
    puzzle.add_between_line([(4, 8), (3, 7), (3, 8)])
    puzzle.add_between_line([(1, 3), (2, 4), (2, 5)])
    puzzle.add_between_line([(3, 1), (4, 2), (3, 2)])

    return puzzle
