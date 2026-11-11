"""PuzzleMadness Between Lines Sudoku — 2025-03-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 8, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 7, 0, 0, 1, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 2, 0, 3, 0, 0, 0, 6, 0],
        [1, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 5), (4, 5), (5, 4), (5, 3), (6, 2), (7, 1)])
    puzzle.add_between_line([(7, 6), (6, 7), (6, 6), (5, 7), (5, 8)])
    puzzle.add_between_line([(8, 3), (7, 2), (8, 1), (7, 0), (6, 0)])
    puzzle.add_between_line([(6, 4), (7, 4), (8, 4), (8, 5), (7, 5)])
    puzzle.add_between_line([(2, 2), (1, 3), (0, 3), (0, 4)])
    puzzle.add_between_line([(1, 8), (0, 7), (1, 7), (2, 8)])
    puzzle.add_between_line([(5, 6), (6, 5), (5, 5), (4, 6)])
    puzzle.add_between_line([(6, 8), (7, 8), (7, 7)])
    puzzle.add_between_line([(1, 0), (2, 1), (1, 1)])
    puzzle.add_between_line([(5, 0), (4, 1), (5, 2)])
    puzzle.add_between_line([(4, 7), (3, 8), (4, 8)])

    return puzzle
