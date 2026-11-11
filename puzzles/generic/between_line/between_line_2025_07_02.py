"""PuzzleMadness Between Lines Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 8, 0, 5, 0, 1, 0, 0, 3],
        [3, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 1, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 0), (4, 1), (3, 1), (2, 2), (1, 1), (2, 0)])
    puzzle.add_between_line([(5, 7), (6, 6), (6, 5), (7, 4), (6, 4)])
    puzzle.add_between_line([(1, 3), (0, 4), (0, 3), (1, 2), (0, 1)])
    puzzle.add_between_line([(4, 6), (3, 6), (2, 6), (1, 5), (0, 6)])
    puzzle.add_between_line([(5, 2), (5, 3), (6, 3), (5, 4), (4, 4)])
    puzzle.add_between_line([(7, 8), (8, 8), (7, 7), (6, 7)])
    puzzle.add_between_line([(2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_between_line([(7, 2), (7, 1), (8, 2), (7, 3)])
    puzzle.add_between_line([(2, 7), (3, 8), (3, 7)])
    puzzle.add_between_line([(1, 8), (1, 7), (0, 7)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 0)])

    return puzzle
