"""PuzzleMadness Between Lines Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [4, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 2, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 4, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 7), (6, 6), (7, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_between_line([(4, 5), (4, 4), (3, 5), (2, 6), (1, 6)])
    puzzle.add_between_line([(8, 4), (8, 5), (7, 6), (8, 7), (8, 6)])
    puzzle.add_between_line([(8, 1), (7, 1), (7, 2), (8, 3), (7, 3)])
    puzzle.add_between_line([(6, 1), (7, 0), (6, 0), (5, 0), (5, 1)])
    puzzle.add_between_line([(0, 4), (1, 4), (2, 4), (1, 5)])
    puzzle.add_between_line([(2, 7), (2, 8), (1, 7), (0, 8)])
    puzzle.add_between_line([(3, 4), (3, 3), (3, 2), (2, 1)])
    puzzle.add_between_line([(5, 2), (6, 2), (6, 3), (5, 4)])
    puzzle.add_between_line([(2, 2), (1, 3), (1, 2)])
    puzzle.add_between_line([(4, 7), (4, 6), (3, 7)])
    puzzle.add_between_line([(4, 0), (4, 1), (3, 1)])
    puzzle.add_between_line([(5, 3), (4, 2), (4, 3)])

    return puzzle
