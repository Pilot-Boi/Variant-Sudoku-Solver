"""PuzzleMadness Thermometer Sudoku — 2025-01-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 5), (7, 5), (6, 5), (5, 5), (5, 6), (4, 6)])
    puzzle.add_thermometer([(5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(3, 3), (4, 3), (5, 3), (5, 4), (4, 4)])
    puzzle.add_thermometer([(4, 1), (5, 1), (6, 1), (7, 1), (8, 1)])
    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7), (7, 7)])
    puzzle.add_thermometer([(1, 4), (1, 3), (0, 3), (0, 4)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0)])
    puzzle.add_thermometer([(6, 4), (7, 4), (8, 4)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 3)])
    puzzle.add_thermometer([(3, 4), (2, 4), (2, 3)])
    puzzle.add_thermometer([(4, 2), (5, 2), (6, 2)])

    return puzzle
