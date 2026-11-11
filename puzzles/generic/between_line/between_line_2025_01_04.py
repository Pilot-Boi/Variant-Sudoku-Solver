"""PuzzleMadness Between Lines Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 9, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 4, 0, 0, 0, 0, 0, 7, 0],
        [8, 0, 0, 0, 5, 0, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 7), (8, 6), (8, 5), (7, 4), (6, 3), (5, 3)])
    puzzle.add_between_line([(0, 2), (1, 1), (2, 0), (1, 0), (0, 1)])
    puzzle.add_between_line([(5, 0), (6, 0), (6, 1), (7, 2), (8, 3)])
    puzzle.add_between_line([(2, 2), (1, 3), (2, 4), (3, 3), (3, 4)])
    puzzle.add_between_line([(4, 0), (3, 0), (3, 1), (4, 1), (5, 1)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 8), (6, 7)])
    puzzle.add_between_line([(6, 5), (5, 6), (4, 6), (4, 5)])
    puzzle.add_between_line([(6, 2), (5, 2), (4, 2), (4, 3)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 1), (7, 0)])
    puzzle.add_between_line([(1, 8), (1, 7), (0, 8)])
    puzzle.add_between_line([(4, 7), (5, 7), (5, 8)])
    puzzle.add_between_line([(3, 5), (2, 5), (1, 5)])

    return puzzle
