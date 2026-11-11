"""PuzzleMadness Between Lines Sudoku — 2025-11-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 2, 4, 9],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 5, 0, 0],
        [3, 1, 0, 7, 0, 0, 0, 0, 0],
        [0, 5, 0, 8, 0, 0, 0, 6, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 6, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 8), (8, 7), (8, 6), (7, 5), (6, 5), (6, 4)])
    puzzle.add_between_line([(6, 7), (5, 7), (6, 6), (7, 7), (7, 6)])
    puzzle.add_between_line([(1, 5), (0, 4), (1, 4), (1, 3), (2, 3)])
    puzzle.add_between_line([(2, 8), (2, 7), (3, 6), (4, 7), (3, 7)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 2), (2, 1)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 3), (7, 2)])
    puzzle.add_between_line([(4, 6), (5, 6), (5, 5), (4, 4)])
    puzzle.add_between_line([(3, 2), (4, 2), (3, 1)])
    puzzle.add_between_line([(5, 3), (6, 2), (6, 3)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 7)])

    return puzzle
