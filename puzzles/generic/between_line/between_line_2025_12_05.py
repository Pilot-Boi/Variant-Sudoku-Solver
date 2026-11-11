"""PuzzleMadness Between Lines Sudoku — 2025-12-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 5, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 8, 0, 0, 0, 0],
        [2, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 5), (0, 5), (1, 4), (1, 3), (2, 4), (2, 5)])
    puzzle.add_between_line([(1, 7), (2, 7), (3, 8), (4, 7), (5, 8)])
    puzzle.add_between_line([(8, 8), (7, 7), (6, 7), (5, 6), (6, 5)])
    puzzle.add_between_line([(8, 3), (7, 3), (6, 4), (5, 4), (5, 3)])
    puzzle.add_between_line([(3, 1), (3, 2), (3, 3), (4, 2), (4, 3)])
    puzzle.add_between_line([(2, 6), (3, 6), (4, 5), (5, 5)])
    puzzle.add_between_line([(0, 3), (1, 2), (0, 1), (1, 0)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 2), (8, 2)])
    puzzle.add_between_line([(7, 0), (6, 0), (6, 1)])
    puzzle.add_between_line([(8, 5), (8, 6), (8, 7)])
    puzzle.add_between_line([(1, 1), (2, 2), (2, 3)])
    puzzle.add_between_line([(3, 5), (3, 4), (4, 4)])

    return puzzle
