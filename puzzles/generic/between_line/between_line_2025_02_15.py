"""PuzzleMadness Between Lines Sudoku — 2025-02-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 8, 0, 0, 0, 3, 0],
        [0, 0, 0, 5, 2, 0, 0, 0, 0],
        [2, 0, 0, 0, 6, 3, 0, 0, 0],
        [0, 7, 0, 1, 0, 8, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 5, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 8), (7, 8), (6, 8), (6, 7), (6, 6), (7, 7)])
    puzzle.add_between_line([(1, 6), (2, 6), (2, 7), (1, 8), (2, 8)])
    puzzle.add_between_line([(6, 1), (5, 1), (5, 2), (4, 2), (3, 1)])
    puzzle.add_between_line([(4, 4), (3, 4), (4, 5), (3, 5), (3, 6)])
    puzzle.add_between_line([(2, 5), (1, 4), (0, 3), (1, 3), (2, 4)])
    puzzle.add_between_line([(0, 4), (1, 5), (0, 5), (0, 6)])
    puzzle.add_between_line([(8, 4), (8, 5), (8, 6), (8, 7)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0), (4, 1)])
    puzzle.add_between_line([(6, 3), (6, 2), (7, 2)])
    puzzle.add_between_line([(1, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(6, 4), (7, 4), (8, 3)])
    puzzle.add_between_line([(3, 8), (3, 7), (4, 7)])

    return puzzle
