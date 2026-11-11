"""PuzzleMadness Between Lines Sudoku — 2025-07-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 8, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 5, 2, 0],
        [0, 1, 2, 0, 0, 0, 0, 8, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 4, 0, 0, 0, 0, 0, 0],
        [0, 7, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 4), (2, 5), (3, 4), (3, 5), (2, 6), (1, 5)])
    puzzle.add_between_line([(4, 1), (4, 2), (5, 1), (4, 0), (5, 0)])
    puzzle.add_between_line([(7, 0), (8, 1), (8, 2), (7, 3), (8, 3)])
    puzzle.add_between_line([(7, 4), (6, 5), (6, 4), (5, 3), (6, 3)])
    puzzle.add_between_line([(5, 8), (4, 7), (4, 6), (3, 6)])
    puzzle.add_between_line([(7, 1), (6, 1), (6, 2), (5, 2)])
    puzzle.add_between_line([(5, 6), (6, 7), (7, 6), (8, 6)])
    puzzle.add_between_line([(6, 6), (7, 5), (8, 4)])
    puzzle.add_between_line([(0, 6), (1, 6), (0, 7)])
    puzzle.add_between_line([(4, 8), (3, 7), (3, 8)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 3)])

    return puzzle
