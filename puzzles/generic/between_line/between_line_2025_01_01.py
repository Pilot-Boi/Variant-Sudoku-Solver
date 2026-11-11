"""PuzzleMadness Between Lines Sudoku — 2025-01-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 3],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 9, 0, 6, 2, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 8, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 7), (2, 6), (1, 7), (1, 6), (1, 5), (2, 5)])
    puzzle.add_between_line([(2, 0), (2, 1), (3, 2), (4, 3), (5, 3)])
    puzzle.add_between_line([(8, 3), (7, 3), (6, 3), (5, 4), (6, 4)])
    puzzle.add_between_line([(5, 8), (6, 7), (5, 6), (5, 5), (4, 5)])
    puzzle.add_between_line([(0, 5), (1, 4), (0, 4), (1, 3), (0, 2)])
    puzzle.add_between_line([(4, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_between_line([(7, 8), (7, 7), (7, 6), (8, 7)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 0), (7, 1)])
    puzzle.add_between_line([(3, 6), (3, 5), (3, 4)])
    puzzle.add_between_line([(4, 1), (3, 0), (4, 0)])
    puzzle.add_between_line([(1, 0), (0, 0), (1, 1)])

    return puzzle
