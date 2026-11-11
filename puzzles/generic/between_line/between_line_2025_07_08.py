"""PuzzleMadness Between Lines Sudoku — 2025-07-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 7, 4, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 5, 9, 0, 0, 2],
        [0, 7, 0, 0, 0, 5, 3, 0, 0],
        [5, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 2), (8, 2), (8, 3), (7, 4), (8, 5), (8, 4)])
    puzzle.add_between_line([(0, 8), (1, 7), (0, 6), (1, 6), (2, 7)])
    puzzle.add_between_line([(2, 2), (1, 1), (2, 0), (3, 1), (3, 2)])
    puzzle.add_between_line([(6, 2), (5, 3), (6, 4), (5, 4), (5, 5)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 7), (5, 6)])
    puzzle.add_between_line([(4, 2), (5, 1), (5, 0), (4, 1)])
    puzzle.add_between_line([(4, 3), (4, 4), (4, 5), (3, 6)])
    puzzle.add_between_line([(0, 4), (1, 5), (1, 4), (1, 3)])
    puzzle.add_between_line([(6, 6), (5, 7), (4, 8)])
    puzzle.add_between_line([(3, 4), (2, 4), (3, 5)])
    puzzle.add_between_line([(7, 6), (8, 7), (7, 7)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 8)])

    return puzzle
