"""PuzzleMadness Between Lines Sudoku — 2025-07-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 0, 0, 1],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 2), (4, 2), (5, 1), (4, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(3, 2), (2, 2), (3, 3), (2, 3), (1, 3)])
    puzzle.add_between_line([(2, 1), (1, 2), (0, 2), (0, 3), (1, 4)])
    puzzle.add_between_line([(6, 1), (7, 0), (8, 1), (7, 1), (7, 2)])
    puzzle.add_between_line([(4, 4), (3, 4), (2, 4), (1, 5)])
    puzzle.add_between_line([(1, 1), (0, 1), (1, 0), (2, 0)])
    puzzle.add_between_line([(6, 6), (7, 7), (7, 6), (8, 6)])
    puzzle.add_between_line([(6, 2), (5, 3), (6, 3)])
    puzzle.add_between_line([(6, 5), (6, 4), (7, 3)])
    puzzle.add_between_line([(4, 6), (5, 5), (4, 5)])

    return puzzle
