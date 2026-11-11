"""PuzzleMadness Between Lines Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 6, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 8],
        [1, 0, 2, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 3, 0, 9, 0],
        [0, 0, 0, 0, 6, 0, 3, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (5, 2), (6, 2), (7, 2), (7, 1), (6, 0)])
    puzzle.add_between_line([(1, 2), (2, 2), (1, 3), (2, 3), (3, 2)])
    puzzle.add_between_line([(6, 6), (7, 6), (6, 7), (6, 8), (7, 8)])
    puzzle.add_between_line([(4, 1), (4, 0), (3, 1), (2, 1), (1, 1)])
    puzzle.add_between_line([(4, 8), (3, 8), (2, 7), (2, 6), (3, 7)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 1), (0, 0)])
    puzzle.add_between_line([(8, 5), (7, 4), (8, 4), (8, 3)])
    puzzle.add_between_line([(0, 5), (1, 5), (2, 4), (1, 4)])
    puzzle.add_between_line([(6, 1), (5, 0), (5, 1)])
    puzzle.add_between_line([(8, 0), (7, 0), (8, 1)])
    puzzle.add_between_line([(6, 5), (6, 4), (7, 5)])

    return puzzle
