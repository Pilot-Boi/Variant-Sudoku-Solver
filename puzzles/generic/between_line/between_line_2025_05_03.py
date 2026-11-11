"""PuzzleMadness Between Lines Sudoku — 2025-05-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 2, 0, 3, 0, 4, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 6, 0, 1, 9, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 7, 0, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 1), (6, 2), (7, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_between_line([(8, 0), (8, 1), (7, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(4, 4), (5, 5), (5, 6), (4, 7), (4, 6)])
    puzzle.add_between_line([(8, 7), (7, 8), (7, 7), (8, 6), (7, 5)])
    puzzle.add_between_line([(2, 2), (1, 3), (2, 3), (2, 4)])
    puzzle.add_between_line([(3, 3), (4, 3), (5, 4), (6, 5)])
    puzzle.add_between_line([(3, 2), (2, 1), (2, 0), (3, 1)])
    puzzle.add_between_line([(6, 3), (7, 4), (7, 3)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4)])
    puzzle.add_between_line([(3, 6), (2, 7), (3, 7)])
    puzzle.add_between_line([(2, 8), (1, 8), (0, 7)])

    return puzzle
