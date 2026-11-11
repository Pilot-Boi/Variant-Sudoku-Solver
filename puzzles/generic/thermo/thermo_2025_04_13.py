"""PuzzleMadness Thermometer Sudoku — 2025-04-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 1, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 1), (6, 1), (6, 2), (6, 3), (6, 4), (5, 4)])
    puzzle.add_thermometer([(6, 7), (6, 6), (7, 6), (7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (0, 2), (0, 3)])
    puzzle.add_thermometer([(3, 1), (3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_thermometer([(3, 8), (2, 8), (2, 7), (1, 7)])
    puzzle.add_thermometer([(4, 7), (4, 6), (3, 6), (3, 7)])
    puzzle.add_thermometer([(2, 3), (2, 4), (1, 4), (1, 3)])
    puzzle.add_thermometer([(4, 5), (3, 5), (3, 4), (4, 4)])
    puzzle.add_thermometer([(8, 3), (8, 2), (7, 2), (7, 3)])
    puzzle.add_thermometer([(0, 4), (0, 5), (0, 6)])
    puzzle.add_thermometer([(5, 0), (5, 1), (5, 2)])
    puzzle.add_thermometer([(7, 8), (6, 8), (5, 8)])
    puzzle.add_thermometer([(8, 0), (7, 0), (6, 0)])

    return puzzle
