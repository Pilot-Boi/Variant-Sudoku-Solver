"""PuzzleMadness Between Lines Sudoku — 2025-11-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-11-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/11/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 1, 0, 0, 3],
        [0, 1, 0, 0, 7, 0, 0, 0, 0],
        [3, 0, 0, 5, 0, 0, 0, 4, 0],
        [9, 0, 0, 4, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [8, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(7, 3), (7, 2), (8, 2), (7, 1), (6, 1), (6, 0)])
    puzzle.add_between_line([(6, 8), (7, 8), (6, 7), (7, 7), (8, 8)])
    puzzle.add_between_line([(7, 5), (8, 5), (7, 4), (6, 5), (5, 5)])
    puzzle.add_between_line([(4, 8), (3, 8), (4, 7), (5, 7), (4, 6)])
    puzzle.add_between_line([(4, 3), (5, 2), (5, 1), (5, 0)])
    puzzle.add_between_line([(3, 3), (2, 2), (1, 2), (0, 2)])
    puzzle.add_between_line([(4, 0), (4, 1), (3, 1), (2, 1)])
    puzzle.add_between_line([(5, 3), (6, 3), (5, 4)])
    puzzle.add_between_line([(1, 0), (2, 0), (3, 0)])
    puzzle.add_between_line([(6, 6), (5, 6), (4, 5)])

    return puzzle
