"""PuzzleMadness Between Lines Sudoku — 2025-07-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 7, 0, 0, 9, 0, 0],
        [0, 3, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 7, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 4, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 1), (8, 0), (7, 1), (6, 0), (5, 1), (5, 2)])
    puzzle.add_between_line([(6, 5), (7, 6), (8, 5), (7, 4), (7, 3)])
    puzzle.add_between_line([(3, 8), (4, 7), (3, 7), (2, 7), (3, 6)])
    puzzle.add_between_line([(2, 1), (1, 0), (0, 1), (0, 2), (1, 1)])
    puzzle.add_between_line([(5, 0), (4, 0), (4, 1), (3, 1)])
    puzzle.add_between_line([(1, 8), (0, 7), (1, 7), (0, 6)])
    puzzle.add_between_line([(2, 3), (1, 3), (1, 4), (2, 5)])
    puzzle.add_between_line([(1, 5), (0, 5), (0, 4)])
    puzzle.add_between_line([(7, 7), (6, 8), (5, 7)])
    puzzle.add_between_line([(2, 4), (3, 3), (4, 4)])

    return puzzle
