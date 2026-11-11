"""PuzzleMadness Between Lines Sudoku — 2025-08-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 4, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 0],
        [6, 0, 0, 0, 3, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 5), (0, 4), (0, 3), (1, 3), (1, 2), (2, 3)])
    puzzle.add_between_line([(3, 7), (2, 8), (2, 7), (2, 6), (3, 5)])
    puzzle.add_between_line([(7, 5), (6, 6), (5, 6), (6, 5), (5, 5)])
    puzzle.add_between_line([(8, 7), (7, 7), (6, 8), (6, 7), (5, 7)])
    puzzle.add_between_line([(5, 8), (4, 7), (4, 6), (4, 5)])
    puzzle.add_between_line([(5, 1), (5, 2), (6, 1), (7, 2)])
    puzzle.add_between_line([(0, 0), (1, 1), (2, 1), (3, 1)])
    puzzle.add_between_line([(3, 4), (2, 5), (1, 6)])
    puzzle.add_between_line([(0, 6), (0, 7), (1, 8)])
    puzzle.add_between_line([(8, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(7, 4), (8, 5), (8, 4)])

    return puzzle
