"""PuzzleMadness Between Lines Sudoku — 2025-06-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 8, 0, 0, 0, 0],
        [6, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [1, 0, 7, 0, 0, 0, 0, 6, 0],
        [0, 0, 6, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 2, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 3, 1, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 5), (3, 4), (2, 5), (1, 4), (0, 4), (0, 3)])
    puzzle.add_between_line([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])
    puzzle.add_between_line([(4, 0), (3, 1), (4, 1), (5, 2), (6, 1)])
    puzzle.add_between_line([(6, 4), (5, 5), (4, 6), (3, 7), (3, 8)])
    puzzle.add_between_line([(7, 4), (8, 3), (8, 4), (8, 5)])
    puzzle.add_between_line([(2, 6), (2, 7), (1, 8), (0, 7)])
    puzzle.add_between_line([(3, 2), (4, 2), (4, 3), (4, 4)])
    puzzle.add_between_line([(7, 1), (8, 2), (8, 1)])
    puzzle.add_between_line([(8, 7), (7, 7), (7, 8)])
    puzzle.add_between_line([(6, 3), (7, 2), (7, 3)])
    puzzle.add_between_line([(6, 6), (6, 7), (6, 8)])

    return puzzle
