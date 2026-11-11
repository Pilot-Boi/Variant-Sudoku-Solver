"""PuzzleMadness Between Lines Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 3],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 2, 3, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 5, 0, 0, 7, 4, 0, 0],
        [0, 0, 1, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 8), (4, 8), (3, 7), (3, 8), (2, 7), (2, 8)])
    puzzle.add_between_line([(6, 3), (7, 3), (8, 3), (8, 4), (7, 4)])
    puzzle.add_between_line([(6, 7), (7, 8), (8, 8), (7, 7), (8, 7)])
    puzzle.add_between_line([(4, 1), (3, 1), (2, 2), (1, 1), (0, 1)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4), (1, 3)])
    puzzle.add_between_line([(4, 7), (5, 6), (5, 5), (4, 6)])
    puzzle.add_between_line([(4, 0), (5, 0), (6, 1), (5, 1)])
    puzzle.add_between_line([(5, 3), (4, 4), (4, 3)])
    puzzle.add_between_line([(7, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(2, 5), (3, 5), (3, 6)])

    return puzzle
