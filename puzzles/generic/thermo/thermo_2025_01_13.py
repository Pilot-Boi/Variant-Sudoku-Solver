"""PuzzleMadness Thermometer Sudoku — 2025-01-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 2), (4, 2), (4, 3), (3, 3), (3, 2), (3, 1)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 5), (1, 5), (1, 4), (0, 4)])
    puzzle.add_thermometer([(6, 6), (5, 6), (5, 7), (5, 8), (4, 8)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3), (7, 3), (6, 3)])
    puzzle.add_thermometer([(4, 4), (4, 5), (4, 6), (4, 7)])
    puzzle.add_thermometer([(3, 7), (3, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(0, 1), (1, 1), (1, 0), (2, 0)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(6, 4), (6, 5), (7, 5), (7, 6)])
    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(7, 0), (7, 1), (6, 1)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 8)])

    return puzzle
