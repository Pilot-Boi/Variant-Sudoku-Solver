"""PuzzleMadness Between Lines Sudoku — 2025-11-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 7, 0, 0],
        [0, 6, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 5, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 8, 2],
        [0, 0, 0, 9, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 3), (7, 4), (6, 5), (6, 6), (5, 7), (6, 8)])
    puzzle.add_between_line([(2, 0), (2, 1), (3, 2), (2, 2), (2, 3)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 5), (0, 6), (0, 5)])
    puzzle.add_between_line([(3, 8), (3, 7), (4, 6), (3, 5), (3, 4)])
    puzzle.add_between_line([(1, 8), (2, 7), (1, 7), (0, 7)])
    puzzle.add_between_line([(8, 8), (8, 7), (8, 6), (7, 6)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 2), (1, 3)])
    puzzle.add_between_line([(4, 1), (3, 1), (4, 2)])
    puzzle.add_between_line([(3, 3), (4, 3), (5, 3)])
    puzzle.add_between_line([(6, 1), (7, 0), (7, 1)])

    return puzzle
