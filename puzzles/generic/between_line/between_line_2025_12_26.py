"""PuzzleMadness Between Lines Sudoku — 2025-12-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 7, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 1, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 0), (8, 1), (7, 0), (6, 1), (6, 2), (7, 2)])
    puzzle.add_between_line([(4, 5), (5, 6), (6, 5), (5, 4), (6, 4)])
    puzzle.add_between_line([(2, 3), (3, 4), (3, 3), (2, 2), (1, 1)])
    puzzle.add_between_line([(2, 7), (1, 8), (1, 7), (1, 6), (2, 6)])
    puzzle.add_between_line([(4, 2), (3, 2), (4, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(3, 5), (2, 5), (3, 6), (4, 7)])
    puzzle.add_between_line([(8, 8), (7, 7), (7, 8), (6, 8)])
    puzzle.add_between_line([(8, 4), (7, 4), (7, 5), (8, 6)])
    puzzle.add_between_line([(6, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_between_line([(1, 0), (0, 0), (0, 1)])
    puzzle.add_between_line([(3, 0), (3, 1), (4, 1)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 5)])

    return puzzle
