"""PuzzleMadness Between Lines Sudoku — 2025-05-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 4, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 0, 0, 4, 6, 0, 0],
        [4, 0, 0, 0, 8, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 3), (1, 4), (2, 4), (2, 5), (1, 6), (1, 7)])
    puzzle.add_between_line([(2, 3), (3, 3), (4, 2), (3, 1), (3, 2)])
    puzzle.add_between_line([(5, 0), (5, 1), (5, 2), (6, 3), (6, 4)])
    puzzle.add_between_line([(5, 4), (4, 3), (4, 4), (3, 5), (2, 6)])
    puzzle.add_between_line([(5, 7), (6, 7), (6, 6), (7, 6)])
    puzzle.add_between_line([(4, 0), (4, 1), (3, 0), (2, 0)])
    puzzle.add_between_line([(8, 0), (7, 1), (7, 2), (8, 1)])
    puzzle.add_between_line([(1, 3), (1, 2), (1, 1)])
    puzzle.add_between_line([(8, 6), (8, 5), (7, 5)])
    puzzle.add_between_line([(3, 8), (2, 8), (1, 8)])

    return puzzle
