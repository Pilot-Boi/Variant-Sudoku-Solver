"""PuzzleMadness Between Lines Sudoku — 2025-02-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 7, 8, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [5, 4, 7, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 0), (5, 1), (6, 2), (7, 3), (7, 4), (6, 3)])
    puzzle.add_between_line([(2, 1), (3, 1), (2, 2), (1, 3), (1, 2)])
    puzzle.add_between_line([(1, 0), (2, 0), (1, 1), (0, 2), (0, 1)])
    puzzle.add_between_line([(5, 4), (6, 4), (5, 3), (4, 4), (3, 4)])
    puzzle.add_between_line([(8, 8), (8, 7), (7, 8), (6, 7), (5, 7)])
    puzzle.add_between_line([(5, 6), (6, 6), (6, 5), (7, 6)])
    puzzle.add_between_line([(4, 8), (3, 7), (4, 7), (5, 8)])
    puzzle.add_between_line([(2, 7), (1, 7), (0, 6), (0, 5)])
    puzzle.add_between_line([(3, 3), (4, 3), (3, 2), (4, 1)])
    puzzle.add_between_line([(2, 4), (2, 5), (3, 5)])
    puzzle.add_between_line([(1, 6), (2, 6), (1, 5)])
    puzzle.add_between_line([(8, 4), (8, 5), (8, 6)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7)])

    return puzzle
