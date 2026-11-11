"""PuzzleMadness Between Lines Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 5, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 6, 2, 0, 8, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 2), (1, 2), (0, 3), (1, 4), (0, 5), (1, 6)])
    puzzle.add_between_line([(6, 5), (5, 6), (6, 6), (7, 6), (7, 5)])
    puzzle.add_between_line([(2, 3), (3, 3), (4, 3), (4, 2), (3, 1)])
    puzzle.add_between_line([(2, 5), (3, 6), (4, 5), (5, 5), (6, 4)])
    puzzle.add_between_line([(0, 0), (1, 1), (2, 1), (1, 0), (2, 0)])
    puzzle.add_between_line([(5, 2), (5, 1), (6, 1), (7, 1)])
    puzzle.add_between_line([(8, 2), (7, 3), (7, 4), (6, 3)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_between_line([(2, 6), (3, 7), (2, 8), (2, 7)])
    puzzle.add_between_line([(6, 2), (7, 2), (8, 1)])
    puzzle.add_between_line([(4, 0), (4, 1), (5, 0)])
    puzzle.add_between_line([(5, 4), (4, 4), (5, 3)])
    puzzle.add_between_line([(6, 0), (7, 0), (8, 0)])

    return puzzle
