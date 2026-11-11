"""PuzzleMadness Between Lines Sudoku — 2025-06-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 8, 0, 0, 0, 6, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 4, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 1, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 5), (8, 6), (7, 7), (8, 8), (7, 8), (6, 8)])
    puzzle.add_between_line([(5, 1), (4, 1), (5, 2), (4, 3), (5, 4)])
    puzzle.add_between_line([(6, 3), (7, 4), (6, 4), (5, 3), (6, 2)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 0), (6, 0), (7, 1)])
    puzzle.add_between_line([(4, 0), (3, 1), (2, 0), (1, 0), (1, 1)])
    puzzle.add_between_line([(5, 6), (5, 5), (4, 6), (5, 7)])
    puzzle.add_between_line([(2, 6), (1, 6), (0, 6), (0, 7)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 7), (2, 7)])
    puzzle.add_between_line([(4, 2), (3, 2), (2, 3), (1, 2)])
    puzzle.add_between_line([(8, 3), (8, 2), (7, 2)])
    puzzle.add_between_line([(6, 7), (6, 6), (6, 5)])
    puzzle.add_between_line([(0, 1), (0, 2), (1, 3)])

    return puzzle
