"""PuzzleMadness Between Lines Sudoku — 2025-02-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 2, 3, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 8, 5],
        [6, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 6],
        [5, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 9, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 6), (4, 6), (3, 5), (4, 4), (5, 5), (5, 6)])
    puzzle.add_between_line([(7, 6), (7, 7), (6, 7), (5, 7), (6, 8)])
    puzzle.add_between_line([(6, 3), (7, 2), (8, 1), (7, 1), (7, 0)])
    puzzle.add_between_line([(8, 8), (7, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_between_line([(5, 4), (4, 3), (3, 2), (2, 1)])
    puzzle.add_between_line([(6, 5), (6, 4), (7, 3), (7, 4)])
    puzzle.add_between_line([(0, 7), (1, 8), (2, 8), (1, 7)])
    puzzle.add_between_line([(1, 2), (0, 2), (0, 1), (1, 1)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 7)])
    puzzle.add_between_line([(5, 1), (5, 0), (6, 1)])
    puzzle.add_between_line([(2, 3), (1, 4), (0, 4)])

    return puzzle
