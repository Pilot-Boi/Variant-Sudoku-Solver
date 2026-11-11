"""PuzzleMadness Between Lines Sudoku — 2025-11-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 3, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 6, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 2), (4, 1), (3, 2), (4, 3), (4, 4), (4, 5)])
    puzzle.add_between_line([(1, 8), (2, 8), (2, 7), (2, 6), (1, 7)])
    puzzle.add_between_line([(3, 8), (4, 7), (5, 6), (6, 5), (5, 4)])
    puzzle.add_between_line([(7, 8), (6, 7), (7, 6), (8, 6), (7, 7)])
    puzzle.add_between_line([(5, 0), (6, 0), (7, 0), (6, 1), (6, 2)])
    puzzle.add_between_line([(1, 6), (1, 5), (2, 5), (3, 6)])
    puzzle.add_between_line([(3, 7), (4, 6), (3, 5), (2, 4)])
    puzzle.add_between_line([(2, 2), (3, 3), (2, 3), (1, 3)])
    puzzle.add_between_line([(7, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(7, 1), (8, 1), (8, 2)])
    puzzle.add_between_line([(7, 3), (6, 4), (6, 3)])

    return puzzle
