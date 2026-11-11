"""PuzzleMadness Between Lines Sudoku — 2025-07-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 2, 8, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 9, 0, 0, 8, 6, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 2],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 1), (3, 0), (3, 1), (2, 1), (1, 1), (0, 1)])
    puzzle.add_between_line([(8, 1), (7, 2), (6, 1), (6, 0), (5, 1)])
    puzzle.add_between_line([(0, 6), (0, 7), (1, 7), (2, 7), (2, 6)])
    puzzle.add_between_line([(0, 2), (1, 3), (2, 3), (2, 2), (1, 2)])
    puzzle.add_between_line([(4, 4), (4, 3), (3, 2), (4, 2)])
    puzzle.add_between_line([(7, 5), (7, 4), (7, 3), (6, 3)])
    puzzle.add_between_line([(1, 4), (0, 5), (1, 6), (2, 5)])
    puzzle.add_between_line([(6, 4), (6, 5), (6, 6), (5, 5)])
    puzzle.add_between_line([(2, 8), (3, 8), (4, 8)])
    puzzle.add_between_line([(2, 4), (3, 5), (3, 6)])
    puzzle.add_between_line([(5, 7), (5, 6), (4, 6)])
    puzzle.add_between_line([(8, 6), (8, 7), (7, 6)])

    return puzzle
