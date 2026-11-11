"""PuzzleMadness Between Lines Sudoku — 2025-09-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 3, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 1, 6, 0],
        [0, 0, 2, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 9],
        [0, 1, 8, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 1), (2, 0), (3, 1), (3, 2), (4, 1), (5, 2)])
    puzzle.add_between_line([(1, 8), (2, 8), (3, 7), (2, 6), (2, 7)])
    puzzle.add_between_line([(1, 3), (1, 2), (2, 2), (2, 3), (2, 4)])
    puzzle.add_between_line([(7, 4), (8, 4), (7, 5), (6, 6), (7, 7)])
    puzzle.add_between_line([(5, 5), (5, 4), (4, 5), (3, 4), (4, 3)])
    puzzle.add_between_line([(5, 3), (6, 4), (6, 3), (7, 3)])
    puzzle.add_between_line([(5, 7), (4, 7), (5, 8), (4, 8)])
    puzzle.add_between_line([(1, 6), (0, 6), (1, 5), (2, 5)])
    puzzle.add_between_line([(3, 6), (4, 6), (5, 6)])
    puzzle.add_between_line([(6, 1), (7, 1), (8, 2)])
    puzzle.add_between_line([(8, 7), (8, 8), (7, 8)])

    return puzzle
