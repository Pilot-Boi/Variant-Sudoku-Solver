"""PuzzleMadness Between Lines Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 5, 1, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 9],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 9, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 0), (6, 1), (5, 1), (4, 1), (3, 1), (4, 0)])
    puzzle.add_between_line([(7, 8), (6, 7), (5, 6), (4, 7), (3, 6)])
    puzzle.add_between_line([(0, 7), (1, 7), (0, 6), (0, 5), (1, 6)])
    puzzle.add_between_line([(2, 5), (2, 6), (3, 7), (4, 8), (5, 8)])
    puzzle.add_between_line([(7, 6), (7, 5), (6, 5), (6, 6)])
    puzzle.add_between_line([(4, 2), (5, 2), (6, 2), (7, 2)])
    puzzle.add_between_line([(4, 3), (3, 3), (4, 4), (5, 3)])
    puzzle.add_between_line([(0, 1), (1, 1), (1, 2), (0, 2)])
    puzzle.add_between_line([(5, 4), (4, 5), (3, 5)])
    puzzle.add_between_line([(7, 3), (8, 2), (8, 3)])
    puzzle.add_between_line([(0, 4), (0, 3), (1, 4)])
    puzzle.add_between_line([(2, 3), (2, 4), (1, 5)])

    return puzzle
