"""PuzzleMadness Between Lines Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [3, 0, 0, 0, 5, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 8), (3, 7), (4, 8), (5, 8), (4, 7), (5, 7)])
    puzzle.add_between_line([(2, 4), (1, 4), (0, 5), (1, 6), (2, 5)])
    puzzle.add_between_line([(7, 3), (7, 4), (8, 5), (8, 6), (7, 6)])
    puzzle.add_between_line([(2, 3), (2, 2), (2, 1), (3, 1), (4, 1)])
    puzzle.add_between_line([(4, 2), (4, 3), (5, 3), (6, 2), (7, 1)])
    puzzle.add_between_line([(8, 1), (8, 2), (7, 2), (6, 3)])
    puzzle.add_between_line([(2, 6), (1, 7), (2, 7), (1, 8)])
    puzzle.add_between_line([(5, 0), (5, 1), (6, 1), (6, 0)])
    puzzle.add_between_line([(0, 4), (0, 3), (1, 3), (0, 2)])
    puzzle.add_between_line([(1, 0), (1, 1), (1, 2)])
    puzzle.add_between_line([(6, 6), (5, 5), (6, 5)])
    puzzle.add_between_line([(5, 6), (4, 6), (3, 5)])

    return puzzle
