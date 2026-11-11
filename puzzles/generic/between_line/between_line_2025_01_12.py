"""PuzzleMadness Between Lines Sudoku — 2025-01-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 2, 0],
        [0, 0, 0, 6, 0, 0, 1, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 7, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 3],
        [0, 0, 6, 9, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (8, 2), (7, 1), (7, 0), (6, 1), (5, 1)])
    puzzle.add_between_line([(8, 7), (7, 6), (6, 7), (6, 8), (7, 7)])
    puzzle.add_between_line([(5, 7), (5, 6), (4, 7), (3, 8), (2, 8)])
    puzzle.add_between_line([(5, 0), (4, 0), (4, 1), (3, 1), (3, 2)])
    puzzle.add_between_line([(0, 2), (1, 3), (0, 4), (1, 5), (0, 5)])
    puzzle.add_between_line([(5, 3), (5, 4), (4, 4), (3, 3)])
    puzzle.add_between_line([(1, 1), (2, 1), (1, 2), (0, 1)])
    puzzle.add_between_line([(6, 3), (6, 4), (7, 5), (6, 6)])
    puzzle.add_between_line([(2, 4), (3, 4), (2, 3), (2, 2)])
    puzzle.add_between_line([(1, 8), (2, 7), (1, 7)])
    puzzle.add_between_line([(4, 6), (3, 6), (2, 5)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4)])

    return puzzle
