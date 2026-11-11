"""PuzzleMadness Between Lines Sudoku — 2025-03-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 8, 0, 0, 0, 0, 0, 4],
        [1, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 3, 0, 6, 0, 0, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 7, 0],
        [0, 8, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 5), (1, 4), (0, 3), (0, 4), (0, 5), (1, 5)])
    puzzle.add_between_line([(6, 6), (7, 6), (8, 7), (7, 8), (7, 7)])
    puzzle.add_between_line([(5, 8), (5, 7), (4, 7), (3, 6), (4, 6)])
    puzzle.add_between_line([(2, 6), (1, 7), (2, 7), (1, 8), (0, 7)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 2), (8, 3), (7, 3)])
    puzzle.add_between_line([(2, 3), (2, 4), (3, 5), (4, 5)])
    puzzle.add_between_line([(2, 0), (2, 1), (1, 0), (0, 0)])
    puzzle.add_between_line([(4, 3), (3, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(1, 1), (2, 2), (3, 1), (3, 2)])
    puzzle.add_between_line([(6, 3), (7, 4), (7, 5)])
    puzzle.add_between_line([(5, 6), (6, 5), (5, 4)])
    puzzle.add_between_line([(4, 0), (4, 1), (5, 1)])
    puzzle.add_between_line([(2, 8), (3, 7), (3, 8)])

    return puzzle
