"""PuzzleMadness Between Lines Sudoku — 2025-07-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 6],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 6, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 7), (2, 7), (3, 6), (4, 7), (5, 8), (6, 8)])
    puzzle.add_between_line([(4, 2), (3, 2), (4, 1), (5, 1), (4, 0)])
    puzzle.add_between_line([(1, 6), (1, 5), (2, 4), (3, 4), (3, 5)])
    puzzle.add_between_line([(0, 6), (0, 5), (1, 4), (2, 3), (2, 2)])
    puzzle.add_between_line([(4, 3), (5, 3), (6, 2), (7, 2), (8, 1)])
    puzzle.add_between_line([(5, 4), (4, 5), (5, 6), (5, 7)])
    puzzle.add_between_line([(0, 1), (1, 0), (1, 1), (2, 0)])
    puzzle.add_between_line([(8, 6), (8, 5), (8, 4), (7, 5)])
    puzzle.add_between_line([(0, 3), (1, 3), (0, 4)])
    puzzle.add_between_line([(6, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(1, 2), (2, 1), (3, 0)])

    return puzzle
