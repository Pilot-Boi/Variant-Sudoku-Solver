"""PuzzleMadness Between Lines Sudoku — 2025-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 8, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 2, 0, 9, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 4, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 9, 7],
        [0, 0, 0, 0, 0, 0, 0, 4, 3],
        [0, 0, 9, 0, 0, 0, 3, 0, 0],
        [5, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 0), (2, 1), (2, 2), (1, 2), (1, 3), (2, 3)])
    puzzle.add_between_line([(3, 3), (4, 3), (5, 2), (4, 1), (5, 0)])
    puzzle.add_between_line([(4, 5), (3, 5), (2, 5), (1, 4), (2, 4)])
    puzzle.add_between_line([(5, 6), (6, 7), (6, 6), (7, 7), (8, 8)])
    puzzle.add_between_line([(2, 7), (3, 8), (4, 8), (5, 7)])
    puzzle.add_between_line([(1, 6), (1, 7), (1, 8), (0, 8)])
    puzzle.add_between_line([(5, 5), (6, 5), (7, 6), (7, 5)])
    puzzle.add_between_line([(5, 1), (6, 1), (7, 0), (8, 1)])
    puzzle.add_between_line([(4, 4), (5, 3), (6, 3)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 4)])
    puzzle.add_between_line([(1, 5), (0, 6), (0, 7)])
    puzzle.add_between_line([(0, 2), (0, 1), (1, 1)])

    return puzzle
