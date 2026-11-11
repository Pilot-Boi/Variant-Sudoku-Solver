"""PuzzleMadness Between Lines Sudoku — 2025-12-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 1, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 8],
        [0, 0, 4, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 9, 1, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 3, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 8), (7, 7), (8, 7), (8, 6), (7, 5), (7, 6)])
    puzzle.add_between_line([(1, 7), (1, 6), (2, 6), (3, 5), (4, 4)])
    puzzle.add_between_line([(7, 4), (6, 5), (6, 4), (6, 3), (5, 3)])
    puzzle.add_between_line([(2, 3), (3, 4), (3, 3), (4, 3), (5, 4)])
    puzzle.add_between_line([(0, 4), (1, 3), (0, 2), (1, 1), (0, 1)])
    puzzle.add_between_line([(5, 5), (4, 6), (5, 7), (6, 7)])
    puzzle.add_between_line([(5, 1), (5, 2), (4, 1), (4, 0)])
    puzzle.add_between_line([(0, 5), (1, 4), (2, 4), (1, 5)])
    puzzle.add_between_line([(3, 7), (3, 8), (4, 8)])
    puzzle.add_between_line([(7, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(0, 0), (1, 0), (2, 0)])
    puzzle.add_between_line([(6, 2), (7, 2), (6, 1)])

    return puzzle
