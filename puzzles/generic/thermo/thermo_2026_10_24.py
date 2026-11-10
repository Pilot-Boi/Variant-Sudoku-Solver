"""PuzzleMadness Thermometer Sudoku — 2026-10-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 3), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 4), (3, 4), (3, 5), (4, 5)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6), (0, 6)])
    puzzle.add_thermometer([(6, 6), (6, 5), (7, 5), (7, 4)])
    puzzle.add_thermometer([(3, 2), (2, 2), (2, 1), (1, 1)])
    puzzle.add_thermometer([(7, 1), (7, 2), (6, 2), (5, 2)])
    puzzle.add_thermometer([(4, 6), (4, 7), (3, 7)])
    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8)])
    puzzle.add_thermometer([(8, 8), (8, 7), (8, 6)])
    puzzle.add_thermometer([(0, 8), (1, 8), (2, 8)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3)])

    return puzzle
