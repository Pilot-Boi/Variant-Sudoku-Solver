"""PuzzleMadness Thermometer Sudoku — 2025-10-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [5, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7), (6, 6), (5, 6), (4, 6)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 4), (1, 4), (1, 3)])
    puzzle.add_thermometer([(7, 1), (7, 2), (7, 3), (7, 4)])
    puzzle.add_thermometer([(4, 1), (4, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(1, 7), (1, 8), (0, 8), (0, 7)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7), (8, 8)])
    puzzle.add_thermometer([(2, 0), (2, 1), (1, 1), (1, 0)])
    puzzle.add_thermometer([(2, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(5, 2), (6, 2), (6, 1)])
    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8)])
    puzzle.add_thermometer([(4, 3), (4, 4), (4, 5)])
    puzzle.add_thermometer([(2, 6), (2, 7), (2, 8)])
    puzzle.add_thermometer([(7, 6), (7, 5), (6, 5)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])

    return puzzle
