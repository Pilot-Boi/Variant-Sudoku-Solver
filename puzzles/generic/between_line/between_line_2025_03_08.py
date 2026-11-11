"""PuzzleMadness Between Lines Sudoku — 2025-03-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 3, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 7, 0, 4, 0],
        [0, 0, 0, 1, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 5, 0, 0, 0, 3, 0, 0],
        [6, 0, 0, 0, 0, 0, 4, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 8), (1, 8), (2, 7), (3, 6), (4, 7), (5, 7)])
    puzzle.add_between_line([(4, 4), (5, 5), (6, 4), (7, 4), (7, 5)])
    puzzle.add_between_line([(5, 4), (4, 3), (3, 2), (2, 3), (2, 4)])
    puzzle.add_between_line([(1, 2), (0, 3), (0, 2), (1, 1), (2, 0)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 3), (5, 2), (5, 1)])
    puzzle.add_between_line([(6, 1), (5, 0), (6, 0), (7, 1)])
    puzzle.add_between_line([(2, 5), (1, 4), (0, 4), (1, 3)])
    puzzle.add_between_line([(5, 3), (4, 2), (3, 1), (2, 1)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(7, 0), (8, 0), (8, 1)])
    puzzle.add_between_line([(7, 6), (6, 7), (7, 8)])

    return puzzle
