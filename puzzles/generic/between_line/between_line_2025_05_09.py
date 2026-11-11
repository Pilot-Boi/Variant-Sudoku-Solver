"""PuzzleMadness Between Lines Sudoku — 2025-05-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 8, 3, 0, 2, 0, 0, 0],
        [7, 0, 0, 0, 6, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [8, 0, 0, 0, 4, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 6), (4, 7), (5, 8), (6, 7), (7, 7), (8, 7)])
    puzzle.add_between_line([(1, 5), (2, 4), (3, 3), (4, 3), (4, 4)])
    puzzle.add_between_line([(1, 3), (2, 2), (3, 1), (4, 1), (5, 0)])
    puzzle.add_between_line([(3, 8), (3, 7), (3, 6), (2, 6), (1, 7)])
    puzzle.add_between_line([(5, 2), (6, 1), (7, 0), (8, 0)])
    puzzle.add_between_line([(8, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_between_line([(8, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_between_line([(2, 1), (1, 2), (0, 3)])
    puzzle.add_between_line([(4, 2), (5, 1), (6, 0)])
    puzzle.add_between_line([(0, 5), (0, 6), (1, 6)])
    puzzle.add_between_line([(3, 5), (2, 5), (3, 4)])

    return puzzle
