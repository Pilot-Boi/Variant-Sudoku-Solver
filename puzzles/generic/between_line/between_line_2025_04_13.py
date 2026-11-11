"""PuzzleMadness Between Lines Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 7, 0, 0, 0, 0, 5],
        [0, 7, 9, 0, 2, 1, 6, 4, 0],
        [0, 6, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 3, 0, 5, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 2), (5, 2), (6, 3), (5, 4), (6, 4), (6, 5)])
    puzzle.add_between_line([(2, 3), (1, 2), (1, 1), (0, 0), (0, 1)])
    puzzle.add_between_line([(5, 6), (4, 7), (3, 7), (2, 6), (1, 7)])
    puzzle.add_between_line([(7, 7), (6, 6), (7, 5), (7, 6), (8, 7)])
    puzzle.add_between_line([(8, 2), (7, 2), (7, 1), (7, 0)])
    puzzle.add_between_line([(3, 6), (3, 5), (4, 4), (3, 3)])
    puzzle.add_between_line([(0, 7), (1, 8), (2, 7), (3, 8)])
    puzzle.add_between_line([(3, 0), (3, 1), (2, 2)])
    puzzle.add_between_line([(5, 7), (6, 8), (5, 8)])
    puzzle.add_between_line([(8, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(0, 3), (1, 3), (1, 4)])

    return puzzle
