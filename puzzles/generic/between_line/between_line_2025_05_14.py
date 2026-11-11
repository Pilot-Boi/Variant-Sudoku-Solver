"""PuzzleMadness Between Lines Sudoku — 2025-05-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 8, 0, 7, 0],
        [0, 7, 0, 1, 4, 0, 0, 5, 0],
        [0, 5, 0, 0, 0, 6, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 8, 7, 3, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 3), (1, 3), (1, 4), (1, 5), (0, 6), (0, 5)])
    puzzle.add_between_line([(5, 0), (6, 1), (6, 2), (6, 3), (5, 3)])
    puzzle.add_between_line([(4, 3), (3, 2), (3, 1), (2, 0), (1, 0)])
    puzzle.add_between_line([(6, 0), (7, 0), (8, 0), (8, 1), (7, 1)])
    puzzle.add_between_line([(8, 5), (8, 6), (7, 5), (7, 4), (8, 4)])
    puzzle.add_between_line([(4, 8), (4, 7), (4, 6), (3, 6)])
    puzzle.add_between_line([(2, 6), (3, 5), (3, 4), (3, 3)])
    puzzle.add_between_line([(6, 4), (5, 5), (6, 6), (7, 7)])
    puzzle.add_between_line([(3, 7), (2, 7), (1, 6)])
    puzzle.add_between_line([(5, 2), (4, 1), (5, 1)])
    puzzle.add_between_line([(6, 7), (5, 7), (6, 8)])

    return puzzle
