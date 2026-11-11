"""PuzzleMadness Between Lines Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 8, 0, 0, 0, 5],
        [9, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (2, 4), (3, 4), (4, 4), (3, 3), (4, 3)])
    puzzle.add_between_line([(7, 7), (6, 6), (7, 5), (6, 4), (5, 3)])
    puzzle.add_between_line([(0, 2), (0, 3), (0, 4), (1, 5), (1, 4)])
    puzzle.add_between_line([(7, 1), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(3, 2), (2, 3), (1, 2), (2, 2), (2, 1)])
    puzzle.add_between_line([(5, 2), (5, 1), (4, 1), (5, 0)])
    puzzle.add_between_line([(4, 7), (3, 7), (4, 8), (5, 7)])
    puzzle.add_between_line([(3, 6), (3, 5), (2, 5), (2, 6)])
    puzzle.add_between_line([(5, 4), (6, 5), (5, 5)])
    puzzle.add_between_line([(3, 0), (2, 0), (1, 0)])
    puzzle.add_between_line([(2, 8), (2, 7), (1, 7)])
    puzzle.add_between_line([(6, 8), (6, 7), (5, 8)])

    return puzzle
