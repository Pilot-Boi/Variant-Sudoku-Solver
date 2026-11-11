"""PuzzleMadness Between Lines Sudoku — 2025-11-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 7, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 3, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 2, 0, 0],
        [4, 0, 8, 0, 0, 0, 0, 0, 0],
        [7, 5, 0, 0, 8, 0, 0, 9, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 1), (8, 0), (7, 1), (7, 0), (6, 1), (6, 2)])
    puzzle.add_between_line([(4, 1), (4, 2), (5, 1), (5, 2), (5, 3)])
    puzzle.add_between_line([(6, 3), (5, 4), (4, 5), (3, 6), (4, 6)])
    puzzle.add_between_line([(1, 4), (0, 3), (1, 2), (2, 1), (3, 1)])
    puzzle.add_between_line([(1, 7), (2, 6), (1, 6), (2, 5)])
    puzzle.add_between_line([(3, 0), (2, 0), (1, 1), (0, 0)])
    puzzle.add_between_line([(6, 7), (5, 7), (6, 8), (7, 7)])
    puzzle.add_between_line([(4, 8), (5, 8), (4, 7), (3, 8)])
    puzzle.add_between_line([(0, 7), (0, 8), (1, 8)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 4)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 5)])
    puzzle.add_between_line([(2, 3), (3, 3), (4, 3)])

    return puzzle
