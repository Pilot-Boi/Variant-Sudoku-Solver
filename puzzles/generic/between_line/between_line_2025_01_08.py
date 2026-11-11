"""PuzzleMadness Between Lines Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 1, 0],
        [0, 3, 0, 0, 0, 6, 0, 0, 7],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 2, 7, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 7), (3, 7), (3, 8), (2, 8), (2, 7), (1, 6)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (1, 2), (1, 3)])
    puzzle.add_between_line([(4, 3), (4, 4), (5, 5), (5, 4), (5, 3)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4), (2, 4), (3, 4)])
    puzzle.add_between_line([(4, 1), (3, 1), (4, 0), (5, 0)])
    puzzle.add_between_line([(6, 6), (7, 6), (6, 7), (6, 8)])
    puzzle.add_between_line([(2, 6), (2, 5), (3, 5), (3, 6)])
    puzzle.add_between_line([(3, 3), (3, 2), (4, 2)])
    puzzle.add_between_line([(7, 7), (8, 8), (7, 8)])
    puzzle.add_between_line([(7, 4), (7, 5), (8, 5)])

    return puzzle
