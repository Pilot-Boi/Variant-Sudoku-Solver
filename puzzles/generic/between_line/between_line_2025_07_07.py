"""PuzzleMadness Between Lines Sudoku — 2025-07-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 4, 9, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 8, 6, 0],
        [0, 6, 0, 0, 2, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 1), (1, 2), (0, 1), (1, 0), (2, 1), (3, 1)])
    puzzle.add_between_line([(7, 8), (8, 7), (8, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(6, 5), (7, 4), (6, 3), (7, 2), (6, 2)])
    puzzle.add_between_line([(7, 6), (6, 7), (6, 6), (5, 7), (6, 8)])
    puzzle.add_between_line([(2, 5), (2, 4), (3, 5), (4, 5), (3, 4)])
    puzzle.add_between_line([(1, 5), (2, 6), (3, 6), (4, 6)])
    puzzle.add_between_line([(0, 4), (0, 3), (1, 3), (2, 3)])
    puzzle.add_between_line([(7, 1), (7, 0), (8, 0), (8, 1)])
    puzzle.add_between_line([(1, 8), (0, 7), (0, 6), (0, 5)])
    puzzle.add_between_line([(8, 2), (7, 3), (8, 4)])
    puzzle.add_between_line([(6, 0), (5, 1), (5, 0)])
    puzzle.add_between_line([(4, 7), (5, 6), (5, 5)])
    puzzle.add_between_line([(5, 2), (5, 3), (4, 4)])

    return puzzle
