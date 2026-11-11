"""PuzzleMadness Thermometer Sudoku — 2025-08-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 4, 3, 0, 0, 0],
        [3, 0, 0, 0, 0, 9, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (3, 4)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 7), (4, 7), (5, 7)])
    puzzle.add_thermometer([(5, 5), (6, 5), (6, 4), (6, 3)])
    puzzle.add_thermometer([(3, 3), (4, 3), (4, 4), (5, 4)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 6), (2, 6)])
    puzzle.add_thermometer([(2, 2), (1, 2), (1, 3), (2, 3)])
    puzzle.add_thermometer([(3, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(5, 1), (6, 1), (7, 1)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7)])
    puzzle.add_thermometer([(4, 8), (5, 8), (6, 8)])
    puzzle.add_thermometer([(7, 3), (7, 4), (7, 5)])
    puzzle.add_thermometer([(6, 2), (5, 2), (4, 2)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6)])

    return puzzle
