"""PuzzleMadness Between Lines Sudoku — 2025-03-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 7, 2, 0, 0, 0],
        [4, 0, 0, 1, 0, 0, 7, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 3, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 1, 5, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 1), (5, 0), (6, 0), (7, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(2, 2), (1, 2), (0, 3), (1, 4), (1, 3)])
    puzzle.add_between_line([(8, 6), (7, 6), (6, 7), (6, 8), (5, 8)])
    puzzle.add_between_line([(1, 6), (2, 7), (1, 7), (0, 8), (0, 7)])
    puzzle.add_between_line([(6, 6), (5, 6), (4, 5), (3, 5)])
    puzzle.add_between_line([(4, 0), (4, 1), (4, 2), (4, 3)])
    puzzle.add_between_line([(7, 4), (8, 5), (7, 5), (6, 5)])
    puzzle.add_between_line([(8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_between_line([(7, 8), (8, 7), (7, 7)])
    puzzle.add_between_line([(3, 8), (4, 8), (4, 7)])
    puzzle.add_between_line([(2, 1), (3, 1), (3, 0)])

    return puzzle
