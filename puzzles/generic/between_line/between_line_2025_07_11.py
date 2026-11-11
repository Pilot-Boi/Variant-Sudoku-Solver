"""PuzzleMadness Between Lines Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 6],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 5, 0, 6, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 1), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2)])
    puzzle.add_between_line([(2, 2), (1, 3), (2, 3), (3, 3), (4, 3)])
    puzzle.add_between_line([(6, 4), (7, 3), (8, 3), (8, 2), (7, 1)])
    puzzle.add_between_line([(7, 7), (6, 6), (5, 7), (5, 8), (4, 7)])
    puzzle.add_between_line([(7, 4), (7, 5), (6, 5), (5, 5), (4, 5)])
    puzzle.add_between_line([(0, 5), (1, 4), (2, 4), (3, 5)])
    puzzle.add_between_line([(5, 1), (4, 0), (4, 1), (5, 2)])
    puzzle.add_between_line([(2, 5), (1, 5), (1, 6), (2, 6)])
    puzzle.add_between_line([(6, 3), (7, 2), (6, 1)])
    puzzle.add_between_line([(0, 7), (1, 8), (2, 8)])
    puzzle.add_between_line([(3, 0), (2, 0), (3, 1)])

    return puzzle
