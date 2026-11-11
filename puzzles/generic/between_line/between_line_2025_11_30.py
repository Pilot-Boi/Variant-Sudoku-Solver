"""PuzzleMadness Between Lines Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 8, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 6, 7],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 8, 0, 7, 0, 0, 0, 0, 0],
        [0, 4, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 0), (1, 0), (0, 1), (1, 2), (2, 3), (2, 4)])
    puzzle.add_between_line([(7, 7), (8, 7), (8, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(3, 3), (3, 2), (4, 1), (5, 1), (4, 2)])
    puzzle.add_between_line([(7, 4), (6, 5), (5, 4), (4, 4), (5, 3)])
    puzzle.add_between_line([(6, 3), (7, 3), (8, 2), (8, 1)])
    puzzle.add_between_line([(7, 1), (6, 1), (5, 2), (4, 3)])
    puzzle.add_between_line([(2, 2), (2, 1), (3, 0), (2, 0)])
    puzzle.add_between_line([(1, 8), (2, 7), (3, 7), (3, 6)])
    puzzle.add_between_line([(0, 5), (1, 4), (0, 3)])
    puzzle.add_between_line([(2, 6), (1, 6), (1, 5)])
    puzzle.add_between_line([(5, 7), (4, 8), (4, 7)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0)])

    return puzzle
