"""PuzzleMadness Between Lines Sudoku — 2025-08-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [3, 0, 0, 4, 6, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 3, 8, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 9, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 5, 0, 0, 7, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 2), (5, 2), (5, 1), (6, 0), (7, 0), (8, 1)])
    puzzle.add_between_line([(1, 5), (1, 6), (2, 5), (1, 4), (0, 4)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 4), (7, 4), (7, 3)])
    puzzle.add_between_line([(2, 1), (2, 2), (3, 3), (3, 2), (4, 2)])
    puzzle.add_between_line([(2, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_between_line([(5, 0), (4, 1), (3, 0), (3, 1)])
    puzzle.add_between_line([(2, 4), (1, 3), (2, 3), (1, 2)])
    puzzle.add_between_line([(5, 5), (5, 4), (4, 5)])
    puzzle.add_between_line([(7, 8), (6, 8), (6, 7)])
    puzzle.add_between_line([(4, 7), (4, 8), (5, 7)])

    return puzzle
