"""PuzzleMadness Between Lines Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 7, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 1, 0, 0, 0, 0, 3],
        [0, 7, 0, 2, 4, 0, 0, 0, 1],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 2)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 4), (2, 4), (1, 5)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 2), (6, 1), (7, 0)])
    puzzle.add_between_line([(6, 5), (7, 6), (7, 5), (6, 4), (5, 5)])
    puzzle.add_between_line([(4, 0), (5, 1), (6, 2), (5, 2), (4, 2)])
    puzzle.add_between_line([(3, 2), (4, 1), (3, 0), (2, 1)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 8), (2, 8)])
    puzzle.add_between_line([(4, 7), (5, 8), (5, 7), (6, 8)])
    puzzle.add_between_line([(2, 5), (3, 5), (2, 6), (3, 7)])
    puzzle.add_between_line([(5, 4), (6, 3), (7, 4)])
    puzzle.add_between_line([(6, 7), (6, 6), (7, 7)])
    puzzle.add_between_line([(1, 3), (2, 2), (2, 3)])
    puzzle.add_between_line([(4, 3), (3, 4), (4, 4)])

    return puzzle
