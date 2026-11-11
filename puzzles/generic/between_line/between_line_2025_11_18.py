"""PuzzleMadness Between Lines Sudoku — 2025-11-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 8, 0],
        [0, 0, 0, 1, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 7, 2, 0, 0, 0, 3, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [4, 8, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 4), (6, 5), (5, 6), (5, 7), (4, 7), (4, 8)])
    puzzle.add_between_line([(5, 2), (6, 2), (7, 1), (8, 2), (7, 2)])
    puzzle.add_between_line([(1, 4), (0, 5), (1, 6), (0, 7), (0, 6)])
    puzzle.add_between_line([(1, 2), (0, 1), (1, 1), (2, 0), (3, 1)])
    puzzle.add_between_line([(6, 1), (7, 0), (6, 0), (5, 0)])
    puzzle.add_between_line([(5, 4), (5, 5), (4, 6), (4, 5)])
    puzzle.add_between_line([(3, 3), (3, 2), (2, 2), (2, 1)])
    puzzle.add_between_line([(5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_between_line([(5, 1), (4, 1), (4, 0)])
    puzzle.add_between_line([(7, 4), (7, 5), (6, 6)])
    puzzle.add_between_line([(2, 3), (2, 4), (1, 3)])

    return puzzle
