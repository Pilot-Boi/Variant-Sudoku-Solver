"""PuzzleMadness Between Lines Sudoku — 2025-07-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 6, 0, 7],
        [2, 0, 6, 0, 0, 0, 0, 8, 0],
        [0, 0, 4, 2, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 6, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 0), (3, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(3, 6), (3, 5), (4, 6), (4, 5), (5, 6)])
    puzzle.add_between_line([(1, 2), (1, 3), (0, 3), (1, 4), (1, 5)])
    puzzle.add_between_line([(5, 4), (6, 5), (7, 5), (8, 4), (7, 4)])
    puzzle.add_between_line([(4, 0), (5, 0), (5, 1), (5, 2), (4, 2)])
    puzzle.add_between_line([(8, 2), (8, 1), (8, 0), (7, 0)])
    puzzle.add_between_line([(0, 8), (1, 8), (1, 7), (0, 7)])
    puzzle.add_between_line([(2, 7), (2, 8), (3, 8), (3, 7)])
    puzzle.add_between_line([(2, 5), (1, 6), (0, 6), (0, 5)])
    puzzle.add_between_line([(5, 8), (6, 8), (7, 8)])
    puzzle.add_between_line([(7, 2), (7, 3), (6, 2)])
    puzzle.add_between_line([(3, 4), (2, 4), (2, 3)])
    puzzle.add_between_line([(6, 6), (6, 7), (7, 6)])

    return puzzle
