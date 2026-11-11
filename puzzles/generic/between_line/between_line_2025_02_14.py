"""PuzzleMadness Between Lines Sudoku — 2025-02-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 2],
        [0, 3, 8, 0, 0, 0, 5, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 5), (1, 4), (0, 4), (1, 3), (2, 3), (2, 2)])
    puzzle.add_between_line([(0, 6), (1, 6), (1, 7), (2, 7), (3, 6)])
    puzzle.add_between_line([(8, 3), (7, 2), (6, 3), (6, 2), (5, 1)])
    puzzle.add_between_line([(6, 1), (5, 0), (6, 0), (7, 1), (8, 2)])
    puzzle.add_between_line([(7, 4), (8, 5), (7, 6), (6, 7), (7, 7)])
    puzzle.add_between_line([(4, 1), (4, 0), (3, 1), (2, 0)])
    puzzle.add_between_line([(5, 5), (4, 4), (3, 4), (4, 5)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 2), (0, 1)])
    puzzle.add_between_line([(6, 4), (6, 5), (6, 6), (5, 7)])
    puzzle.add_between_line([(3, 7), (4, 8), (4, 7)])
    puzzle.add_between_line([(6, 8), (7, 8), (8, 8)])
    puzzle.add_between_line([(1, 0), (1, 1), (2, 1)])

    return puzzle
