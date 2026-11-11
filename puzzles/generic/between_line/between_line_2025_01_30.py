"""PuzzleMadness Between Lines Sudoku — 2025-01-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 7, 9, 4, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [3, 0, 0, 0, 0, 9, 0, 0, 0],
        [5, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 4, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 6), (7, 5), (8, 6), (7, 7), (6, 7), (5, 7)])
    puzzle.add_between_line([(0, 7), (0, 6), (0, 5), (1, 4), (2, 4)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 4), (5, 3), (5, 2)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0), (4, 0), (4, 1)])
    puzzle.add_between_line([(0, 2), (1, 2), (2, 2), (3, 2)])
    puzzle.add_between_line([(5, 8), (4, 7), (3, 7), (2, 7)])
    puzzle.add_between_line([(2, 3), (3, 4), (3, 3), (4, 4)])
    puzzle.add_between_line([(0, 0), (1, 1), (0, 1)])
    puzzle.add_between_line([(5, 1), (5, 0), (6, 0)])
    puzzle.add_between_line([(5, 6), (6, 5), (7, 4)])
    puzzle.add_between_line([(2, 6), (1, 6), (1, 7)])

    return puzzle
