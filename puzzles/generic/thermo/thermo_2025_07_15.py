"""PuzzleMadness Thermometer Sudoku — 2025-07-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 6, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 8), (2, 7), (1, 7), (0, 7), (0, 6), (1, 6)])
    puzzle.add_thermometer([(5, 1), (4, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_thermometer([(4, 4), (4, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(6, 4), (6, 5), (5, 5), (4, 5)])
    puzzle.add_thermometer([(6, 6), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_thermometer([(3, 5), (2, 5), (1, 5), (1, 4)])
    puzzle.add_thermometer([(0, 0), (1, 0), (1, 1), (1, 2)])
    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6)])
    puzzle.add_thermometer([(6, 1), (6, 2), (6, 3)])
    puzzle.add_thermometer([(3, 2), (2, 2), (2, 3)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (7, 8)])

    return puzzle
