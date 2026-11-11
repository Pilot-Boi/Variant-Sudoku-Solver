"""PuzzleMadness Thermometer Sudoku — 2025-05-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 6, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 3],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 6), (1, 6), (1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(6, 5), (6, 6), (6, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(4, 1), (4, 0), (3, 0), (2, 0), (1, 0)])
    puzzle.add_thermometer([(5, 3), (5, 4), (5, 5), (4, 5)])
    puzzle.add_thermometer([(5, 7), (4, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(7, 0), (7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(7, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(3, 3), (3, 4), (4, 4), (4, 3)])
    puzzle.add_thermometer([(0, 2), (1, 2), (2, 2), (3, 2)])
    puzzle.add_thermometer([(6, 2), (6, 3), (7, 3)])
    puzzle.add_thermometer([(3, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(4, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(8, 2), (8, 3), (8, 4)])

    return puzzle
