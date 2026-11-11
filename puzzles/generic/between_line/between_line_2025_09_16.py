"""PuzzleMadness Between Lines Sudoku — 2025-09-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 5, 0, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 6, 4, 0, 0, 9, 2, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4)])
    puzzle.add_between_line([(0, 5), (1, 6), (1, 5), (2, 4), (3, 5)])
    puzzle.add_between_line([(3, 0), (4, 0), (5, 1), (4, 1), (5, 2)])
    puzzle.add_between_line([(6, 6), (6, 7), (5, 8), (4, 8), (5, 7)])
    puzzle.add_between_line([(8, 8), (7, 8), (7, 7), (7, 6)])
    puzzle.add_between_line([(3, 8), (2, 7), (3, 6), (2, 5)])
    puzzle.add_between_line([(1, 3), (1, 2), (2, 3), (3, 3)])
    puzzle.add_between_line([(4, 7), (4, 6), (5, 6)])
    puzzle.add_between_line([(8, 6), (8, 5), (8, 4)])
    puzzle.add_between_line([(3, 1), (3, 2), (4, 2)])

    return puzzle
