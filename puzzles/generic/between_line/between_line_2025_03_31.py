"""PuzzleMadness Between Lines Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 8, 0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 3, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 6, 0, 0, 5],
        [0, 0, 6, 0, 0, 0, 0, 0, 3],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 4],
        [0, 0, 0, 0, 0, 3, 8, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 1), (1, 2), (1, 3), (2, 3), (1, 4), (0, 4)])
    puzzle.add_between_line([(6, 4), (6, 3), (5, 2), (6, 1), (7, 0)])
    puzzle.add_between_line([(4, 1), (5, 0), (4, 0), (3, 1), (3, 2)])
    puzzle.add_between_line([(3, 7), (4, 6), (3, 5), (4, 4), (5, 5)])
    puzzle.add_between_line([(6, 8), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_between_line([(8, 8), (7, 7), (7, 8), (6, 7)])
    puzzle.add_between_line([(8, 5), (7, 5), (7, 4), (8, 3)])
    puzzle.add_between_line([(3, 3), (3, 4), (2, 5), (2, 4)])
    puzzle.add_between_line([(2, 2), (2, 1), (1, 1)])
    puzzle.add_between_line([(0, 6), (1, 7), (0, 7)])
    puzzle.add_between_line([(3, 6), (2, 7), (2, 8)])
    puzzle.add_between_line([(2, 6), (1, 6), (1, 5)])

    return puzzle
