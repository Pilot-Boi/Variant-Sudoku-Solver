"""PuzzleMadness Between Lines Sudoku — 2025-11-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 8, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 9, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 4, 0],
        [2, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 8, 5],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 3), (3, 4), (2, 5), (1, 5), (1, 4), (2, 3)])
    puzzle.add_between_line([(8, 5), (7, 6), (7, 5), (7, 4), (6, 5)])
    puzzle.add_between_line([(4, 5), (5, 6), (4, 6), (3, 7), (3, 8)])
    puzzle.add_between_line([(6, 0), (6, 1), (5, 1), (4, 1), (5, 2)])
    puzzle.add_between_line([(6, 2), (7, 3), (6, 4), (5, 5), (5, 4)])
    puzzle.add_between_line([(2, 6), (1, 7), (2, 8), (1, 8)])
    puzzle.add_between_line([(2, 1), (1, 0), (0, 1), (0, 0)])
    puzzle.add_between_line([(0, 2), (1, 2), (2, 2), (3, 2)])
    puzzle.add_between_line([(6, 3), (5, 3), (4, 2)])
    puzzle.add_between_line([(8, 6), (7, 7), (8, 7)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 8)])
    puzzle.add_between_line([(8, 1), (7, 2), (7, 1)])

    return puzzle
