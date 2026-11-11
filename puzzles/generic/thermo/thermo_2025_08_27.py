"""PuzzleMadness Thermometer Sudoku — 2025-08-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (6, 7), (7, 7), (8, 7)])
    puzzle.add_thermometer([(4, 8), (4, 7), (3, 7), (3, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(7, 3), (6, 3), (6, 4), (7, 4), (8, 4), (8, 3)])
    puzzle.add_thermometer([(7, 0), (6, 0), (5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(2, 8), (2, 7), (1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(3, 4), (3, 3), (2, 3), (2, 4), (1, 4)])
    puzzle.add_thermometer([(5, 4), (4, 4), (4, 3), (5, 3)])
    puzzle.add_thermometer([(3, 5), (2, 5), (1, 5), (0, 5)])
    puzzle.add_thermometer([(2, 2), (1, 2), (0, 2)])
    puzzle.add_thermometer([(8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(1, 1), (1, 0), (0, 0)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 4)])

    return puzzle
