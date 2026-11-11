"""PuzzleMadness Between Lines Sudoku — 2025-11-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 3, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 6, 0, 0, 5, 3, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 4, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 4), (2, 5), (3, 5), (4, 6), (3, 7), (3, 8)])
    puzzle.add_between_line([(3, 1), (3, 0), (4, 1), (5, 1), (5, 2)])
    puzzle.add_between_line([(4, 7), (5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_between_line([(2, 1), (1, 2), (1, 3), (0, 4), (0, 3)])
    puzzle.add_between_line([(8, 5), (8, 6), (7, 7), (7, 6)])
    puzzle.add_between_line([(7, 1), (7, 2), (6, 3), (7, 4)])
    puzzle.add_between_line([(0, 1), (0, 2), (1, 1), (0, 0)])
    puzzle.add_between_line([(6, 1), (7, 0), (6, 0)])
    puzzle.add_between_line([(5, 3), (4, 4), (3, 3)])
    puzzle.add_between_line([(2, 4), (1, 4), (2, 3)])
    puzzle.add_between_line([(8, 2), (7, 3), (8, 3)])

    return puzzle
