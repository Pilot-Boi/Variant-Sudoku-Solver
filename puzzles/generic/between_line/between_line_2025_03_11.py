"""PuzzleMadness Between Lines Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 1, 0, 3, 0, 8, 0, 0],
        [3, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 3],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [9, 0, 0, 0, 0, 4, 0, 7, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 9],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (2, 5), (1, 6), (1, 5), (0, 6), (1, 7)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 7), (7, 8), (8, 8)])
    puzzle.add_between_line([(4, 6), (4, 7), (3, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(3, 6), (3, 5), (4, 4), (5, 5), (6, 5)])
    puzzle.add_between_line([(1, 4), (2, 4), (2, 3), (3, 2)])
    puzzle.add_between_line([(5, 0), (4, 1), (3, 1), (2, 2)])
    puzzle.add_between_line([(5, 3), (6, 3), (5, 4), (6, 4)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 0)])
    puzzle.add_between_line([(0, 1), (1, 2), (1, 1)])
    puzzle.add_between_line([(0, 0), (1, 0), (2, 0)])
    puzzle.add_between_line([(3, 4), (4, 3), (3, 3)])

    return puzzle
