"""PuzzleMadness Between Lines Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 2, 0, 0, 6, 0, 0, 0],
        [0, 8, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [8, 0, 0, 0, 0, 7, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 5, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 0), (6, 0), (5, 0), (4, 0), (3, 1), (3, 0)])
    puzzle.add_between_line([(8, 2), (7, 1), (6, 1), (5, 2), (5, 1)])
    puzzle.add_between_line([(6, 3), (7, 2), (6, 2), (5, 3), (5, 4)])
    puzzle.add_between_line([(4, 1), (3, 2), (3, 3), (3, 4), (3, 5)])
    puzzle.add_between_line([(7, 7), (6, 6), (5, 7), (4, 8), (3, 8)])
    puzzle.add_between_line([(2, 8), (2, 7), (1, 7), (0, 6)])
    puzzle.add_between_line([(1, 2), (2, 2), (1, 3), (1, 4)])
    puzzle.add_between_line([(6, 4), (7, 3), (8, 4), (7, 5)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_between_line([(5, 6), (4, 6), (3, 6)])
    puzzle.add_between_line([(1, 5), (0, 5), (0, 4)])
    puzzle.add_between_line([(4, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 8)])

    return puzzle
