"""PuzzleMadness Between Lines Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 6, 0, 0, 8, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 4, 2, 6, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 4],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 5, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 7), (6, 7), (7, 6), (6, 5), (5, 6), (5, 7)])
    puzzle.add_between_line([(8, 6), (7, 5), (7, 4), (6, 3), (7, 2)])
    puzzle.add_between_line([(7, 0), (6, 1), (5, 2), (4, 1), (3, 1)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 4), (2, 3), (1, 3)])
    puzzle.add_between_line([(1, 8), (0, 8), (1, 7), (1, 6)])
    puzzle.add_between_line([(2, 2), (3, 3), (4, 4), (3, 5)])
    puzzle.add_between_line([(8, 5), (8, 4), (8, 3), (7, 3)])
    puzzle.add_between_line([(4, 2), (5, 3), (5, 4)])
    puzzle.add_between_line([(8, 1), (7, 1), (8, 0)])
    puzzle.add_between_line([(4, 5), (5, 5), (6, 4)])

    return puzzle
