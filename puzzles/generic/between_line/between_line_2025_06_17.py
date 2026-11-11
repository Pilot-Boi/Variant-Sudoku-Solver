"""PuzzleMadness Between Lines Sudoku — 2025-06-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 5, 6, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 8, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 1, 0],
        [1, 9, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 1), (2, 1), (3, 2), (4, 2), (5, 3), (4, 3)])
    puzzle.add_between_line([(6, 0), (7, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_between_line([(5, 5), (4, 4), (3, 5), (3, 6), (4, 5)])
    puzzle.add_between_line([(0, 1), (1, 2), (0, 2), (1, 3), (0, 3)])
    puzzle.add_between_line([(2, 2), (3, 3), (3, 4), (2, 3), (1, 4)])
    puzzle.add_between_line([(0, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_between_line([(6, 3), (6, 2), (7, 3), (7, 4)])
    puzzle.add_between_line([(5, 1), (5, 0), (4, 0), (3, 0)])
    puzzle.add_between_line([(3, 7), (2, 6), (1, 7), (2, 7)])
    puzzle.add_between_line([(0, 5), (1, 5), (0, 4)])
    puzzle.add_between_line([(5, 6), (4, 7), (3, 8)])
    puzzle.add_between_line([(8, 6), (7, 5), (7, 6)])
    puzzle.add_between_line([(8, 0), (7, 0), (8, 1)])

    return puzzle
