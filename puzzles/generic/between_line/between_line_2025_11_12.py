"""PuzzleMadness Between Lines Sudoku — 2025-11-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 1, 0, 0, 0],
        [3, 0, 0, 0, 9, 0, 0, 5, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 8, 6, 0, 0],
        [0, 0, 0, 0, 2, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 3, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 2), (0, 1), (0, 0), (1, 0), (1, 1), (2, 0)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 7), (5, 7), (6, 8)])
    puzzle.add_between_line([(8, 6), (7, 6), (6, 6), (6, 5), (7, 4)])
    puzzle.add_between_line([(2, 1), (2, 2), (1, 3), (2, 3), (1, 4)])
    puzzle.add_between_line([(4, 1), (4, 2), (3, 2), (3, 3)])
    puzzle.add_between_line([(5, 8), (4, 8), (4, 7), (4, 6)])
    puzzle.add_between_line([(4, 0), (5, 1), (5, 2), (5, 3)])
    puzzle.add_between_line([(1, 6), (0, 6), (1, 7), (2, 6)])
    puzzle.add_between_line([(3, 4), (4, 3), (4, 4)])
    puzzle.add_between_line([(8, 3), (7, 2), (8, 2)])
    puzzle.add_between_line([(3, 8), (2, 8), (3, 7)])
    puzzle.add_between_line([(6, 3), (7, 3), (6, 2)])

    return puzzle
