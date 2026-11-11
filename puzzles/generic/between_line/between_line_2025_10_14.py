"""PuzzleMadness Between Lines Sudoku — 2025-10-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 3, 0, 0],
        [2, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 7, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 1, 0, 0],
        [0, 1, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 1, 0, 8, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 8), (3, 8), (4, 7), (3, 6), (2, 6), (1, 6)])
    puzzle.add_between_line([(2, 2), (1, 3), (2, 3), (1, 4), (0, 5)])
    puzzle.add_between_line([(3, 5), (3, 4), (4, 5), (5, 4), (4, 3)])
    puzzle.add_between_line([(3, 2), (4, 1), (5, 1), (5, 0), (4, 0)])
    puzzle.add_between_line([(0, 2), (1, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(1, 8), (1, 7), (0, 7), (0, 8)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 8), (7, 7)])
    puzzle.add_between_line([(1, 5), (2, 5), (2, 4)])
    puzzle.add_between_line([(3, 0), (2, 1), (1, 2)])
    puzzle.add_between_line([(5, 7), (6, 7), (5, 6)])

    return puzzle
