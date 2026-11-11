"""PuzzleMadness Thermometer Sudoku — 2025-01-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 8, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 2), (2, 2), (2, 3), (1, 3), (1, 4), (2, 4)])
    puzzle.add_thermometer([(5, 8), (5, 7), (5, 6), (5, 5), (6, 5)])
    puzzle.add_thermometer([(1, 5), (1, 6), (1, 7), (0, 7), (0, 8)])
    puzzle.add_thermometer([(7, 0), (7, 1), (6, 1), (5, 1), (5, 2)])
    puzzle.add_thermometer([(5, 4), (6, 4), (6, 3), (5, 3), (4, 3)])
    puzzle.add_thermometer([(4, 1), (3, 1), (2, 1), (1, 1)])
    puzzle.add_thermometer([(2, 6), (2, 5), (3, 5), (3, 6)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(4, 7), (3, 7), (3, 8)])
    puzzle.add_thermometer([(1, 8), (2, 8), (2, 7)])

    return puzzle
