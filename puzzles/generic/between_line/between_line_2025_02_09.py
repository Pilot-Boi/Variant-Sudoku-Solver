"""PuzzleMadness Between Lines Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 3, 0],
        [1, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 8, 5, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 6, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 5), (5, 6), (4, 6), (5, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(7, 0), (8, 1), (8, 2), (7, 1), (6, 2)])
    puzzle.add_between_line([(1, 3), (2, 2), (3, 2), (2, 1), (1, 1)])
    puzzle.add_between_line([(5, 8), (6, 8), (6, 7), (7, 7), (8, 6)])
    puzzle.add_between_line([(4, 4), (3, 3), (2, 4), (1, 4), (0, 4)])
    puzzle.add_between_line([(3, 8), (2, 7), (1, 8), (2, 8)])
    puzzle.add_between_line([(4, 0), (3, 1), (4, 1), (5, 1)])
    puzzle.add_between_line([(4, 3), (5, 2), (6, 1), (6, 0)])
    puzzle.add_between_line([(0, 7), (0, 8), (1, 7)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(0, 5), (1, 6), (2, 5)])
    puzzle.add_between_line([(6, 6), (6, 5), (6, 4)])

    return puzzle
