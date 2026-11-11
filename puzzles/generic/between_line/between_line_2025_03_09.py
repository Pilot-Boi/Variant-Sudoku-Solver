"""PuzzleMadness Between Lines Sudoku — 2025-03-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 5, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 3],
        [0, 3, 0, 0, 0, 0, 4, 0, 0],
        [0, 7, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 6, 8, 0, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 3), (8, 4), (7, 5), (6, 4), (5, 3), (4, 3)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 2), (6, 1), (5, 0)])
    puzzle.add_between_line([(4, 1), (5, 1), (4, 0), (3, 0), (2, 1)])
    puzzle.add_between_line([(6, 7), (5, 8), (5, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(2, 8), (1, 7), (0, 6), (0, 7)])
    puzzle.add_between_line([(6, 6), (7, 6), (6, 5), (5, 4)])
    puzzle.add_between_line([(0, 2), (1, 3), (1, 4), (2, 4)])
    puzzle.add_between_line([(5, 6), (4, 6), (5, 5)])
    puzzle.add_between_line([(1, 5), (2, 6), (3, 5)])
    puzzle.add_between_line([(2, 3), (3, 3), (3, 2)])
    puzzle.add_between_line([(0, 0), (1, 0), (1, 1)])

    return puzzle
