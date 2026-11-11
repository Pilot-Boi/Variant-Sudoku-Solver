"""PuzzleMadness Between Lines Sudoku — 2025-08-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 7, 0, 0],
        [0, 4, 2, 0, 0, 0, 5, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 8, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (6, 3), (7, 4), (6, 4), (5, 5), (6, 5)])
    puzzle.add_between_line([(1, 1), (2, 1), (2, 0), (3, 1), (4, 0)])
    puzzle.add_between_line([(2, 5), (3, 5), (4, 5), (5, 6), (4, 7)])
    puzzle.add_between_line([(4, 2), (3, 3), (3, 2), (2, 3), (3, 4)])
    puzzle.add_between_line([(1, 8), (0, 8), (0, 7), (0, 6), (1, 6)])
    puzzle.add_between_line([(1, 5), (1, 4), (2, 4), (1, 3)])
    puzzle.add_between_line([(1, 7), (2, 7), (3, 8), (3, 7)])
    puzzle.add_between_line([(5, 2), (5, 1), (6, 1), (7, 2)])
    puzzle.add_between_line([(7, 6), (8, 5), (8, 6), (8, 7)])
    puzzle.add_between_line([(0, 1), (1, 0), (0, 0)])
    puzzle.add_between_line([(4, 4), (4, 3), (5, 3)])
    puzzle.add_between_line([(8, 2), (8, 3), (8, 4)])
    puzzle.add_between_line([(7, 1), (7, 0), (8, 1)])

    return puzzle
