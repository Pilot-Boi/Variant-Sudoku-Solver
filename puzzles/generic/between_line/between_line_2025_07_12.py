"""PuzzleMadness Between Lines Sudoku — 2025-07-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 8, 0],
        [0, 9, 0, 3, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 1, 6, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 6, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 6, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (7, 4), (7, 5), (8, 6), (7, 7), (6, 7)])
    puzzle.add_between_line([(1, 6), (1, 7), (0, 7), (0, 8), (1, 8)])
    puzzle.add_between_line([(6, 8), (5, 7), (6, 6), (6, 5), (5, 4)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 1), (6, 1), (5, 2)])
    puzzle.add_between_line([(3, 4), (4, 4), (4, 5), (4, 6), (5, 6)])
    puzzle.add_between_line([(5, 1), (4, 0), (3, 0), (4, 1)])
    puzzle.add_between_line([(0, 1), (0, 2), (1, 1), (2, 1)])
    puzzle.add_between_line([(2, 7), (3, 6), (2, 6), (2, 5)])
    puzzle.add_between_line([(0, 4), (1, 3), (0, 3)])
    puzzle.add_between_line([(0, 5), (1, 4), (2, 4)])
    puzzle.add_between_line([(3, 3), (3, 2), (4, 2)])
    puzzle.add_between_line([(7, 3), (8, 3), (8, 2)])

    return puzzle
