"""PuzzleMadness Between Lines Sudoku — 2025-11-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 6, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 1, 0, 0, 2, 0, 0],
        [1, 0, 0, 3, 0, 0, 0, 0, 0],
        [9, 0, 0, 4, 0, 0, 5, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [8, 1, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 4), (8, 5), (7, 4), (6, 4), (5, 3), (6, 2)])
    puzzle.add_between_line([(2, 5), (2, 6), (3, 5), (4, 5), (5, 4)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 6), (1, 7), (2, 8)])
    puzzle.add_between_line([(5, 7), (5, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_between_line([(3, 4), (2, 4), (3, 3), (2, 3), (3, 2)])
    puzzle.add_between_line([(7, 6), (7, 5), (6, 6), (6, 5)])
    puzzle.add_between_line([(1, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_between_line([(0, 1), (0, 2), (0, 3), (1, 3)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 8), (5, 8)])
    puzzle.add_between_line([(4, 0), (4, 1), (3, 1)])
    puzzle.add_between_line([(4, 2), (5, 2), (5, 1)])
    puzzle.add_between_line([(7, 0), (6, 0), (7, 1)])

    return puzzle
