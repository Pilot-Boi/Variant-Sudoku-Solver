"""PuzzleMadness Between Lines Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 3, 4],
        [1, 0, 0, 8, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 8, 0, 0],
        [7, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 1, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 4), (5, 5), (4, 5), (3, 6), (4, 7), (5, 7)])
    puzzle.add_between_line([(3, 5), (2, 5), (3, 4), (4, 3), (5, 4)])
    puzzle.add_between_line([(7, 1), (6, 0), (6, 1), (5, 1), (4, 0)])
    puzzle.add_between_line([(1, 3), (2, 2), (2, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(1, 6), (2, 6), (2, 7), (3, 8), (2, 8)])
    puzzle.add_between_line([(2, 1), (1, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(0, 3), (1, 2), (0, 1), (0, 2)])
    puzzle.add_between_line([(8, 4), (7, 4), (6, 4), (6, 5)])
    puzzle.add_between_line([(5, 2), (4, 1), (3, 2)])
    puzzle.add_between_line([(7, 5), (6, 6), (7, 7)])
    puzzle.add_between_line([(8, 3), (7, 3), (6, 2)])
    puzzle.add_between_line([(1, 7), (0, 7), (0, 6)])

    return puzzle
