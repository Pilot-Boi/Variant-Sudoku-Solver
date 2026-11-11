"""PuzzleMadness Between Lines Sudoku — 2025-10-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 7, 3, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 6), (7, 6), (7, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_between_line([(2, 7), (2, 6), (1, 7), (2, 8), (3, 7)])
    puzzle.add_between_line([(0, 4), (1, 4), (2, 5), (3, 6), (4, 5)])
    puzzle.add_between_line([(5, 5), (6, 4), (7, 4), (8, 5), (8, 4)])
    puzzle.add_between_line([(5, 7), (6, 6), (6, 7), (5, 8), (6, 8)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 2), (2, 2)])
    puzzle.add_between_line([(5, 0), (6, 1), (7, 0), (6, 0)])
    puzzle.add_between_line([(5, 2), (6, 2), (7, 1), (7, 2)])
    puzzle.add_between_line([(1, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(5, 3), (4, 4), (4, 3)])
    puzzle.add_between_line([(2, 4), (3, 4), (2, 3)])
    puzzle.add_between_line([(2, 0), (3, 0), (4, 0)])

    return puzzle
