"""PuzzleMadness Between Lines Sudoku — 2025-10-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 7, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 4, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [0, 0, 0, 1, 0, 3, 7, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 7), (7, 6), (7, 7), (6, 8), (5, 7), (6, 7)])
    puzzle.add_between_line([(0, 7), (1, 8), (1, 7), (1, 6), (0, 6)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 3), (2, 3), (2, 4)])
    puzzle.add_between_line([(1, 2), (2, 2), (1, 1), (0, 1), (0, 0)])
    puzzle.add_between_line([(4, 6), (3, 6), (2, 7), (2, 8)])
    puzzle.add_between_line([(1, 5), (2, 5), (3, 4), (3, 5)])
    puzzle.add_between_line([(8, 4), (7, 3), (6, 2), (7, 2)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 1)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0)])
    puzzle.add_between_line([(6, 6), (6, 5), (5, 5)])

    return puzzle
