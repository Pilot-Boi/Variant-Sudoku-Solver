"""PuzzleMadness Between Lines Sudoku — 2025-07-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 5, 0],
        [0, 6, 0, 0, 0, 8, 0, 0, 0],
        [0, 4, 5, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 3, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 7],
        [0, 0, 0, 7, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (2, 2), (2, 3), (1, 2)])
    puzzle.add_between_line([(7, 0), (7, 1), (6, 2), (5, 1), (6, 1)])
    puzzle.add_between_line([(3, 5), (4, 4), (3, 3), (4, 3), (4, 2)])
    puzzle.add_between_line([(8, 6), (7, 5), (6, 6), (5, 6), (5, 7)])
    puzzle.add_between_line([(5, 4), (6, 4), (6, 5), (7, 4), (8, 4)])
    puzzle.add_between_line([(4, 7), (4, 6), (3, 7), (2, 7)])
    puzzle.add_between_line([(1, 8), (1, 7), (0, 8), (0, 7)])
    puzzle.add_between_line([(3, 2), (3, 1), (4, 0), (4, 1)])
    puzzle.add_between_line([(2, 6), (3, 6), (2, 5)])
    puzzle.add_between_line([(3, 4), (2, 4), (1, 4)])
    puzzle.add_between_line([(8, 2), (8, 3), (7, 2)])
    puzzle.add_between_line([(1, 6), (1, 5), (0, 5)])

    return puzzle
