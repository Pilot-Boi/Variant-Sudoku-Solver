"""PuzzleMadness Between Lines Sudoku — 2025-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 1, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 7],
        [4, 0, 0, 3, 1, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 3, 0, 5, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 1), (4, 0), (5, 0), (5, 1), (4, 2), (3, 1)])
    puzzle.add_between_line([(7, 7), (7, 8), (6, 8), (5, 8), (4, 8)])
    puzzle.add_between_line([(6, 4), (7, 5), (6, 6), (5, 5), (4, 6)])
    puzzle.add_between_line([(1, 1), (1, 2), (0, 1), (1, 0), (2, 0)])
    puzzle.add_between_line([(4, 7), (3, 7), (2, 7), (1, 7)])
    puzzle.add_between_line([(8, 7), (8, 6), (8, 5), (7, 6)])
    puzzle.add_between_line([(2, 5), (3, 4), (3, 3), (2, 2)])
    puzzle.add_between_line([(3, 8), (2, 8), (1, 8)])
    puzzle.add_between_line([(5, 3), (5, 4), (4, 4)])
    puzzle.add_between_line([(7, 3), (7, 4), (8, 4)])
    puzzle.add_between_line([(6, 7), (5, 6), (5, 7)])

    return puzzle
