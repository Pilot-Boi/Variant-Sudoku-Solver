"""PuzzleMadness Between Lines Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 5, 9, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 4, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 5, 0, 2, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 8), (4, 7), (4, 6), (3, 7), (2, 8), (3, 8)])
    puzzle.add_between_line([(3, 0), (3, 1), (2, 2), (1, 3), (0, 3)])
    puzzle.add_between_line([(6, 2), (7, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_between_line([(1, 5), (2, 4), (3, 4), (4, 4), (4, 3)])
    puzzle.add_between_line([(1, 4), (0, 5), (0, 6), (0, 7), (1, 8)])
    puzzle.add_between_line([(8, 7), (8, 8), (7, 7), (7, 6)])
    puzzle.add_between_line([(1, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_between_line([(7, 8), (6, 8), (6, 7), (5, 7)])
    puzzle.add_between_line([(5, 3), (6, 4), (5, 4), (4, 5)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0)])
    puzzle.add_between_line([(3, 3), (4, 2), (3, 2)])
    puzzle.add_between_line([(5, 5), (6, 6), (6, 5)])
    puzzle.add_between_line([(4, 1), (5, 2), (5, 1)])

    return puzzle
