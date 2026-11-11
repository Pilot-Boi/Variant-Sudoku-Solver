"""PuzzleMadness Thermometer Sudoku — 2025-01-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 1, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 5), (0, 6), (1, 6), (1, 7), (0, 7), (0, 8)])
    puzzle.add_thermometer([(4, 2), (4, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_thermometer([(3, 6), (3, 7), (3, 8), (4, 8), (5, 8)])
    puzzle.add_thermometer([(2, 2), (2, 1), (2, 0), (1, 0), (1, 1)])
    puzzle.add_thermometer([(8, 7), (8, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 6), (2, 7)])
    puzzle.add_thermometer([(4, 7), (5, 7), (5, 6), (4, 6)])
    puzzle.add_thermometer([(7, 3), (6, 3), (6, 2)])
    puzzle.add_thermometer([(6, 4), (5, 4), (4, 4)])
    puzzle.add_thermometer([(7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(4, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(8, 4), (8, 3), (8, 2)])
    puzzle.add_thermometer([(1, 2), (1, 3), (1, 4)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2)])

    return puzzle
