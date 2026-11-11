"""PuzzleMadness Between Lines Sudoku — 2025-02-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [8, 7, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(1, 6), (1, 5), (0, 5), (1, 4), (2, 5), (3, 5)])
    puzzle.add_between_line([(4, 1), (3, 2), (2, 3), (3, 3), (4, 2)])
    puzzle.add_between_line([(6, 3), (6, 4), (7, 5), (7, 4), (8, 4)])
    puzzle.add_between_line([(7, 7), (8, 7), (7, 6), (6, 7), (6, 6)])
    puzzle.add_between_line([(0, 1), (0, 0), (1, 1), (2, 0), (3, 0)])
    puzzle.add_between_line([(4, 3), (5, 4), (6, 5), (5, 5)])
    puzzle.add_between_line([(4, 8), (5, 8), (5, 7), (4, 7)])
    puzzle.add_between_line([(8, 3), (7, 3), (8, 2), (7, 1)])
    puzzle.add_between_line([(6, 0), (6, 1), (6, 2), (7, 2)])
    puzzle.add_between_line([(7, 0), (8, 0), (8, 1)])
    puzzle.add_between_line([(0, 8), (1, 7), (2, 8)])
    puzzle.add_between_line([(1, 3), (0, 4), (0, 3)])

    return puzzle
