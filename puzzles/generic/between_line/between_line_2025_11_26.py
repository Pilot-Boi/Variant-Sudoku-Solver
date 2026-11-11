"""PuzzleMadness Between Lines Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 6, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 4, 0, 0],
        [9, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (4, 4), (5, 3), (6, 3), (6, 2), (7, 1)])
    puzzle.add_between_line([(1, 1), (1, 0), (0, 0), (0, 1), (0, 2)])
    puzzle.add_between_line([(6, 6), (5, 5), (5, 6), (5, 7), (5, 8)])
    puzzle.add_between_line([(3, 3), (2, 4), (3, 5), (4, 6), (3, 7)])
    puzzle.add_between_line([(3, 1), (4, 1), (3, 2), (2, 2), (2, 3)])
    puzzle.add_between_line([(4, 2), (5, 2), (5, 1), (4, 0)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 2), (8, 2)])
    puzzle.add_between_line([(2, 5), (1, 5), (0, 5), (1, 4)])
    puzzle.add_between_line([(8, 6), (7, 7), (6, 8)])
    puzzle.add_between_line([(3, 0), (2, 1), (2, 0)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 7)])

    return puzzle
