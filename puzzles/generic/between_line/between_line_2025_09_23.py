"""PuzzleMadness Between Lines Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 8, 0, 0, 0],
        [0, 3, 0, 0, 0, 5, 0, 0, 0],
        [0, 9, 0, 7, 0, 6, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 4, 8, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (3, 7), (2, 7), (1, 8), (0, 7), (1, 6)])
    puzzle.add_between_line([(6, 1), (7, 1), (8, 1), (7, 2), (8, 3)])
    puzzle.add_between_line([(4, 4), (5, 5), (4, 5), (5, 6), (6, 6)])
    puzzle.add_between_line([(1, 4), (0, 4), (0, 3), (1, 3), (1, 2)])
    puzzle.add_between_line([(3, 1), (3, 0), (4, 1), (4, 0)])
    puzzle.add_between_line([(0, 5), (1, 5), (2, 4), (2, 5)])
    puzzle.add_between_line([(4, 8), (5, 8), (6, 8), (5, 7)])
    puzzle.add_between_line([(6, 3), (5, 3), (4, 2)])
    puzzle.add_between_line([(7, 4), (6, 5), (7, 6)])
    puzzle.add_between_line([(3, 3), (3, 2), (2, 2)])
    puzzle.add_between_line([(8, 7), (7, 8), (7, 7)])

    return puzzle
