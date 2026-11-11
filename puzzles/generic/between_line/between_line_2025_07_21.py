"""PuzzleMadness Between Lines Sudoku — 2025-07-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [5, 2, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 7, 0, 0],
        [6, 0, 0, 0, 0, 7, 5, 2, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 3), (8, 2), (7, 3), (6, 3), (5, 2), (4, 2)])
    puzzle.add_between_line([(6, 5), (6, 6), (7, 6), (6, 7), (6, 8)])
    puzzle.add_between_line([(5, 3), (6, 4), (7, 5), (8, 6), (7, 7)])
    puzzle.add_between_line([(6, 2), (5, 1), (6, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(3, 8), (4, 8), (5, 8), (4, 7)])
    puzzle.add_between_line([(5, 4), (4, 5), (4, 4), (3, 4)])
    puzzle.add_between_line([(2, 3), (3, 2), (2, 2), (1, 1)])
    puzzle.add_between_line([(0, 8), (1, 8), (2, 8), (2, 7)])
    puzzle.add_between_line([(1, 3), (0, 4), (1, 5)])
    puzzle.add_between_line([(3, 0), (4, 0), (3, 1)])
    puzzle.add_between_line([(4, 6), (3, 7), (2, 6)])

    return puzzle
