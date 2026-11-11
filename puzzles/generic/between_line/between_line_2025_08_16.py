"""PuzzleMadness Between Lines Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 3, 6],
        [6, 0, 0, 0, 0, 9, 1, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [7, 0, 0, 0, 4, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 4), (5, 5), (4, 5), (4, 4), (3, 4), (3, 5)])
    puzzle.add_between_line([(7, 3), (6, 4), (7, 4), (6, 5), (6, 6)])
    puzzle.add_between_line([(3, 0), (2, 1), (1, 2), (1, 3), (2, 2)])
    puzzle.add_between_line([(3, 7), (2, 7), (1, 7), (0, 6), (1, 5)])
    puzzle.add_between_line([(6, 1), (6, 0), (7, 1), (8, 2)])
    puzzle.add_between_line([(6, 7), (7, 7), (7, 8), (8, 8)])
    puzzle.add_between_line([(5, 2), (4, 3), (3, 2), (4, 2)])
    puzzle.add_between_line([(7, 5), (8, 6), (8, 7)])
    puzzle.add_between_line([(0, 5), (0, 4), (1, 4)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 1)])

    return puzzle
