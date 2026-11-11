"""PuzzleMadness Between Lines Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 6, 0, 8, 0, 0, 0, 0, 3],
        [0, 1, 0, 0, 3, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 5, 0, 0, 0, 0, 7],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 7, 9],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 4), (0, 4), (0, 3), (0, 2), (1, 2), (2, 2)])
    puzzle.add_between_line([(2, 0), (3, 0), (4, 1), (5, 0), (4, 0)])
    puzzle.add_between_line([(6, 4), (5, 5), (5, 4), (4, 5), (3, 4)])
    puzzle.add_between_line([(8, 3), (8, 4), (7, 5), (8, 6), (8, 7)])
    puzzle.add_between_line([(5, 1), (6, 0), (6, 1), (5, 2)])
    puzzle.add_between_line([(1, 5), (2, 6), (3, 7), (4, 6)])
    puzzle.add_between_line([(3, 3), (4, 3), (5, 3), (6, 2)])
    puzzle.add_between_line([(6, 7), (7, 7), (8, 8), (7, 8)])
    puzzle.add_between_line([(0, 7), (1, 7), (0, 8)])
    puzzle.add_between_line([(3, 2), (2, 3), (2, 4)])
    puzzle.add_between_line([(8, 1), (8, 2), (7, 1)])
    puzzle.add_between_line([(2, 8), (2, 7), (1, 8)])

    return puzzle
