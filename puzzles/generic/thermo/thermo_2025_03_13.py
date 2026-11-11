"""PuzzleMadness Thermometer Sudoku — 2025-03-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 1, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 2],
        [0, 8, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 4), (4, 3), (5, 3), (5, 2), (4, 2), (4, 1)])
    puzzle.add_thermometer([(2, 6), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_thermometer([(7, 7), (6, 7), (6, 6), (7, 6)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(5, 8), (4, 8), (3, 8), (2, 8)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7), (5, 7)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0), (1, 0)])
    puzzle.add_thermometer([(6, 5), (6, 4), (6, 3)])
    puzzle.add_thermometer([(1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(2, 1), (1, 1), (1, 2)])
    puzzle.add_thermometer([(6, 2), (6, 1), (6, 0)])

    return puzzle
