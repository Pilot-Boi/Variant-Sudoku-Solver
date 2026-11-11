"""PuzzleMadness Between Lines Sudoku — 2025-01-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 8, 0, 3, 0, 6, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 6, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 1, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 2, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 0), (7, 0), (8, 1), (7, 2), (6, 1), (5, 0)])
    puzzle.add_between_line([(4, 6), (4, 7), (5, 7), (6, 7), (7, 6)])
    puzzle.add_between_line([(2, 1), (2, 2), (3, 1), (4, 1), (5, 2)])
    puzzle.add_between_line([(3, 3), (3, 2), (4, 2), (4, 3), (3, 4)])
    puzzle.add_between_line([(5, 6), (6, 5), (5, 5), (6, 4)])
    puzzle.add_between_line([(6, 3), (6, 2), (5, 1), (4, 0)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 8), (4, 8)])
    puzzle.add_between_line([(1, 3), (2, 4), (1, 4)])
    puzzle.add_between_line([(8, 4), (8, 3), (7, 4)])
    puzzle.add_between_line([(8, 5), (7, 5), (6, 6)])
    puzzle.add_between_line([(8, 7), (7, 7), (8, 6)])

    return puzzle
