"""PuzzleMadness Thermometer Sudoku — 2025-07-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 7, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 9, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 1), (7, 1), (6, 1), (6, 2), (7, 2), (8, 2)])
    puzzle.add_thermometer([(2, 3), (2, 2), (1, 2), (1, 3), (1, 4)])
    puzzle.add_thermometer([(5, 2), (4, 2), (4, 3), (5, 3), (6, 3)])
    puzzle.add_thermometer([(6, 7), (6, 8), (5, 8), (5, 7), (4, 7)])
    puzzle.add_thermometer([(3, 0), (3, 1), (2, 1), (1, 1)])
    puzzle.add_thermometer([(1, 6), (1, 5), (0, 5), (0, 6)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 7), (3, 8)])
    puzzle.add_thermometer([(5, 4), (4, 4), (4, 5)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(2, 4), (2, 5), (2, 6)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])

    return puzzle
