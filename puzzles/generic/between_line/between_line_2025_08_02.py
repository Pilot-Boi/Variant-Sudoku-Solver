"""PuzzleMadness Between Lines Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 3, 0, 0, 6, 4],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 6, 0, 0, 0, 5, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 4, 9, 8, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (6, 3), (5, 2), (4, 3), (4, 4), (5, 3)])
    puzzle.add_between_line([(2, 1), (1, 2), (0, 1), (0, 0), (1, 1)])
    puzzle.add_between_line([(1, 4), (2, 5), (1, 5), (2, 6), (1, 6)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 4), (7, 5), (6, 6)])
    puzzle.add_between_line([(3, 3), (4, 2), (5, 1), (5, 0)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 8), (5, 7)])
    puzzle.add_between_line([(7, 4), (8, 5), (8, 6), (7, 6)])
    puzzle.add_between_line([(5, 6), (4, 6), (4, 5)])
    puzzle.add_between_line([(8, 2), (8, 3), (8, 4)])
    puzzle.add_between_line([(7, 8), (8, 8), (7, 7)])
    puzzle.add_between_line([(3, 2), (2, 2), (3, 1)])

    return puzzle
