"""PuzzleMadness Between Lines Sudoku — 2025-01-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 6, 2, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [9, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 4, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 3), (4, 4), (3, 3), (2, 2), (1, 2), (2, 3)])
    puzzle.add_between_line([(8, 7), (8, 8), (7, 8), (6, 8), (5, 8)])
    puzzle.add_between_line([(1, 5), (2, 6), (3, 7), (4, 6), (3, 5)])
    puzzle.add_between_line([(0, 3), (1, 3), (0, 2), (1, 1), (0, 1)])
    puzzle.add_between_line([(7, 6), (6, 6), (5, 6), (5, 5)])
    puzzle.add_between_line([(6, 5), (7, 4), (8, 5), (8, 6)])
    puzzle.add_between_line([(4, 3), (5, 2), (6, 1), (5, 1)])
    puzzle.add_between_line([(4, 2), (3, 2), (3, 1), (4, 1)])
    puzzle.add_between_line([(2, 4), (1, 4), (0, 5)])
    puzzle.add_between_line([(8, 4), (8, 3), (8, 2)])
    puzzle.add_between_line([(3, 8), (2, 8), (2, 7)])
    puzzle.add_between_line([(3, 0), (2, 0), (2, 1)])

    return puzzle
