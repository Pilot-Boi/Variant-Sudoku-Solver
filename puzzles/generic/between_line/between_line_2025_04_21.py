"""PuzzleMadness Between Lines Sudoku — 2025-04-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 5, 0],
        [0, 0, 5, 0, 6, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 9],
        [3, 0, 0, 0, 0, 7, 0, 1, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 6), (2, 5), (1, 6), (2, 7), (1, 7), (0, 7)])
    puzzle.add_between_line([(0, 0), (0, 1), (0, 2), (1, 3), (2, 3)])
    puzzle.add_between_line([(6, 2), (6, 1), (5, 2), (4, 2), (5, 1)])
    puzzle.add_between_line([(3, 3), (3, 4), (4, 4), (5, 4), (6, 4)])
    puzzle.add_between_line([(3, 0), (3, 1), (2, 2), (2, 1)])
    puzzle.add_between_line([(1, 5), (0, 4), (0, 3), (1, 4)])
    puzzle.add_between_line([(8, 5), (7, 6), (7, 5), (6, 6)])
    puzzle.add_between_line([(5, 6), (4, 6), (5, 7), (5, 8)])
    puzzle.add_between_line([(4, 5), (5, 5), (6, 5)])
    puzzle.add_between_line([(6, 3), (7, 4), (8, 3)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 6)])
    puzzle.add_between_line([(7, 3), (8, 2), (7, 2)])

    return puzzle
