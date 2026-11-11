"""PuzzleMadness Between Lines Sudoku — 2025-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 3, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 4, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [4, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 5, 0, 0, 8, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 4), (1, 4), (1, 5), (0, 4), (1, 3), (0, 3)])
    puzzle.add_between_line([(6, 6), (7, 6), (7, 7), (7, 8), (6, 7)])
    puzzle.add_between_line([(5, 8), (4, 7), (3, 7), (3, 8), (2, 8)])
    puzzle.add_between_line([(3, 0), (4, 1), (5, 1), (5, 0), (6, 1)])
    puzzle.add_between_line([(2, 2), (1, 1), (1, 2), (0, 1)])
    puzzle.add_between_line([(5, 3), (6, 4), (7, 3), (6, 2)])
    puzzle.add_between_line([(7, 4), (6, 5), (5, 6), (5, 5)])
    puzzle.add_between_line([(2, 3), (3, 4), (4, 4)])
    puzzle.add_between_line([(5, 7), (4, 6), (3, 5)])
    puzzle.add_between_line([(0, 5), (0, 6), (0, 7)])

    return puzzle
