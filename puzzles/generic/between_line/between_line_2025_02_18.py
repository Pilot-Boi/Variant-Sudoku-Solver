"""PuzzleMadness Between Lines Sudoku — 2025-02-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 5, 0, 9, 0, 0, 2, 8, 0],
        [0, 0, 0, 5, 7, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 3, 0, 0],
        [0, 8, 2, 0, 0, 0, 7, 1, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 0), (3, 1), (3, 0), (2, 1), (2, 2), (1, 1)])
    puzzle.add_between_line([(6, 3), (6, 2), (7, 1), (6, 0), (6, 1)])
    puzzle.add_between_line([(8, 8), (8, 7), (8, 6), (7, 6), (7, 7)])
    puzzle.add_between_line([(7, 3), (7, 2), (8, 1), (8, 0), (7, 0)])
    puzzle.add_between_line([(4, 2), (5, 2), (5, 3), (4, 4)])
    puzzle.add_between_line([(1, 7), (0, 6), (1, 5), (2, 5)])
    puzzle.add_between_line([(4, 8), (5, 8), (4, 7), (4, 6)])
    puzzle.add_between_line([(2, 6), (2, 7), (2, 8)])
    puzzle.add_between_line([(3, 5), (2, 4), (3, 4)])
    puzzle.add_between_line([(1, 0), (0, 0), (0, 1)])
    puzzle.add_between_line([(7, 4), (6, 5), (5, 5)])

    return puzzle
