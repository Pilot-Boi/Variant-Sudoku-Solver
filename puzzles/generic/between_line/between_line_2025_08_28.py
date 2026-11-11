"""PuzzleMadness Between Lines Sudoku — 2025-08-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 6, 0, 0, 8, 2, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 1, 0, 4],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 2, 8, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 3), (4, 4), (4, 5), (5, 5), (6, 5), (7, 6)])
    puzzle.add_between_line([(1, 7), (0, 6), (1, 6), (2, 6), (3, 6)])
    puzzle.add_between_line([(3, 1), (2, 0), (3, 0), (4, 1), (5, 1)])
    puzzle.add_between_line([(0, 0), (0, 1), (0, 2), (1, 3), (2, 2)])
    puzzle.add_between_line([(6, 8), (7, 8), (8, 7), (8, 8)])
    puzzle.add_between_line([(3, 7), (2, 7), (3, 8), (4, 7)])
    puzzle.add_between_line([(7, 2), (6, 3), (5, 2), (5, 3)])
    puzzle.add_between_line([(6, 6), (5, 6), (4, 6), (5, 7)])
    puzzle.add_between_line([(7, 1), (8, 1), (7, 0)])
    puzzle.add_between_line([(4, 2), (3, 2), (2, 1)])
    puzzle.add_between_line([(8, 2), (7, 3), (8, 3)])

    return puzzle
