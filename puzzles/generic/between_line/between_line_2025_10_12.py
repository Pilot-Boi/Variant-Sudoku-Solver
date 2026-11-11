"""PuzzleMadness Between Lines Sudoku — 2025-10-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 3, 0, 5],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 4, 8, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 6), (6, 5), (5, 4), (5, 3), (4, 2), (3, 3)])
    puzzle.add_between_line([(0, 1), (1, 1), (1, 2), (1, 3), (0, 3)])
    puzzle.add_between_line([(7, 8), (8, 8), (8, 7), (7, 6), (8, 5)])
    puzzle.add_between_line([(3, 6), (2, 7), (1, 6), (1, 5), (1, 4)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0), (3, 1), (2, 1)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 7), (4, 6)])
    puzzle.add_between_line([(8, 4), (8, 3), (8, 2), (8, 1)])
    puzzle.add_between_line([(6, 8), (5, 8), (5, 7), (4, 8)])
    puzzle.add_between_line([(4, 1), (4, 0), (5, 0)])
    puzzle.add_between_line([(4, 4), (4, 5), (5, 5)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 7)])

    return puzzle
