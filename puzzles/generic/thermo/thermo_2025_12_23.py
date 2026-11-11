"""PuzzleMadness Thermometer Sudoku — 2025-12-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 8), (0, 8), (0, 7), (1, 7), (2, 7), (2, 6)])
    puzzle.add_thermometer([(2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 1), (7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(4, 0), (4, 1), (3, 1), (3, 2), (4, 2)])
    puzzle.add_thermometer([(4, 6), (5, 6), (5, 7), (4, 7), (3, 7)])
    puzzle.add_thermometer([(7, 5), (7, 6), (6, 6), (6, 5), (5, 5)])
    puzzle.add_thermometer([(1, 2), (0, 2), (0, 1), (1, 1), (1, 0)])
    puzzle.add_thermometer([(1, 4), (1, 5), (1, 6), (0, 6)])
    puzzle.add_thermometer([(6, 7), (6, 8), (7, 8), (7, 7)])
    puzzle.add_thermometer([(3, 4), (3, 5), (4, 5), (4, 4)])
    puzzle.add_thermometer([(8, 5), (8, 4), (7, 4)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0)])

    return puzzle
