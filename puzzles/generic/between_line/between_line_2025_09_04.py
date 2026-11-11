"""PuzzleMadness Between Lines Sudoku — 2025-09-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 6, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 3, 0, 0, 9, 6, 0],
        [0, 1, 8, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 8, 0, 0, 2],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (6, 1), (7, 0), (8, 1), (7, 1), (8, 2)])
    puzzle.add_between_line([(2, 5), (3, 4), (2, 3), (1, 2), (0, 1)])
    puzzle.add_between_line([(1, 3), (0, 2), (0, 3), (1, 4), (2, 4)])
    puzzle.add_between_line([(6, 7), (6, 6), (5, 7), (4, 7), (3, 8)])
    puzzle.add_between_line([(2, 1), (3, 1), (4, 2), (3, 3), (4, 3)])
    puzzle.add_between_line([(0, 8), (1, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(7, 5), (7, 6), (7, 7), (8, 7)])
    puzzle.add_between_line([(0, 6), (1, 6), (0, 5), (0, 4)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0)])
    puzzle.add_between_line([(6, 3), (5, 2), (4, 1)])
    puzzle.add_between_line([(6, 8), (7, 8), (8, 8)])

    return puzzle
