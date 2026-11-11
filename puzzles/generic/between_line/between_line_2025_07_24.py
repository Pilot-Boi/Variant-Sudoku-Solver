"""PuzzleMadness Between Lines Sudoku — 2025-07-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 6, 7],
        [0, 6, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 6, 0, 7, 0, 0, 0],
        [0, 0, 1, 0, 0, 5, 0, 0, 0],
        [6, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 4), (6, 3), (7, 3), (7, 2), (7, 1), (6, 2)])
    puzzle.add_between_line([(2, 0), (1, 1), (1, 0), (0, 0), (0, 1)])
    puzzle.add_between_line([(1, 8), (0, 7), (1, 7), (2, 6), (1, 6)])
    puzzle.add_between_line([(3, 8), (3, 7), (4, 7), (3, 6), (3, 5)])
    puzzle.add_between_line([(8, 0), (7, 0), (8, 1), (8, 2)])
    puzzle.add_between_line([(7, 8), (7, 7), (6, 6), (5, 6)])
    puzzle.add_between_line([(5, 3), (5, 4), (4, 3), (5, 2)])
    puzzle.add_between_line([(2, 4), (2, 5), (1, 4)])
    puzzle.add_between_line([(1, 3), (0, 3), (1, 2)])
    puzzle.add_between_line([(4, 0), (3, 0), (3, 1)])
    puzzle.add_between_line([(8, 6), (7, 5), (8, 5)])

    return puzzle
