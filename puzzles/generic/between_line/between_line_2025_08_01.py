"""PuzzleMadness Between Lines Sudoku — 2025-08-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 7, 0, 8, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 4, 0, 0, 7, 8, 0, 5],
        [0, 0, 0, 2, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 7), (7, 8), (6, 7), (6, 8), (5, 7), (5, 6)])
    puzzle.add_between_line([(6, 4), (5, 5), (6, 6), (7, 6), (8, 5)])
    puzzle.add_between_line([(1, 5), (2, 6), (1, 7), (1, 8), (2, 7)])
    puzzle.add_between_line([(4, 6), (3, 6), (3, 7), (4, 7), (5, 8)])
    puzzle.add_between_line([(0, 6), (0, 5), (0, 4), (1, 3), (1, 4)])
    puzzle.add_between_line([(8, 1), (7, 1), (6, 0), (6, 1)])
    puzzle.add_between_line([(3, 5), (2, 5), (3, 4), (4, 4)])
    puzzle.add_between_line([(7, 4), (7, 3), (8, 3), (8, 4)])
    puzzle.add_between_line([(1, 1), (0, 2), (1, 2), (2, 2)])
    puzzle.add_between_line([(5, 0), (4, 1), (3, 2)])
    puzzle.add_between_line([(3, 3), (4, 3), (5, 3)])
    puzzle.add_between_line([(6, 3), (6, 2), (5, 1)])

    return puzzle
