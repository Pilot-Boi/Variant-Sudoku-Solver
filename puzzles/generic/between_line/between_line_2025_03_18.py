"""PuzzleMadness Between Lines Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
        [0, 0, 0, 0, 0, 7, 0, 4, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 8, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 3), (4, 4), (3, 3), (2, 3), (1, 3), (1, 2)])
    puzzle.add_between_line([(5, 0), (6, 1), (5, 2), (6, 3), (6, 2)])
    puzzle.add_between_line([(1, 7), (2, 8), (3, 7), (2, 6), (3, 5)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 0), (1, 1), (2, 2)])
    puzzle.add_between_line([(8, 8), (7, 8), (6, 7), (6, 8)])
    puzzle.add_between_line([(2, 5), (2, 4), (1, 5), (1, 4)])
    puzzle.add_between_line([(8, 4), (7, 3), (8, 2), (8, 3)])
    puzzle.add_between_line([(5, 4), (5, 5), (4, 5)])
    puzzle.add_between_line([(5, 3), (4, 2), (3, 2)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 8)])

    return puzzle
