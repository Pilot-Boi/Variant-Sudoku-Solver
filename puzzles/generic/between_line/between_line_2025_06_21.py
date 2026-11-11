"""PuzzleMadness Between Lines Sudoku — 2025-06-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 1, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 6, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 4],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 2), (3, 1), (4, 0), (5, 1), (6, 0), (5, 0)])
    puzzle.add_between_line([(1, 4), (1, 3), (0, 3), (1, 2), (0, 2)])
    puzzle.add_between_line([(2, 6), (3, 5), (4, 4), (3, 4), (3, 3)])
    puzzle.add_between_line([(0, 7), (1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_between_line([(6, 4), (5, 4), (4, 5), (3, 6), (3, 7)])
    puzzle.add_between_line([(4, 7), (4, 6), (5, 5), (6, 6)])
    puzzle.add_between_line([(2, 5), (1, 6), (0, 5), (0, 4)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0), (2, 0)])
    puzzle.add_between_line([(4, 1), (5, 2), (6, 2)])
    puzzle.add_between_line([(5, 6), (5, 7), (6, 8)])
    puzzle.add_between_line([(8, 6), (8, 7), (7, 6)])
    puzzle.add_between_line([(8, 3), (7, 4), (8, 5)])

    return puzzle
