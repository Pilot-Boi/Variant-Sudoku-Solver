"""PuzzleMadness Between Lines Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 1, 3, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 2, 5, 0, 0],
        [0, 0, 0, 4, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 1, 7, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 5), (1, 4), (0, 4), (1, 3), (0, 2), (1, 2)])
    puzzle.add_between_line([(4, 2), (5, 1), (5, 0), (4, 0), (3, 1)])
    puzzle.add_between_line([(7, 2), (6, 1), (6, 0), (7, 0), (8, 1)])
    puzzle.add_between_line([(2, 4), (3, 3), (4, 4), (5, 3), (5, 4)])
    puzzle.add_between_line([(6, 7), (6, 8), (5, 7), (4, 8), (5, 8)])
    puzzle.add_between_line([(8, 5), (7, 4), (6, 5), (7, 5)])
    puzzle.add_between_line([(1, 7), (2, 8), (3, 8), (4, 7)])
    puzzle.add_between_line([(6, 4), (6, 3), (6, 2), (7, 3)])
    puzzle.add_between_line([(1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(2, 2), (2, 3), (3, 2)])
    puzzle.add_between_line([(7, 8), (7, 7), (7, 6)])
    puzzle.add_between_line([(0, 5), (0, 6), (0, 7)])
    puzzle.add_between_line([(5, 6), (4, 6), (3, 6)])

    return puzzle
