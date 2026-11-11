"""PuzzleMadness Between Lines Sudoku — 2025-01-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 1, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 2, 0, 3, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 6, 0],
        [0, 3, 0, 5, 0, 0, 8, 0, 0],
        [0, 0, 6, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 5), (6, 6), (6, 7), (5, 6), (5, 7), (4, 7)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(2, 7), (1, 7), (1, 8), (0, 7), (0, 6)])
    puzzle.add_between_line([(3, 8), (2, 8), (3, 7), (2, 6), (1, 6)])
    puzzle.add_between_line([(8, 2), (8, 3), (7, 2), (6, 1), (6, 0)])
    puzzle.add_between_line([(3, 2), (3, 3), (4, 4), (4, 3)])
    puzzle.add_between_line([(2, 4), (2, 5), (3, 5), (3, 4)])
    puzzle.add_between_line([(5, 3), (4, 2), (5, 1), (5, 0)])
    puzzle.add_between_line([(7, 3), (6, 3), (7, 4), (8, 4)])
    puzzle.add_between_line([(1, 2), (1, 1), (0, 0)])
    puzzle.add_between_line([(2, 2), (3, 1), (4, 0)])
    puzzle.add_between_line([(6, 4), (6, 5), (7, 5)])

    return puzzle
