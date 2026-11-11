"""PuzzleMadness Thermometer Sudoku — 2025-07-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 6), (1, 6), (1, 7), (1, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(7, 2), (7, 1), (6, 1), (6, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7), (7, 7), (7, 6)])
    puzzle.add_thermometer([(5, 5), (5, 4), (5, 3), (4, 3), (4, 4)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (0, 2), (1, 2)])
    puzzle.add_thermometer([(8, 3), (7, 3), (7, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(0, 4), (1, 4), (2, 4), (2, 5)])
    puzzle.add_thermometer([(6, 7), (6, 8), (5, 8), (5, 7)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(4, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])

    return puzzle
