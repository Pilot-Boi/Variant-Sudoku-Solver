"""PuzzleMadness Thermometer Sudoku — 2025-11-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (5, 8), (5, 7), (5, 6)])
    puzzle.add_thermometer([(2, 2), (3, 2), (4, 2), (4, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(2, 6), (3, 6), (3, 5), (2, 5), (1, 5), (1, 6)])
    puzzle.add_thermometer([(7, 2), (7, 1), (6, 1), (6, 0), (5, 0)])
    puzzle.add_thermometer([(8, 7), (8, 6), (8, 5), (7, 5), (6, 5)])
    puzzle.add_thermometer([(4, 7), (4, 6), (4, 5), (4, 4), (5, 4)])
    puzzle.add_thermometer([(3, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3), (6, 3)])
    puzzle.add_thermometer([(0, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 8), (2, 8)])
    puzzle.add_thermometer([(1, 0), (1, 1), (1, 2), (0, 2)])
    puzzle.add_thermometer([(0, 3), (0, 4), (1, 4)])
    puzzle.add_thermometer([(6, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1)])
    puzzle.add_thermometer([(6, 6), (6, 7), (7, 7)])

    return puzzle
