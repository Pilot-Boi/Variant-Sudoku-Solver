"""PuzzleMadness Between Lines Sudoku — 2025-12-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 1, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [2, 6, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 2), (2, 3), (2, 2), (1, 3), (0, 2), (1, 1)])
    puzzle.add_between_line([(7, 7), (6, 7), (7, 6), (8, 5), (7, 4)])
    puzzle.add_between_line([(0, 6), (1, 6), (1, 7), (0, 8), (0, 7)])
    puzzle.add_between_line([(4, 0), (5, 1), (4, 2), (3, 1), (4, 1)])
    puzzle.add_between_line([(6, 1), (7, 2), (6, 3), (5, 3), (4, 3)])
    puzzle.add_between_line([(8, 4), (8, 3), (7, 3), (6, 4)])
    puzzle.add_between_line([(5, 8), (4, 7), (5, 6), (5, 7)])
    puzzle.add_between_line([(4, 5), (3, 6), (2, 5), (2, 6)])
    puzzle.add_between_line([(7, 1), (8, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 8)])
    puzzle.add_between_line([(7, 5), (6, 5), (6, 6)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0)])

    return puzzle
