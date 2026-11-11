"""PuzzleMadness Between Lines Sudoku — 2025-01-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 3],
        [0, 4, 2, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 2, 0, 0],
        [0, 8, 0, 4, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 8, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 6), (2, 5), (3, 5), (4, 5), (5, 4), (6, 4)])
    puzzle.add_between_line([(4, 8), (5, 8), (5, 7), (6, 6), (6, 7)])
    puzzle.add_between_line([(3, 1), (2, 2), (2, 3), (1, 2), (0, 1)])
    puzzle.add_between_line([(7, 7), (7, 6), (7, 5), (7, 4), (6, 3)])
    puzzle.add_between_line([(4, 3), (3, 2), (4, 1), (5, 2), (4, 2)])
    puzzle.add_between_line([(0, 7), (0, 8), (1, 7), (1, 8)])
    puzzle.add_between_line([(8, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(6, 2), (5, 1), (6, 1), (5, 0)])
    puzzle.add_between_line([(6, 5), (5, 6), (5, 5)])
    puzzle.add_between_line([(8, 2), (7, 1), (8, 1)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0)])

    return puzzle
