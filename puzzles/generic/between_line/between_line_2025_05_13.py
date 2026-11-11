"""PuzzleMadness Between Lines Sudoku — 2025-05-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 3, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 6, 2, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 4, 3, 0],
        [0, 7, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 7, 6, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 4)])
    puzzle.add_between_line([(3, 2), (3, 1), (4, 2), (5, 3), (6, 2)])
    puzzle.add_between_line([(7, 3), (7, 4), (6, 4), (6, 5), (7, 5)])
    puzzle.add_between_line([(2, 5), (1, 4), (1, 3), (0, 2), (0, 3)])
    puzzle.add_between_line([(0, 5), (0, 4), (1, 5), (1, 6)])
    puzzle.add_between_line([(4, 0), (5, 1), (5, 0), (6, 1)])
    puzzle.add_between_line([(7, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7)])
    puzzle.add_between_line([(5, 4), (4, 5), (5, 6)])
    puzzle.add_between_line([(0, 0), (1, 0), (1, 1)])
    puzzle.add_between_line([(1, 7), (2, 6), (2, 7)])

    return puzzle
