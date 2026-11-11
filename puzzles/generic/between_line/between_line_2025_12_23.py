"""PuzzleMadness Between Lines Sudoku — 2025-12-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-12-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/12/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 4, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 9],
        [0, 0, 7, 0, 0, 0, 0, 5, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 8, 0, 0, 2, 7, 0, 0],
        [5, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(0, 3), (0, 4), (1, 5), (0, 6), (1, 6), (2, 5)])
    puzzle.add_between_line([(6, 1), (6, 2), (7, 3), (8, 3), (8, 4)])
    puzzle.add_between_line([(2, 7), (3, 6), (4, 5), (5, 4), (5, 5)])
    puzzle.add_between_line([(7, 7), (8, 6), (8, 7), (7, 8), (6, 7)])
    puzzle.add_between_line([(4, 4), (5, 3), (6, 3), (7, 4)])
    puzzle.add_between_line([(4, 3), (3, 4), (2, 3), (1, 4)])
    puzzle.add_between_line([(6, 8), (5, 8), (4, 8), (4, 7)])
    puzzle.add_between_line([(7, 2), (8, 1), (7, 1)])
    puzzle.add_between_line([(3, 3), (2, 2), (1, 1)])
    puzzle.add_between_line([(5, 1), (4, 2), (4, 1)])
    puzzle.add_between_line([(6, 0), (5, 0), (4, 0)])

    return puzzle
