"""PuzzleMadness Thermometer Sudoku — 2025-02-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 2, 0, 0],
        [0, 6, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 8), (6, 8), (5, 8), (4, 8), (3, 8), (2, 8)])
    puzzle.add_thermometer([(6, 2), (5, 2), (4, 2), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3), (7, 4), (7, 5), (6, 5)])
    puzzle.add_thermometer([(4, 5), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3)])
    puzzle.add_thermometer([(8, 8), (8, 7), (7, 7), (7, 6)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7), (1, 6)])
    puzzle.add_thermometer([(4, 3), (3, 3), (2, 3), (2, 4)])
    puzzle.add_thermometer([(5, 0), (5, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(1, 0), (1, 1), (2, 1), (2, 0)])
    puzzle.add_thermometer([(7, 2), (7, 1), (8, 1)])
    puzzle.add_thermometer([(5, 7), (6, 7), (6, 6)])
    puzzle.add_thermometer([(0, 5), (0, 6), (0, 7)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1)])

    return puzzle
