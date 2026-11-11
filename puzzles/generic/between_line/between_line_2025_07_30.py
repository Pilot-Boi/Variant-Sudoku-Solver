"""PuzzleMadness Between Lines Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 2, 4, 0],
        [0, 0, 0, 3, 0, 0, 0, 8, 0],
        [0, 8, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
        [4, 0, 2, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (5, 5), (5, 6), (4, 7), (5, 7), (4, 8)])
    puzzle.add_between_line([(2, 8), (1, 7), (2, 6), (1, 6), (0, 6)])
    puzzle.add_between_line([(8, 1), (7, 1), (6, 0), (5, 1), (4, 1)])
    puzzle.add_between_line([(2, 3), (3, 3), (4, 2), (3, 2), (2, 1)])
    puzzle.add_between_line([(3, 6), (2, 5), (2, 4), (3, 5)])
    puzzle.add_between_line([(5, 3), (4, 4), (4, 3), (5, 2)])
    puzzle.add_between_line([(8, 8), (7, 7), (6, 8), (7, 8)])
    puzzle.add_between_line([(3, 1), (3, 0), (2, 0), (1, 1)])
    puzzle.add_between_line([(1, 3), (0, 2), (0, 3)])
    puzzle.add_between_line([(7, 6), (7, 5), (6, 5)])
    puzzle.add_between_line([(0, 4), (1, 5), (1, 4)])

    return puzzle
