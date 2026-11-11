"""PuzzleMadness Between Lines Sudoku — 2025-02-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 9, 0, 0, 0, 5, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 6],
        [0, 0, 0, 8, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 6, 0, 7, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 7), (6, 8), (6, 7), (5, 7), (6, 6), (7, 6)])
    puzzle.add_between_line([(4, 2), (3, 2), (2, 2), (3, 1), (4, 1)])
    puzzle.add_between_line([(1, 4), (1, 3), (0, 4), (1, 5), (0, 5)])
    puzzle.add_between_line([(7, 0), (8, 0), (7, 1), (7, 2), (8, 1)])
    puzzle.add_between_line([(5, 2), (5, 1), (6, 2), (5, 3), (4, 3)])
    puzzle.add_between_line([(4, 0), (5, 0), (6, 1), (6, 0)])
    puzzle.add_between_line([(8, 7), (8, 6), (7, 5), (6, 4)])
    puzzle.add_between_line([(3, 6), (3, 7), (2, 6), (2, 5)])
    puzzle.add_between_line([(6, 3), (7, 3), (7, 4)])
    puzzle.add_between_line([(4, 7), (4, 8), (5, 8)])
    puzzle.add_between_line([(8, 4), (8, 3), (8, 2)])
    puzzle.add_between_line([(5, 6), (4, 5), (5, 4)])

    return puzzle
