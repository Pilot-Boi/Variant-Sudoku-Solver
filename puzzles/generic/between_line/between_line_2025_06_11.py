"""PuzzleMadness Between Lines Sudoku — 2025-06-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 3, 5],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 2, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 8, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [9, 5, 4, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 3), (4, 4), (5, 3), (6, 4), (6, 5), (7, 5)])
    puzzle.add_between_line([(7, 3), (7, 4), (6, 3), (5, 2), (6, 2)])
    puzzle.add_between_line([(8, 2), (8, 3), (7, 2), (6, 1), (5, 0)])
    puzzle.add_between_line([(2, 3), (3, 2), (2, 2), (3, 1), (4, 2)])
    puzzle.add_between_line([(7, 8), (8, 7), (7, 7), (7, 6), (6, 7)])
    puzzle.add_between_line([(3, 5), (3, 6), (2, 5), (1, 5)])
    puzzle.add_between_line([(0, 3), (1, 4), (0, 4), (0, 5)])
    puzzle.add_between_line([(2, 6), (2, 7), (2, 8), (3, 8)])
    puzzle.add_between_line([(1, 3), (1, 2), (1, 1), (2, 0)])
    puzzle.add_between_line([(0, 8), (0, 7), (1, 8)])
    puzzle.add_between_line([(5, 7), (6, 6), (5, 6)])
    puzzle.add_between_line([(4, 5), (4, 6), (4, 7)])
    puzzle.add_between_line([(0, 6), (1, 7), (1, 6)])

    return puzzle
