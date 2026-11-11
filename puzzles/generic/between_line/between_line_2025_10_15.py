"""PuzzleMadness Between Lines Sudoku — 2025-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 6, 1, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 8, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 1), (2, 1), (3, 1), (4, 2), (4, 3), (5, 4)])
    puzzle.add_between_line([(8, 6), (7, 7), (6, 6), (6, 7), (7, 8)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 4), (7, 3), (8, 2)])
    puzzle.add_between_line([(5, 3), (5, 2), (6, 2), (7, 1), (6, 1)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_between_line([(2, 3), (3, 3), (3, 4), (4, 5)])
    puzzle.add_between_line([(2, 4), (2, 5), (3, 5), (3, 6)])
    puzzle.add_between_line([(2, 8), (1, 7), (0, 6), (1, 6)])
    puzzle.add_between_line([(7, 0), (6, 0), (5, 1)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7)])
    puzzle.add_between_line([(2, 6), (1, 5), (0, 4)])

    return puzzle
