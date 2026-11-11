"""PuzzleMadness Between Lines Sudoku — 2025-11-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 3, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 3, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 1, 0, 7, 0, 0, 3],
        [0, 9, 0, 5, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 5, 0],
        [1, 0, 7, 4, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 8), (1, 7), (1, 8), (2, 7), (2, 6), (1, 6)])
    puzzle.add_between_line([(4, 7), (4, 8), (3, 7), (4, 6), (5, 7)])
    puzzle.add_between_line([(5, 2), (4, 1), (3, 1), (3, 0), (4, 0)])
    puzzle.add_between_line([(5, 6), (6, 7), (7, 7), (8, 8), (7, 8)])
    puzzle.add_between_line([(3, 2), (2, 3), (1, 3), (0, 4)])
    puzzle.add_between_line([(5, 4), (5, 3), (6, 4), (6, 5)])
    puzzle.add_between_line([(2, 0), (1, 0), (1, 1), (2, 2)])
    puzzle.add_between_line([(7, 3), (6, 3), (7, 4), (8, 3)])
    puzzle.add_between_line([(6, 1), (7, 2), (7, 1)])
    puzzle.add_between_line([(3, 4), (3, 3), (4, 4)])
    puzzle.add_between_line([(8, 7), (8, 6), (7, 6)])

    return puzzle
