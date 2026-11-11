"""PuzzleMadness Between Lines Sudoku — 2025-12-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 6],
        [1, 0, 8, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 3],
        [9, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 8, 9, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 0), (1, 0), (0, 1), (0, 2), (1, 2), (1, 3)])
    puzzle.add_between_line([(6, 6), (7, 7), (8, 6), (8, 5), (7, 4)])
    puzzle.add_between_line([(7, 3), (6, 3), (5, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(2, 2), (2, 3), (3, 2), (4, 2), (4, 3)])
    puzzle.add_between_line([(0, 3), (1, 4), (2, 5), (3, 5), (3, 6)])
    puzzle.add_between_line([(3, 8), (4, 7), (3, 7), (2, 8)])
    puzzle.add_between_line([(2, 6), (2, 7), (1, 7), (1, 6)])
    puzzle.add_between_line([(7, 2), (8, 1), (7, 1), (6, 2)])
    puzzle.add_between_line([(2, 1), (3, 1), (4, 1)])
    puzzle.add_between_line([(3, 4), (4, 5), (4, 6)])
    puzzle.add_between_line([(5, 4), (6, 4), (6, 5)])

    return puzzle
