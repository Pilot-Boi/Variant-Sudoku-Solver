"""PuzzleMadness Between Lines Sudoku — 2025-02-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [6, 0, 1, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 1)])
    puzzle.add_between_line([(7, 2), (8, 2), (7, 1), (6, 0), (5, 1)])
    puzzle.add_between_line([(2, 0), (3, 0), (3, 1), (4, 2), (4, 3)])
    puzzle.add_between_line([(1, 1), (1, 2), (2, 3), (3, 2), (3, 3)])
    puzzle.add_between_line([(6, 6), (5, 7), (4, 7), (4, 6), (3, 6)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 3), (6, 4)])
    puzzle.add_between_line([(2, 7), (3, 7), (2, 6), (3, 5)])
    puzzle.add_between_line([(6, 3), (5, 3), (6, 2), (5, 2)])
    puzzle.add_between_line([(0, 8), (1, 8), (1, 7), (2, 8)])
    puzzle.add_between_line([(7, 7), (8, 6), (7, 6)])
    puzzle.add_between_line([(4, 5), (5, 5), (5, 4)])
    puzzle.add_between_line([(8, 8), (7, 8), (8, 7)])
    puzzle.add_between_line([(7, 4), (6, 5), (7, 5)])

    return puzzle
