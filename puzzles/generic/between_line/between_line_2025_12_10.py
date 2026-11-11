"""PuzzleMadness Between Lines Sudoku — 2025-12-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 3, 2, 0, 8, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 3, 0, 0, 7, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 2],
        [8, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 8), (7, 8), (7, 7), (6, 6), (5, 5), (5, 6)])
    puzzle.add_between_line([(4, 5), (3, 5), (2, 4), (2, 5), (1, 6)])
    puzzle.add_between_line([(2, 6), (1, 7), (1, 8), (2, 8), (3, 8)])
    puzzle.add_between_line([(1, 5), (0, 5), (0, 4), (0, 3), (1, 4)])
    puzzle.add_between_line([(8, 4), (8, 3), (7, 4), (6, 3), (7, 2)])
    puzzle.add_between_line([(8, 5), (7, 6), (8, 7), (8, 6)])
    puzzle.add_between_line([(3, 7), (3, 6), (4, 7), (4, 6)])
    puzzle.add_between_line([(5, 4), (6, 4), (5, 3), (4, 4)])
    puzzle.add_between_line([(4, 0), (5, 1), (5, 0)])
    puzzle.add_between_line([(5, 2), (4, 2), (3, 1)])
    puzzle.add_between_line([(2, 0), (1, 1), (2, 1)])
    puzzle.add_between_line([(5, 7), (5, 8), (6, 8)])

    return puzzle
