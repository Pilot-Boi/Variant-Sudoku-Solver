"""PuzzleMadness Between Lines Sudoku — 2025-05-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 8, 4, 0, 6, 0, 7, 0],
        [0, 0, 6, 0, 0, 1, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 3, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 1],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 1), (3, 1), (4, 2), (5, 2), (6, 1), (6, 2)])
    puzzle.add_between_line([(4, 5), (5, 4), (5, 5), (4, 6), (3, 5)])
    puzzle.add_between_line([(4, 4), (4, 3), (5, 3), (6, 3), (7, 3)])
    puzzle.add_between_line([(7, 8), (8, 8), (8, 7), (8, 6), (7, 7)])
    puzzle.add_between_line([(8, 5), (7, 5), (6, 4), (6, 5), (6, 6)])
    puzzle.add_between_line([(1, 8), (1, 7), (2, 7), (3, 8)])
    puzzle.add_between_line([(0, 3), (1, 4), (0, 4), (0, 5)])
    puzzle.add_between_line([(5, 1), (4, 1), (4, 0), (3, 0)])
    puzzle.add_between_line([(5, 7), (4, 7), (5, 6)])
    puzzle.add_between_line([(7, 0), (7, 1), (8, 0)])
    puzzle.add_between_line([(7, 2), (8, 2), (8, 1)])
    puzzle.add_between_line([(2, 0), (1, 0), (0, 1)])

    return puzzle
