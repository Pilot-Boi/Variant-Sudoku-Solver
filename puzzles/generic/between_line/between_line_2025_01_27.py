"""PuzzleMadness Between Lines Sudoku — 2025-01-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-01-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/1/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 9, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 4],
        [0, 0, 6, 0, 0, 7, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 3, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 3), (1, 2), (2, 3), (3, 4), (4, 4), (3, 5)])
    puzzle.add_between_line([(1, 6), (1, 5), (0, 5), (0, 6), (1, 7)])
    puzzle.add_between_line([(5, 1), (5, 0), (6, 0), (7, 1), (8, 0)])
    puzzle.add_between_line([(4, 8), (3, 8), (3, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(7, 7), (8, 6), (8, 5), (7, 5)])
    puzzle.add_between_line([(7, 8), (6, 7), (5, 6), (5, 7)])
    puzzle.add_between_line([(6, 6), (6, 5), (5, 5), (5, 4)])
    puzzle.add_between_line([(3, 2), (4, 1), (3, 1), (3, 0)])
    puzzle.add_between_line([(0, 3), (0, 4), (1, 4)])
    puzzle.add_between_line([(3, 3), (2, 2), (1, 1)])
    puzzle.add_between_line([(3, 6), (2, 6), (2, 5)])
    puzzle.add_between_line([(6, 3), (7, 4), (6, 4)])

    return puzzle
