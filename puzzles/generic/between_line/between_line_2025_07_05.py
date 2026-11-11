"""PuzzleMadness Between Lines Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 6, 0],
        [2, 0, 5, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 6, 0, 0, 8, 0, 1],
        [0, 0, 0, 0, 0, 0, 4, 0, 9],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 8), (1, 7), (2, 7), (3, 8), (4, 7), (3, 7)])
    puzzle.add_between_line([(3, 1), (3, 2), (2, 1), (1, 1), (0, 1)])
    puzzle.add_between_line([(7, 4), (7, 3), (6, 3), (5, 4), (6, 4)])
    puzzle.add_between_line([(1, 2), (2, 3), (1, 4), (0, 4), (1, 5)])
    puzzle.add_between_line([(5, 5), (4, 4), (4, 3), (4, 2)])
    puzzle.add_between_line([(3, 3), (3, 4), (3, 5), (4, 5)])
    puzzle.add_between_line([(6, 0), (7, 1), (8, 1), (8, 2)])
    puzzle.add_between_line([(8, 6), (7, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(7, 7), (6, 7), (6, 8)])
    puzzle.add_between_line([(6, 6), (5, 7), (5, 6)])
    puzzle.add_between_line([(4, 1), (5, 0), (5, 1)])
    puzzle.add_between_line([(2, 4), (2, 5), (1, 6)])

    return puzzle
