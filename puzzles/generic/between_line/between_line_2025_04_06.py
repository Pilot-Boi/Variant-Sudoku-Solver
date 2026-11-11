"""PuzzleMadness Between Lines Sudoku — 2025-04-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 1, 0],
        [5, 0, 0, 0, 8, 0, 0, 0, 0],
        [8, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(4, 8), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8)])
    puzzle.add_between_line([(4, 2), (4, 1), (3, 2), (2, 1), (1, 0)])
    puzzle.add_between_line([(6, 0), (5, 0), (5, 1), (6, 1), (5, 2)])
    puzzle.add_between_line([(5, 8), (6, 8), (7, 8), (7, 7), (6, 6)])
    puzzle.add_between_line([(3, 4), (3, 3), (4, 3), (5, 4), (6, 4)])
    puzzle.add_between_line([(5, 5), (4, 6), (3, 6), (2, 6)])
    puzzle.add_between_line([(7, 3), (6, 3), (7, 2), (6, 2)])
    puzzle.add_between_line([(8, 4), (7, 4), (7, 5), (7, 6)])
    puzzle.add_between_line([(1, 2), (1, 3), (0, 4), (1, 5)])
    puzzle.add_between_line([(8, 0), (7, 0), (7, 1)])
    puzzle.add_between_line([(2, 3), (1, 4), (2, 4)])
    puzzle.add_between_line([(0, 7), (1, 6), (2, 5)])

    return puzzle
