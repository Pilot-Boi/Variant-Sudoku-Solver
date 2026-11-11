"""PuzzleMadness Between Lines Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 8],
        [1, 2, 0, 0, 0, 0, 9, 0, 3],
        [0, 0, 0, 0, 0, 0, 3, 0, 2],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [6, 0, 9, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 5, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 0), (7, 0), (7, 1), (6, 1), (5, 0), (4, 0)])
    puzzle.add_between_line([(5, 6), (4, 6), (5, 7), (4, 7), (3, 8)])
    puzzle.add_between_line([(1, 8), (2, 7), (1, 6), (1, 5), (0, 5)])
    puzzle.add_between_line([(4, 2), (5, 2), (6, 3), (5, 4), (4, 4)])
    puzzle.add_between_line([(6, 7), (7, 8), (8, 8), (7, 7)])
    puzzle.add_between_line([(6, 2), (7, 3), (8, 4), (7, 4)])
    puzzle.add_between_line([(6, 5), (5, 5), (4, 5), (3, 5)])
    puzzle.add_between_line([(3, 0), (4, 1), (3, 2), (2, 1)])
    puzzle.add_between_line([(1, 7), (0, 7), (0, 6)])
    puzzle.add_between_line([(1, 3), (1, 4), (2, 4)])
    puzzle.add_between_line([(1, 0), (1, 1), (0, 2)])

    return puzzle
