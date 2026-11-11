"""PuzzleMadness Between Lines Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 9, 0, 0, 0, 0],
        [0, 3, 9, 0, 5, 0, 8, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 9],
        [0, 8, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 6), (8, 7), (7, 7), (7, 6), (6, 6), (5, 7)])
    puzzle.add_between_line([(3, 7), (2, 8), (1, 7), (0, 8), (0, 7)])
    puzzle.add_between_line([(1, 0), (1, 1), (0, 2), (0, 3), (1, 3)])
    puzzle.add_between_line([(7, 0), (8, 0), (7, 1), (6, 0), (5, 0)])
    puzzle.add_between_line([(2, 5), (1, 4), (1, 5), (0, 6), (0, 5)])
    puzzle.add_between_line([(6, 2), (5, 2), (5, 1), (6, 1)])
    puzzle.add_between_line([(4, 1), (4, 2), (5, 3), (4, 3)])
    puzzle.add_between_line([(8, 2), (7, 3), (8, 4), (7, 5)])
    puzzle.add_between_line([(3, 8), (4, 7), (4, 8)])
    puzzle.add_between_line([(4, 5), (4, 4), (3, 5)])
    puzzle.add_between_line([(2, 7), (1, 6), (2, 6)])
    puzzle.add_between_line([(7, 4), (6, 4), (6, 3)])

    return puzzle
