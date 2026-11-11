"""PuzzleMadness Between Lines Sudoku — 2025-02-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 4, 0, 0],
        [0, 0, 0, 1, 6, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 7, 0, 6, 3],
        [0, 0, 0, 0, 5, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 3), (2, 4), (2, 5), (3, 6), (2, 7), (1, 8)])
    puzzle.add_between_line([(1, 2), (0, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_between_line([(4, 3), (3, 3), (3, 2), (3, 1), (2, 2)])
    puzzle.add_between_line([(5, 7), (6, 8), (7, 8), (7, 7), (8, 7)])
    puzzle.add_between_line([(8, 2), (7, 2), (7, 1), (8, 1)])
    puzzle.add_between_line([(5, 3), (5, 2), (4, 1), (3, 0)])
    puzzle.add_between_line([(3, 7), (4, 8), (5, 8), (4, 7)])
    puzzle.add_between_line([(6, 6), (5, 5), (6, 4), (6, 5)])
    puzzle.add_between_line([(0, 7), (1, 7), (0, 8)])
    puzzle.add_between_line([(4, 0), (5, 1), (5, 0)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4)])

    return puzzle
