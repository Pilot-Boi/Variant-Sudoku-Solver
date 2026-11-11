"""PuzzleMadness Between Lines Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 4, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 7, 0, 6],
        [0, 0, 0, 0, 0, 0, 4, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 5],
        [0, 8, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(3, 5), (4, 4), (3, 3), (3, 2), (2, 3), (3, 4)])
    puzzle.add_between_line([(0, 5), (0, 4), (0, 3), (1, 2), (1, 3)])
    puzzle.add_between_line([(1, 7), (0, 6), (1, 6), (2, 6), (1, 5)])
    puzzle.add_between_line([(1, 1), (2, 1), (3, 1), (4, 0), (5, 1)])
    puzzle.add_between_line([(6, 1), (6, 2), (7, 3), (8, 3)])
    puzzle.add_between_line([(4, 6), (4, 7), (5, 6), (6, 7)])
    puzzle.add_between_line([(8, 2), (7, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(4, 5), (5, 5), (6, 5)])
    puzzle.add_between_line([(2, 8), (3, 8), (2, 7)])
    puzzle.add_between_line([(1, 0), (0, 0), (0, 1)])

    return puzzle
