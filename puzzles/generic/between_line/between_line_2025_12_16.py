"""PuzzleMadness Between Lines Sudoku — 2025-12-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 3, 0, 9, 2, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [2, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 9, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 1, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 1), (3, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 6), (1, 5), (0, 4)])
    puzzle.add_between_line([(8, 5), (7, 6), (6, 6), (5, 6), (4, 6)])
    puzzle.add_between_line([(7, 7), (7, 8), (6, 7), (5, 7), (4, 7)])
    puzzle.add_between_line([(7, 0), (6, 0), (7, 1), (8, 1)])
    puzzle.add_between_line([(3, 4), (2, 5), (1, 4), (0, 3)])
    puzzle.add_between_line([(8, 4), (8, 3), (7, 3), (7, 4)])
    puzzle.add_between_line([(5, 4), (4, 3), (4, 2), (3, 2)])
    puzzle.add_between_line([(0, 1), (1, 0), (1, 1)])
    puzzle.add_between_line([(2, 4), (1, 3), (2, 3)])
    puzzle.add_between_line([(3, 5), (3, 6), (4, 5)])

    return puzzle
