"""PuzzleMadness Between Lines Sudoku — 2025-06-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 2, 0, 7, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 9],
        [5, 8, 0, 0, 0, 0, 1, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 2, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 7), (3, 8), (4, 8), (4, 7), (4, 6), (5, 7)])
    puzzle.add_between_line([(4, 5), (4, 4), (4, 3), (3, 3), (3, 4)])
    puzzle.add_between_line([(6, 6), (5, 5), (6, 5), (6, 4), (7, 4)])
    puzzle.add_between_line([(0, 6), (1, 6), (1, 5), (2, 5), (2, 6)])
    puzzle.add_between_line([(8, 0), (7, 1), (6, 0), (6, 1)])
    puzzle.add_between_line([(0, 4), (1, 3), (2, 4), (2, 3)])
    puzzle.add_between_line([(8, 1), (7, 2), (6, 3), (5, 2)])
    puzzle.add_between_line([(5, 3), (4, 2), (5, 1)])
    puzzle.add_between_line([(3, 0), (3, 1), (3, 2)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 1)])
    puzzle.add_between_line([(2, 7), (1, 7), (1, 8)])

    return puzzle
