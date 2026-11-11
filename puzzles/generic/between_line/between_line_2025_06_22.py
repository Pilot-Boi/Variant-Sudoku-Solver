"""PuzzleMadness Between Lines Sudoku — 2025-06-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 8, 0, 3, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 9, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 3, 7, 0, 8, 0, 0, 0],
        [0, 0, 4, 0, 0, 3, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (1, 7), (2, 7), (3, 8), (4, 8), (5, 8)])
    puzzle.add_between_line([(0, 0), (1, 0), (1, 1), (2, 2), (3, 2)])
    puzzle.add_between_line([(6, 0), (5, 0), (5, 1), (6, 2), (6, 1)])
    puzzle.add_between_line([(0, 5), (1, 4), (2, 3), (3, 4), (2, 5)])
    puzzle.add_between_line([(7, 3), (8, 4), (8, 5), (7, 6)])
    puzzle.add_between_line([(1, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 2), (1, 3)])
    puzzle.add_between_line([(2, 0), (3, 1), (4, 1), (4, 2)])
    puzzle.add_between_line([(3, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(4, 3), (4, 4), (3, 3)])
    puzzle.add_between_line([(4, 5), (5, 4), (6, 3)])

    return puzzle
