"""PuzzleMadness Between Lines Sudoku — 2025-09-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 1, 0, 8, 0, 0, 4],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 1, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 7), (4, 6), (5, 7), (5, 6), (4, 5), (3, 6)])
    puzzle.add_between_line([(0, 6), (1, 6), (0, 7), (0, 8), (1, 8)])
    puzzle.add_between_line([(3, 7), (2, 6), (2, 5), (1, 5), (0, 5)])
    puzzle.add_between_line([(6, 6), (6, 7), (7, 7), (8, 7), (8, 6)])
    puzzle.add_between_line([(2, 0), (3, 0), (4, 1), (4, 2), (4, 3)])
    puzzle.add_between_line([(4, 0), (5, 1), (5, 2), (5, 3)])
    puzzle.add_between_line([(3, 2), (2, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(1, 7), (2, 7), (3, 8), (4, 8)])
    puzzle.add_between_line([(0, 1), (1, 2), (2, 1), (3, 1)])
    puzzle.add_between_line([(0, 0), (1, 0), (1, 1)])
    puzzle.add_between_line([(7, 1), (6, 0), (5, 0)])
    puzzle.add_between_line([(4, 4), (3, 3), (3, 4)])

    return puzzle
