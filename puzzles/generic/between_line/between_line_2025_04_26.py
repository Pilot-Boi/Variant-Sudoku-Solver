"""PuzzleMadness Between Lines Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 5, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 2],
        [3, 4, 0, 0, 0, 0, 0, 9, 0],
        [0, 5, 6, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 2, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 6), (5, 7), (5, 6), (6, 6), (7, 6), (8, 6)])
    puzzle.add_between_line([(1, 4), (0, 5), (0, 6), (1, 5), (2, 6)])
    puzzle.add_between_line([(8, 1), (7, 0), (7, 1), (6, 1), (5, 0)])
    puzzle.add_between_line([(7, 2), (7, 3), (8, 4), (7, 4), (6, 4)])
    puzzle.add_between_line([(8, 7), (7, 7), (6, 7), (7, 8)])
    puzzle.add_between_line([(0, 8), (1, 7), (1, 8), (2, 8)])
    puzzle.add_between_line([(2, 3), (2, 2), (1, 3), (0, 4)])
    puzzle.add_between_line([(4, 2), (5, 3), (4, 3)])
    puzzle.add_between_line([(3, 5), (3, 4), (2, 4)])
    puzzle.add_between_line([(1, 0), (0, 0), (1, 1)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 6)])

    return puzzle
