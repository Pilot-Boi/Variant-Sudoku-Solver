"""PuzzleMadness Between Lines Sudoku — 2025-06-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 6],
        [4, 0, 0, 0, 0, 6, 1, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 3, 0],
        [0, 0, 0, 0, 2, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 6, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 1), (4, 0), (3, 0), (2, 0), (1, 1), (0, 0)])
    puzzle.add_between_line([(3, 5), (3, 6), (4, 5), (5, 5), (5, 4)])
    puzzle.add_between_line([(2, 7), (2, 8), (1, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(6, 2), (7, 2), (8, 2), (7, 1), (8, 1)])
    puzzle.add_between_line([(8, 6), (8, 7), (7, 7), (6, 6)])
    puzzle.add_between_line([(2, 6), (3, 7), (4, 6), (5, 7)])
    puzzle.add_between_line([(7, 5), (6, 4), (5, 3), (6, 3)])
    puzzle.add_between_line([(0, 3), (1, 2), (0, 2), (0, 1)])
    puzzle.add_between_line([(7, 8), (6, 7), (5, 8)])
    puzzle.add_between_line([(7, 0), (6, 0), (5, 0)])
    puzzle.add_between_line([(3, 1), (2, 2), (2, 3)])

    return puzzle
