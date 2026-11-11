"""PuzzleMadness Between Lines Sudoku — 2025-01-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 6, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 0, 0, 0, 2, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 3, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 7), (8, 6), (7, 7), (6, 7), (5, 8), (4, 8)])
    puzzle.add_between_line([(6, 0), (6, 1), (5, 2), (5, 3), (6, 3)])
    puzzle.add_between_line([(7, 1), (6, 2), (7, 3), (6, 4), (5, 5)])
    puzzle.add_between_line([(5, 7), (5, 6), (4, 5), (3, 5), (4, 6)])
    puzzle.add_between_line([(0, 5), (1, 6), (2, 5), (3, 6), (4, 7)])
    puzzle.add_between_line([(7, 6), (7, 5), (7, 4), (8, 5)])
    puzzle.add_between_line([(1, 7), (0, 6), (0, 7), (0, 8)])
    puzzle.add_between_line([(0, 1), (1, 2), (1, 1), (0, 0)])
    puzzle.add_between_line([(3, 2), (2, 1), (3, 0)])
    puzzle.add_between_line([(2, 8), (3, 7), (2, 6)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4)])
    puzzle.add_between_line([(5, 0), (4, 1), (5, 1)])

    return puzzle
