"""PuzzleMadness Between Lines Sudoku — 2025-02-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 6, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [5, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 7, 2, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 3],
        [8, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 7, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 7), (2, 7), (2, 8), (1, 8), (0, 8), (1, 7)])
    puzzle.add_between_line([(4, 5), (5, 6), (4, 7), (4, 8), (3, 8)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 1), (2, 2), (3, 1)])
    puzzle.add_between_line([(7, 8), (6, 8), (7, 7), (8, 7), (8, 8)])
    puzzle.add_between_line([(7, 6), (8, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(5, 8), (5, 7), (6, 6), (5, 5)])
    puzzle.add_between_line([(6, 3), (5, 3), (4, 2), (3, 2)])
    puzzle.add_between_line([(6, 4), (7, 4), (7, 3)])
    puzzle.add_between_line([(1, 4), (2, 5), (1, 6)])
    puzzle.add_between_line([(4, 3), (5, 4), (4, 4)])

    return puzzle
