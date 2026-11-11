"""PuzzleMadness Between Lines Sudoku — 2025-12-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 5, 3, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [8, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 3), (6, 2), (6, 3), (5, 4), (6, 4), (6, 5)])
    puzzle.add_between_line([(2, 1), (3, 0), (2, 0), (1, 1), (1, 2)])
    puzzle.add_between_line([(4, 2), (3, 2), (2, 3), (1, 4), (0, 5)])
    puzzle.add_between_line([(3, 5), (4, 5), (3, 6), (4, 7), (3, 7)])
    puzzle.add_between_line([(7, 0), (8, 1), (7, 1), (8, 2), (7, 3)])
    puzzle.add_between_line([(7, 5), (6, 6), (7, 6), (8, 6)])
    puzzle.add_between_line([(1, 6), (0, 6), (1, 5), (2, 5)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 8), (5, 7)])
    puzzle.add_between_line([(7, 2), (6, 1), (6, 0)])
    puzzle.add_between_line([(3, 1), (4, 1), (4, 0)])
    puzzle.add_between_line([(4, 6), (5, 5), (5, 6)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4)])

    return puzzle
