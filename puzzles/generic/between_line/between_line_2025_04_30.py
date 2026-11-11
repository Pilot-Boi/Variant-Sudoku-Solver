"""PuzzleMadness Between Lines Sudoku — 2025-04-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 3],
        [0, 0, 0, 1, 0, 3, 0, 0, 7],
        [3, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 2, 0, 0, 6],
        [7, 6, 0, 0, 0, 0, 0, 9, 1],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 4), (4, 3), (5, 3), (6, 4), (5, 4), (6, 5)])
    puzzle.add_between_line([(8, 5), (7, 5), (7, 6), (7, 7), (8, 8)])
    puzzle.add_between_line([(5, 6), (4, 5), (3, 6), (2, 5), (2, 6)])
    puzzle.add_between_line([(1, 8), (2, 8), (3, 8), (3, 7), (4, 6)])
    puzzle.add_between_line([(0, 7), (0, 6), (0, 5), (0, 4), (0, 3)])
    puzzle.add_between_line([(2, 1), (3, 0), (4, 1), (5, 0)])
    puzzle.add_between_line([(2, 4), (1, 3), (0, 2), (0, 1)])
    puzzle.add_between_line([(6, 8), (5, 7), (4, 7), (4, 8)])
    puzzle.add_between_line([(4, 2), (3, 2), (3, 3)])
    puzzle.add_between_line([(8, 2), (7, 1), (7, 2)])
    puzzle.add_between_line([(7, 4), (8, 3), (8, 4)])
    puzzle.add_between_line([(1, 7), (2, 7), (1, 6)])

    return puzzle
