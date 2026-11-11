"""PuzzleMadness Between Lines Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 9, 5, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 5, 0, 0, 0, 3, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 2, 0],
        [0, 7, 2, 3, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (0, 2), (1, 1), (2, 1), (1, 2), (2, 2)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 1), (4, 2), (3, 1)])
    puzzle.add_between_line([(5, 7), (6, 8), (7, 7), (8, 7), (7, 8)])
    puzzle.add_between_line([(5, 5), (4, 4), (5, 4), (6, 4), (7, 4)])
    puzzle.add_between_line([(0, 5), (1, 4), (2, 5), (3, 6)])
    puzzle.add_between_line([(6, 1), (7, 1), (7, 2), (8, 1)])
    puzzle.add_between_line([(3, 2), (3, 3), (2, 3), (2, 4)])
    puzzle.add_between_line([(5, 6), (4, 7), (3, 8)])
    puzzle.add_between_line([(8, 3), (8, 2), (7, 3)])
    puzzle.add_between_line([(3, 0), (2, 0), (1, 0)])

    return puzzle
