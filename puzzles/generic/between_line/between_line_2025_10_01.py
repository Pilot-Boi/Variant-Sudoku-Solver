"""PuzzleMadness Between Lines Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 7, 0],
        [0, 5, 0, 9, 0, 0, 0, 8, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 6, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 0), (0, 1), (1, 2), (1, 3), (2, 2), (3, 3)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 6), (2, 7), (1, 7)])
    puzzle.add_between_line([(3, 1), (4, 1), (5, 0), (6, 0), (7, 0)])
    puzzle.add_between_line([(3, 5), (3, 4), (4, 5), (5, 4), (6, 3)])
    puzzle.add_between_line([(8, 4), (7, 4), (6, 5), (5, 6)])
    puzzle.add_between_line([(6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_between_line([(2, 8), (3, 8), (4, 8), (3, 7)])
    puzzle.add_between_line([(5, 8), (5, 7), (4, 7), (3, 6)])
    puzzle.add_between_line([(4, 3), (5, 3), (4, 4)])
    puzzle.add_between_line([(5, 2), (5, 1), (6, 2)])
    puzzle.add_between_line([(7, 7), (8, 8), (7, 8)])
    puzzle.add_between_line([(6, 4), (7, 3), (8, 3)])

    return puzzle
