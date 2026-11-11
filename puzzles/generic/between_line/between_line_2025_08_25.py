"""PuzzleMadness Between Lines Sudoku — 2025-08-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 1, 0, 2, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 6, 0],
        [0, 8, 4, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 7],
        [9, 6, 3, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (4, 3), (3, 4), (4, 4), (3, 5), (4, 5)])
    puzzle.add_between_line([(2, 3), (1, 2), (2, 1), (2, 2), (3, 2)])
    puzzle.add_between_line([(5, 8), (6, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_between_line([(6, 2), (7, 2), (6, 1), (5, 2), (4, 1)])
    puzzle.add_between_line([(3, 1), (4, 0), (5, 0), (5, 1)])
    puzzle.add_between_line([(2, 5), (1, 4), (0, 5), (1, 6)])
    puzzle.add_between_line([(7, 0), (7, 1), (8, 1), (8, 0)])
    puzzle.add_between_line([(1, 7), (1, 8), (0, 7)])
    puzzle.add_between_line([(8, 5), (7, 5), (7, 4)])
    puzzle.add_between_line([(8, 3), (8, 4), (7, 3)])

    return puzzle
