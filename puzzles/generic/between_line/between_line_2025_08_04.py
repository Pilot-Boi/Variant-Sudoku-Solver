"""PuzzleMadness Between Lines Sudoku — 2025-08-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 2, 0, 0, 9, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 9],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 7, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 3],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 1, 0, 7, 0, 0, 3, 0],
        [6, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 1), (5, 1), (6, 1), (7, 1), (7, 0), (8, 1)])
    puzzle.add_between_line([(2, 1), (1, 0), (1, 1), (2, 2), (3, 2)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 3), (4, 2), (5, 3)])
    puzzle.add_between_line([(8, 6), (7, 6), (6, 5), (5, 6), (4, 7)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 7), (2, 8), (1, 8)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4), (7, 5)])
    puzzle.add_between_line([(3, 4), (2, 4), (1, 5), (0, 6)])
    puzzle.add_between_line([(6, 3), (7, 3), (7, 2), (6, 2)])
    puzzle.add_between_line([(1, 4), (2, 3), (1, 2), (0, 3)])
    puzzle.add_between_line([(1, 6), (2, 6), (3, 6)])
    puzzle.add_between_line([(6, 7), (6, 8), (5, 8)])
    puzzle.add_between_line([(4, 0), (3, 1), (3, 0)])

    return puzzle
