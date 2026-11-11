"""PuzzleMadness Between Lines Sudoku — 2025-05-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-05-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/5/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 7, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 7, 0, 1, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 4), (1, 5), (0, 5), (1, 4), (2, 3), (3, 3)])
    puzzle.add_between_line([(4, 1), (5, 0), (5, 1), (6, 1), (7, 1)])
    puzzle.add_between_line([(6, 2), (5, 3), (4, 3), (4, 2), (5, 2)])
    puzzle.add_between_line([(8, 0), (7, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_between_line([(0, 8), (1, 8), (2, 7), (3, 7), (2, 8)])
    puzzle.add_between_line([(1, 3), (2, 2), (3, 2), (2, 1)])
    puzzle.add_between_line([(4, 7), (4, 8), (5, 8), (6, 7)])
    puzzle.add_between_line([(7, 8), (8, 7), (7, 6), (7, 5)])
    puzzle.add_between_line([(5, 7), (4, 6), (5, 5)])
    puzzle.add_between_line([(7, 7), (6, 6), (5, 6)])
    puzzle.add_between_line([(7, 2), (7, 3), (7, 4)])

    return puzzle
