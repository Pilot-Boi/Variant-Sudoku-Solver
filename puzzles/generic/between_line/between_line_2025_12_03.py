"""PuzzleMadness Between Lines Sudoku — 2025-12-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 8, 6, 0, 0],
        [0, 0, 1, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 7, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 5, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 3), (2, 3), (1, 3), (2, 4), (3, 5), (2, 5)])
    puzzle.add_between_line([(8, 8), (7, 7), (6, 7), (5, 8), (5, 7)])
    puzzle.add_between_line([(7, 2), (6, 2), (6, 1), (5, 2), (5, 1)])
    puzzle.add_between_line([(5, 3), (4, 3), (3, 2), (4, 2), (3, 1)])
    puzzle.add_between_line([(7, 3), (7, 4), (6, 5), (5, 6), (4, 7)])
    puzzle.add_between_line([(0, 8), (1, 7), (1, 6), (2, 6)])
    puzzle.add_between_line([(1, 1), (1, 0), (0, 1), (1, 2)])
    puzzle.add_between_line([(2, 2), (2, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(3, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_between_line([(5, 4), (5, 5), (6, 4)])
    puzzle.add_between_line([(7, 1), (8, 1), (8, 2)])
    puzzle.add_between_line([(8, 7), (8, 6), (8, 5)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4)])

    return puzzle
