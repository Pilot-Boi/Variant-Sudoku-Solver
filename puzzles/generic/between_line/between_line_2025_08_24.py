"""PuzzleMadness Between Lines Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 8, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 4, 6],
        [0, 0, 0, 3, 0, 0, 0, 0, 2],
        [0, 3, 5, 8, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 5), (5, 4), (4, 3), (5, 2), (5, 1), (5, 0)])
    puzzle.add_between_line([(4, 4), (3, 4), (4, 5), (5, 6), (6, 6)])
    puzzle.add_between_line([(1, 2), (0, 2), (1, 1), (1, 0), (2, 1)])
    puzzle.add_between_line([(2, 8), (2, 7), (1, 7), (1, 8), (0, 7)])
    puzzle.add_between_line([(7, 4), (8, 4), (7, 3), (6, 4)])
    puzzle.add_between_line([(8, 1), (8, 2), (7, 1), (7, 2)])
    puzzle.add_between_line([(1, 4), (2, 5), (1, 5), (2, 6)])
    puzzle.add_between_line([(0, 3), (0, 4), (0, 5)])
    puzzle.add_between_line([(8, 8), (7, 8), (7, 7)])
    puzzle.add_between_line([(8, 6), (7, 5), (8, 5)])
    puzzle.add_between_line([(3, 2), (3, 1), (2, 2)])

    return puzzle
