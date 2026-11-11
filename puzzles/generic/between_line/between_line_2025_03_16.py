"""PuzzleMadness Between Lines Sudoku — 2025-03-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 8, 0, 2, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 6, 9, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 1],
        [9, 0, 6, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 5), (6, 4), (7, 3), (7, 2), (8, 2), (8, 3)])
    puzzle.add_between_line([(7, 0), (8, 1), (7, 1), (6, 0), (6, 1)])
    puzzle.add_between_line([(3, 2), (2, 2), (1, 2), (2, 3), (1, 4)])
    puzzle.add_between_line([(0, 3), (0, 4), (0, 5), (1, 5), (2, 4)])
    puzzle.add_between_line([(7, 8), (7, 7), (6, 7), (5, 6), (4, 7)])
    puzzle.add_between_line([(0, 7), (1, 8), (2, 7), (2, 8)])
    puzzle.add_between_line([(8, 8), (8, 7), (8, 6), (7, 6)])
    puzzle.add_between_line([(6, 6), (6, 5), (5, 5), (4, 6)])
    puzzle.add_between_line([(1, 1), (0, 0), (0, 1), (0, 2)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1)])
    puzzle.add_between_line([(5, 3), (4, 2), (5, 1)])
    puzzle.add_between_line([(8, 5), (7, 4), (8, 4)])

    return puzzle
