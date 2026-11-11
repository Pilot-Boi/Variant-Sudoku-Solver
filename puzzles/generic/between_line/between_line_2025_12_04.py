"""PuzzleMadness Between Lines Sudoku — 2025-12-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 7, 8, 0, 0, 5, 0],
        [9, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 1, 6, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 9, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 6), (6, 5), (7, 4), (6, 4), (5, 5), (4, 6)])
    puzzle.add_between_line([(3, 0), (2, 1), (1, 1), (1, 0), (2, 0)])
    puzzle.add_between_line([(2, 6), (3, 6), (4, 5), (4, 4), (5, 3)])
    puzzle.add_between_line([(2, 3), (1, 2), (1, 3), (0, 3), (1, 4)])
    puzzle.add_between_line([(6, 8), (7, 8), (8, 7), (8, 6), (7, 7)])
    puzzle.add_between_line([(6, 6), (6, 7), (5, 8), (5, 7)])
    puzzle.add_between_line([(3, 8), (4, 7), (3, 7), (2, 8)])
    puzzle.add_between_line([(3, 4), (4, 3), (3, 2), (4, 2)])
    puzzle.add_between_line([(2, 4), (2, 5), (1, 6), (2, 7)])
    puzzle.add_between_line([(7, 0), (7, 1), (8, 1)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 7)])
    puzzle.add_between_line([(5, 1), (4, 1), (4, 0)])

    return puzzle
