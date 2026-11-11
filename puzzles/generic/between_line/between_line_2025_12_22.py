"""PuzzleMadness Between Lines Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 8, 0, 0, 0],
        [3, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 2],
        [0, 0, 5, 3, 8, 0, 7, 0, 6],
        [2, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (4, 4), (3, 3), (2, 2), (3, 2), (3, 1)])
    puzzle.add_between_line([(4, 2), (4, 1), (4, 0), (5, 1), (6, 0)])
    puzzle.add_between_line([(8, 6), (7, 7), (6, 6), (6, 7), (6, 8)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4), (6, 3), (6, 4)])
    puzzle.add_between_line([(2, 3), (2, 4), (3, 5), (2, 6)])
    puzzle.add_between_line([(8, 1), (7, 0), (7, 1), (8, 2)])
    puzzle.add_between_line([(1, 1), (1, 0), (2, 1), (1, 2)])
    puzzle.add_between_line([(0, 1), (0, 2), (0, 3), (1, 3)])
    puzzle.add_between_line([(5, 2), (5, 3), (4, 3)])
    puzzle.add_between_line([(6, 5), (5, 6), (4, 6)])
    puzzle.add_between_line([(3, 4), (4, 5), (5, 5)])

    return puzzle
