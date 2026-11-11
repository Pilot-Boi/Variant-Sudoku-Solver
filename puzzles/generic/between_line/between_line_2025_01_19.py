"""PuzzleMadness Between Lines Sudoku — 2025-01-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 7, 0, 9, 0, 0, 0],
        [6, 0, 0, 4, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 2],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [8, 0, 4, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 6), (0, 5), (1, 6), (2, 6), (1, 5), (2, 5)])
    puzzle.add_between_line([(1, 4), (2, 4), (1, 3), (2, 2), (1, 1)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1), (3, 2), (3, 3)])
    puzzle.add_between_line([(7, 7), (8, 8), (8, 7), (7, 6), (6, 7)])
    puzzle.add_between_line([(4, 1), (4, 2), (4, 3), (5, 4), (6, 3)])
    puzzle.add_between_line([(7, 2), (8, 3), (7, 4), (8, 4)])
    puzzle.add_between_line([(6, 0), (5, 1), (4, 0), (3, 1)])
    puzzle.add_between_line([(3, 5), (3, 6), (4, 5), (3, 4)])
    puzzle.add_between_line([(1, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(5, 8), (4, 7), (4, 8)])
    puzzle.add_between_line([(5, 7), (6, 6), (7, 5)])
    puzzle.add_between_line([(2, 8), (3, 7), (3, 8)])

    return puzzle
