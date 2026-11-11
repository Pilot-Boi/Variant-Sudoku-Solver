"""PuzzleMadness Between Lines Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 8],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 7, 0, 6],
        [0, 0, 0, 8, 5, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 3, 0, 8, 0],
        [0, 0, 0, 2, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 1), (4, 2), (5, 2), (5, 1), (6, 0), (7, 0)])
    puzzle.add_between_line([(3, 5), (4, 5), (3, 4), (2, 5), (2, 4)])
    puzzle.add_between_line([(5, 8), (6, 7), (6, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(8, 2), (7, 1), (7, 2), (6, 2), (5, 3)])
    puzzle.add_between_line([(0, 2), (0, 3), (1, 4), (2, 3), (1, 2)])
    puzzle.add_between_line([(0, 1), (1, 0), (2, 1), (3, 2)])
    puzzle.add_between_line([(8, 4), (8, 3), (7, 3), (7, 4)])
    puzzle.add_between_line([(8, 6), (7, 7), (7, 8), (8, 8)])
    puzzle.add_between_line([(5, 4), (5, 5), (4, 6), (5, 6)])
    puzzle.add_between_line([(4, 8), (5, 7), (4, 7)])
    puzzle.add_between_line([(1, 7), (1, 6), (1, 5)])
    puzzle.add_between_line([(3, 8), (2, 8), (2, 7)])
    puzzle.add_between_line([(6, 5), (6, 4), (6, 3)])

    return puzzle
