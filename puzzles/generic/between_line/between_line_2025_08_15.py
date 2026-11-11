"""PuzzleMadness Between Lines Sudoku — 2025-08-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 2, 0, 0, 0, 9, 0],
        [7, 3, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 2, 0, 0, 4, 0, 0, 5, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 4), (1, 4), (1, 3), (0, 3), (1, 2), (2, 2)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 4), (5, 5), (4, 5)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(4, 7), (4, 6), (3, 7), (4, 8), (5, 8)])
    puzzle.add_between_line([(6, 0), (6, 1), (5, 0), (4, 1)])
    puzzle.add_between_line([(5, 1), (4, 2), (3, 3), (4, 4)])
    puzzle.add_between_line([(8, 3), (8, 4), (8, 5), (7, 5)])
    puzzle.add_between_line([(5, 4), (6, 3), (5, 2)])
    puzzle.add_between_line([(6, 7), (7, 6), (6, 6)])
    puzzle.add_between_line([(0, 2), (1, 1), (0, 1)])
    puzzle.add_between_line([(2, 7), (1, 7), (0, 7)])

    return puzzle
