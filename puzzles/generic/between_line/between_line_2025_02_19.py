"""PuzzleMadness Between Lines Sudoku — 2025-02-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 8, 7, 0, 3, 4, 1, 0, 0],
        [0, 0, 5, 6, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [5, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 5), (6, 6), (5, 7), (4, 6), (3, 5), (2, 4)])
    puzzle.add_between_line([(0, 4), (1, 4), (1, 5), (0, 6), (1, 6)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 1), (1, 1), (1, 2)])
    puzzle.add_between_line([(8, 6), (8, 5), (8, 4), (7, 3), (7, 2)])
    puzzle.add_between_line([(5, 2), (6, 1), (7, 0), (7, 1), (8, 2)])
    puzzle.add_between_line([(4, 7), (4, 8), (5, 8), (6, 7)])
    puzzle.add_between_line([(1, 3), (2, 2), (3, 1), (4, 1)])
    puzzle.add_between_line([(7, 4), (6, 4), (5, 4), (4, 3)])
    puzzle.add_between_line([(2, 8), (3, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(4, 5), (3, 4), (4, 4)])
    puzzle.add_between_line([(7, 7), (8, 7), (7, 6)])
    puzzle.add_between_line([(2, 1), (3, 0), (4, 0)])

    return puzzle
