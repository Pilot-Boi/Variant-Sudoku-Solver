"""PuzzleMadness Between Lines Sudoku — 2025-12-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 4, 0, 0, 5],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 4, 1, 0, 0, 0, 0, 3, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 3, 0, 0, 0, 9, 5, 1],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 2), (3, 1), (2, 1), (1, 0), (0, 1), (0, 2)])
    puzzle.add_between_line([(8, 7), (7, 8), (7, 7), (7, 6), (6, 5)])
    puzzle.add_between_line([(8, 0), (7, 0), (6, 0), (5, 1), (4, 1)])
    puzzle.add_between_line([(1, 5), (0, 4), (1, 3), (2, 4), (2, 3)])
    puzzle.add_between_line([(5, 4), (6, 4), (5, 3), (6, 3), (6, 2)])
    puzzle.add_between_line([(6, 1), (7, 2), (8, 2), (7, 3)])
    puzzle.add_between_line([(0, 6), (0, 7), (1, 6), (1, 7)])
    puzzle.add_between_line([(4, 6), (3, 6), (2, 7), (2, 6)])
    puzzle.add_between_line([(2, 2), (3, 2), (4, 3)])
    puzzle.add_between_line([(3, 5), (3, 4), (4, 4)])
    puzzle.add_between_line([(5, 8), (4, 7), (3, 8)])
    puzzle.add_between_line([(7, 5), (8, 5), (8, 6)])

    return puzzle
