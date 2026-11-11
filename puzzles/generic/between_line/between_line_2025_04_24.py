"""PuzzleMadness Between Lines Sudoku — 2025-04-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 3, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 5, 4, 6],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 4, 0, 0, 0, 9],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 7), (6, 6), (5, 5), (6, 4), (6, 3), (7, 4)])
    puzzle.add_between_line([(5, 0), (4, 0), (3, 1), (3, 2), (2, 2)])
    puzzle.add_between_line([(4, 3), (5, 3), (5, 4), (4, 4), (3, 5)])
    puzzle.add_between_line([(8, 3), (8, 4), (7, 3), (6, 2), (7, 2)])
    puzzle.add_between_line([(1, 2), (2, 1), (1, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(0, 6), (1, 6), (2, 5), (2, 4)])
    puzzle.add_between_line([(8, 2), (8, 1), (8, 0), (7, 1)])
    puzzle.add_between_line([(0, 8), (1, 8), (2, 7), (1, 7)])
    puzzle.add_between_line([(7, 6), (8, 7), (7, 7), (8, 8)])
    puzzle.add_between_line([(0, 2), (0, 3), (0, 4)])
    puzzle.add_between_line([(2, 3), (1, 4), (0, 5)])
    puzzle.add_between_line([(5, 8), (4, 8), (3, 7)])
    puzzle.add_between_line([(5, 6), (4, 6), (4, 7)])

    return puzzle
