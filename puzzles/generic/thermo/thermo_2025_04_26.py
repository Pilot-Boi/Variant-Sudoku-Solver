"""PuzzleMadness Thermometer Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 6), (4, 6), (4, 5), (3, 5), (2, 5), (2, 6)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])
    puzzle.add_thermometer([(8, 7), (8, 6), (7, 6), (7, 5), (8, 5)])
    puzzle.add_thermometer([(3, 3), (4, 3), (5, 3), (5, 4), (4, 4)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3), (6, 3)])
    puzzle.add_thermometer([(7, 1), (6, 1), (6, 0), (7, 0)])
    puzzle.add_thermometer([(3, 2), (3, 1), (4, 1), (5, 1)])
    puzzle.add_thermometer([(2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(5, 5), (6, 5), (6, 6)])
    puzzle.add_thermometer([(1, 4), (2, 4), (3, 4)])

    return puzzle
