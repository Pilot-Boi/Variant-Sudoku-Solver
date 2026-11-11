"""PuzzleMadness Between Lines Sudoku — 2025-03-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 8, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 8, 0, 0, 3],
        [2, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 5, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (3, 2)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 7), (5, 7), (5, 6)])
    puzzle.add_between_line([(2, 3), (2, 2), (1, 1), (1, 2), (1, 3)])
    puzzle.add_between_line([(0, 7), (1, 7), (0, 8), (1, 8), (2, 8)])
    puzzle.add_between_line([(8, 2), (7, 2), (6, 2), (5, 1), (4, 2)])
    puzzle.add_between_line([(4, 4), (5, 5), (6, 4), (7, 3)])
    puzzle.add_between_line([(3, 4), (2, 5), (1, 6), (1, 5)])
    puzzle.add_between_line([(8, 6), (7, 6), (7, 7), (8, 7)])
    puzzle.add_between_line([(4, 8), (5, 8), (4, 7)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 1)])
    puzzle.add_between_line([(2, 7), (3, 6), (4, 6)])

    return puzzle
