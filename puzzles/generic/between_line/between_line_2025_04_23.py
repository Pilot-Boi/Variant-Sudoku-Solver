"""PuzzleMadness Between Lines Sudoku — 2025-04-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 7, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 8, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 3, 2, 0, 0, 1, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 1), (3, 2), (4, 1), (5, 0), (4, 0), (3, 0)])
    puzzle.add_between_line([(5, 4), (6, 3), (6, 4), (7, 3), (8, 3)])
    puzzle.add_between_line([(6, 7), (5, 7), (6, 6), (7, 5), (7, 6)])
    puzzle.add_between_line([(2, 7), (2, 6), (2, 5), (1, 5), (1, 6)])
    puzzle.add_between_line([(5, 6), (4, 5), (4, 4), (5, 5)])
    puzzle.add_between_line([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_between_line([(5, 2), (6, 1), (7, 1), (6, 2)])
    puzzle.add_between_line([(6, 5), (7, 4), (8, 4), (8, 5)])
    puzzle.add_between_line([(6, 0), (5, 1), (4, 2)])
    puzzle.add_between_line([(3, 4), (3, 5), (2, 4)])
    puzzle.add_between_line([(0, 8), (1, 8), (2, 8)])
    puzzle.add_between_line([(4, 6), (3, 7), (4, 7)])

    return puzzle
