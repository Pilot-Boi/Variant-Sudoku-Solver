"""PuzzleMadness Between Lines Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 7, 6, 0],
        [0, 6, 0, 0, 0, 4, 3, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 1, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 5, 0, 0],
        [0, 0, 8, 4, 0, 0, 0, 7, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (2, 5), (1, 4), (0, 5), (1, 6), (0, 6)])
    puzzle.add_between_line([(8, 7), (7, 6), (6, 5), (5, 6), (5, 5)])
    puzzle.add_between_line([(4, 4), (3, 3), (4, 2), (3, 2), (3, 1)])
    puzzle.add_between_line([(8, 8), (7, 8), (7, 7), (6, 8), (6, 7)])
    puzzle.add_between_line([(1, 7), (2, 8), (3, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(4, 0), (5, 1), (6, 2), (6, 1)])
    puzzle.add_between_line([(1, 0), (0, 0), (0, 1), (1, 1)])
    puzzle.add_between_line([(7, 2), (7, 3), (8, 4), (7, 4)])
    puzzle.add_between_line([(4, 3), (5, 3), (5, 4), (4, 5)])
    puzzle.add_between_line([(5, 7), (4, 8), (3, 8)])
    puzzle.add_between_line([(6, 3), (6, 4), (7, 5)])
    puzzle.add_between_line([(3, 4), (3, 5), (2, 4)])

    return puzzle
