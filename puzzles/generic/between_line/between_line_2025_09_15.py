"""PuzzleMadness Between Lines Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 3, 4, 0, 0, 0, 0],
        [1, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 3, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 3), (4, 4), (3, 3), (2, 2), (3, 1), (2, 1)])
    puzzle.add_between_line([(2, 7), (3, 6), (2, 6), (1, 6), (0, 7)])
    puzzle.add_between_line([(6, 3), (6, 2), (5, 1), (4, 1), (3, 0)])
    puzzle.add_between_line([(5, 5), (4, 6), (4, 7), (5, 7), (5, 8)])
    puzzle.add_between_line([(8, 8), (7, 8), (7, 7), (8, 6)])
    puzzle.add_between_line([(2, 8), (1, 8), (1, 7), (0, 8)])
    puzzle.add_between_line([(4, 5), (5, 4), (6, 5), (5, 6)])
    puzzle.add_between_line([(4, 3), (4, 2), (5, 2)])
    puzzle.add_between_line([(4, 8), (3, 7), (3, 8)])
    puzzle.add_between_line([(2, 4), (2, 5), (3, 4)])
    puzzle.add_between_line([(1, 2), (1, 1), (1, 0)])

    return puzzle
