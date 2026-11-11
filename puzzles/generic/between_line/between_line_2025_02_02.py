"""PuzzleMadness Between Lines Sudoku — 2025-02-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 1, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 2, 4, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 0), (1, 1), (2, 0), (3, 1), (3, 2), (4, 1)])
    puzzle.add_between_line([(8, 4), (8, 3), (8, 2), (7, 3), (6, 4)])
    puzzle.add_between_line([(6, 8), (5, 7), (5, 6), (4, 6), (4, 5)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 5), (7, 6), (7, 7)])
    puzzle.add_between_line([(4, 3), (5, 2), (6, 2), (6, 1), (7, 1)])
    puzzle.add_between_line([(6, 0), (5, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(0, 5), (0, 6), (1, 6), (2, 7)])
    puzzle.add_between_line([(8, 1), (7, 2), (6, 3), (5, 3)])
    puzzle.add_between_line([(3, 5), (3, 6), (2, 5), (2, 6)])
    puzzle.add_between_line([(1, 3), (2, 2), (1, 2)])
    puzzle.add_between_line([(4, 2), (3, 3), (2, 3)])
    puzzle.add_between_line([(4, 8), (3, 7), (2, 8)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4)])

    return puzzle
