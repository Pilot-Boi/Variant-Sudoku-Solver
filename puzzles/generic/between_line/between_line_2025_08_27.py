"""PuzzleMadness Between Lines Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 3, 0, 0],
        [0, 0, 5, 4, 7, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 0, 0],
        [6, 0, 0, 0, 2, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 3, 0],
        [0, 0, 0, 7, 4, 2, 0, 8, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 3), (5, 2), (4, 1), (3, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(3, 6), (3, 5), (4, 6), (5, 7), (6, 6)])
    puzzle.add_between_line([(1, 6), (0, 6), (1, 7), (2, 6), (2, 5)])
    puzzle.add_between_line([(5, 1), (5, 0), (6, 0), (7, 1), (6, 1)])
    puzzle.add_between_line([(2, 3), (1, 4), (0, 4), (0, 5), (1, 5)])
    puzzle.add_between_line([(5, 6), (6, 5), (5, 5), (4, 5)])
    puzzle.add_between_line([(7, 6), (7, 5), (8, 4), (7, 4)])
    puzzle.add_between_line([(1, 2), (1, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(7, 0), (8, 1), (8, 0)])
    puzzle.add_between_line([(8, 6), (7, 7), (8, 8)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 2)])

    return puzzle
