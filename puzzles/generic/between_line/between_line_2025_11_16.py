"""PuzzleMadness Between Lines Sudoku — 2025-11-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 2, 0, 0, 8, 0, 0],
        [0, 0, 4, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 8, 0, 7, 0, 0, 0, 0, 0],
        [7, 0, 9, 0, 0, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 7), (5, 7), (6, 7), (7, 6), (7, 7), (6, 8)])
    puzzle.add_between_line([(0, 4), (0, 5), (1, 5), (2, 4), (1, 4)])
    puzzle.add_between_line([(8, 7), (8, 6), (7, 5), (8, 5), (7, 4)])
    puzzle.add_between_line([(8, 2), (7, 2), (8, 3), (7, 3), (6, 4)])
    puzzle.add_between_line([(2, 3), (3, 4), (2, 5), (1, 6), (0, 7)])
    puzzle.add_between_line([(2, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_between_line([(7, 1), (6, 1), (7, 0), (6, 0)])
    puzzle.add_between_line([(5, 2), (6, 3), (5, 4), (5, 3)])
    puzzle.add_between_line([(0, 2), (1, 2), (1, 1), (2, 2)])
    puzzle.add_between_line([(3, 1), (4, 2), (3, 3)])
    puzzle.add_between_line([(0, 8), (1, 8), (1, 7)])
    puzzle.add_between_line([(6, 5), (5, 5), (4, 5)])
    puzzle.add_between_line([(0, 0), (1, 0), (0, 1)])

    return puzzle
