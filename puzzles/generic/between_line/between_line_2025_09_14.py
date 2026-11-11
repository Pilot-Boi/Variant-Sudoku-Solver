"""PuzzleMadness Between Lines Sudoku — 2025-09-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 8, 7, 0, 1, 0, 9],
        [0, 8, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 6, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 5), (5, 5), (6, 4), (7, 5), (8, 5), (8, 4)])
    puzzle.add_between_line([(1, 4), (2, 4), (1, 3), (1, 2), (2, 3)])
    puzzle.add_between_line([(3, 0), (4, 1), (3, 2), (2, 1), (1, 0)])
    puzzle.add_between_line([(4, 4), (3, 4), (2, 5), (1, 6), (0, 6)])
    puzzle.add_between_line([(4, 5), (5, 6), (4, 7), (4, 6)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (2, 2)])
    puzzle.add_between_line([(2, 7), (1, 7), (1, 8), (0, 8)])
    puzzle.add_between_line([(3, 3), (4, 2), (4, 3), (5, 3)])
    puzzle.add_between_line([(8, 6), (7, 7), (8, 7)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 0)])
    puzzle.add_between_line([(7, 2), (6, 2), (6, 3)])
    puzzle.add_between_line([(4, 0), (5, 0), (5, 1)])

    return puzzle
