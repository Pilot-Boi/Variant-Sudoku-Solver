"""PuzzleMadness Between Lines Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 1, 0, 8, 0, 0, 0, 4],
        [0, 8, 0, 0, 0, 0, 6, 7, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 7), (7, 7), (8, 6), (7, 5), (6, 4), (5, 4)])
    puzzle.add_between_line([(8, 5), (7, 4), (6, 3), (6, 2), (7, 3)])
    puzzle.add_between_line([(2, 4), (1, 3), (2, 3), (3, 2), (2, 2)])
    puzzle.add_between_line([(4, 0), (3, 0), (3, 1), (4, 1), (5, 0)])
    puzzle.add_between_line([(3, 7), (2, 7), (2, 6), (3, 5), (4, 4)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 7), (5, 8)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4), (1, 5)])
    puzzle.add_between_line([(7, 0), (8, 1), (7, 1), (6, 1)])
    puzzle.add_between_line([(6, 6), (5, 5), (4, 5)])
    puzzle.add_between_line([(4, 7), (5, 6), (5, 7)])
    puzzle.add_between_line([(0, 6), (1, 6), (2, 5)])

    return puzzle
