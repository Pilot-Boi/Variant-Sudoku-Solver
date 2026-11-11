"""PuzzleMadness Between Lines Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 6, 0, 9, 0, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 8), (7, 7), (8, 7), (7, 6), (8, 5), (7, 4)])
    puzzle.add_between_line([(1, 8), (0, 8), (1, 7), (2, 8), (2, 7)])
    puzzle.add_between_line([(8, 0), (7, 1), (6, 2), (5, 2), (4, 3)])
    puzzle.add_between_line([(5, 4), (4, 5), (4, 4), (3, 5), (2, 5)])
    puzzle.add_between_line([(3, 0), (3, 1), (4, 1), (4, 0)])
    puzzle.add_between_line([(1, 0), (2, 0), (2, 1), (1, 1)])
    puzzle.add_between_line([(5, 6), (4, 7), (4, 8), (3, 7)])
    puzzle.add_between_line([(6, 3), (7, 2), (7, 3), (8, 4)])
    puzzle.add_between_line([(7, 0), (6, 0), (5, 0)])
    puzzle.add_between_line([(0, 2), (1, 2), (1, 3)])
    puzzle.add_between_line([(6, 4), (6, 5), (5, 5)])

    return puzzle
