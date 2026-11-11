"""PuzzleMadness Between Lines Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 6],
        [0, 0, 7, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 4, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 1],
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (6, 2), (7, 1), (7, 0), (6, 1), (5, 2)])
    puzzle.add_between_line([(4, 7), (3, 8), (4, 8), (5, 7), (5, 6)])
    puzzle.add_between_line([(6, 8), (6, 7), (6, 6), (7, 6), (7, 7)])
    puzzle.add_between_line([(3, 4), (2, 5), (3, 6), (2, 6), (2, 7)])
    puzzle.add_between_line([(3, 1), (4, 1), (4, 2), (3, 2)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 7), (0, 6)])
    puzzle.add_between_line([(0, 1), (1, 0), (2, 1), (3, 0)])
    puzzle.add_between_line([(2, 4), (1, 4), (1, 5), (0, 4)])
    puzzle.add_between_line([(8, 3), (7, 4), (7, 5)])
    puzzle.add_between_line([(1, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(4, 5), (5, 4), (4, 4)])
    puzzle.add_between_line([(8, 7), (7, 8), (8, 8)])

    return puzzle
