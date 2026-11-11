"""PuzzleMadness Between Lines Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 0, 1],
        [6, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [7, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 8, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 3, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 8), (3, 8), (2, 8), (3, 7), (4, 7), (5, 6)])
    puzzle.add_between_line([(1, 5), (2, 4), (3, 3), (4, 3), (4, 4)])
    puzzle.add_between_line([(8, 5), (7, 4), (6, 4), (6, 5), (6, 6)])
    puzzle.add_between_line([(7, 3), (6, 2), (5, 2), (4, 2), (5, 1)])
    puzzle.add_between_line([(7, 2), (8, 1), (8, 0), (7, 1), (7, 0)])
    puzzle.add_between_line([(2, 6), (1, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(6, 3), (5, 4), (5, 5), (4, 6)])
    puzzle.add_between_line([(6, 7), (7, 7), (6, 8), (5, 7)])
    puzzle.add_between_line([(1, 1), (1, 2), (2, 2), (3, 2)])
    puzzle.add_between_line([(2, 1), (3, 0), (3, 1)])
    puzzle.add_between_line([(2, 3), (1, 3), (0, 3)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 0)])
    puzzle.add_between_line([(0, 7), (1, 6), (0, 6)])

    return puzzle
