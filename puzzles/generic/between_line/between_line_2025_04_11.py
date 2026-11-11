"""PuzzleMadness Between Lines Sudoku — 2025-04-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 5, 0, 0, 6, 0, 8, 4],
        [6, 0, 1, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 8],
        [5, 0, 2, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 4), (8, 5), (8, 4), (7, 3), (7, 2), (8, 3)])
    puzzle.add_between_line([(0, 7), (1, 7), (2, 7), (3, 6), (3, 7)])
    puzzle.add_between_line([(7, 0), (7, 1), (6, 2), (5, 1), (4, 1)])
    puzzle.add_between_line([(1, 1), (0, 2), (0, 3), (1, 3), (0, 4)])
    puzzle.add_between_line([(5, 0), (4, 0), (3, 0), (2, 1)])
    puzzle.add_between_line([(4, 6), (5, 6), (6, 5), (6, 4)])
    puzzle.add_between_line([(5, 8), (6, 8), (6, 7), (6, 6)])
    puzzle.add_between_line([(3, 1), (4, 2), (4, 3), (5, 2)])
    puzzle.add_between_line([(1, 4), (2, 3), (3, 3)])
    puzzle.add_between_line([(1, 0), (0, 0), (0, 1)])
    puzzle.add_between_line([(4, 5), (5, 4), (4, 4)])
    puzzle.add_between_line([(0, 6), (1, 6), (2, 5)])

    return puzzle
