"""PuzzleMadness Thermometer Sudoku — 2025-07-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 2, 6, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 2), (7, 2), (8, 2), (8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(5, 3), (5, 4), (4, 4), (3, 4), (3, 3), (4, 3)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8), (1, 7), (1, 6), (2, 6)])
    puzzle.add_thermometer([(4, 1), (3, 1), (3, 2), (4, 2), (5, 2)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (6, 7), (7, 7)])
    puzzle.add_thermometer([(6, 4), (7, 4), (7, 5), (8, 5), (8, 4)])
    puzzle.add_thermometer([(1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_thermometer([(2, 2), (2, 1), (1, 1), (1, 0)])
    puzzle.add_thermometer([(4, 7), (4, 6), (5, 6)])
    puzzle.add_thermometer([(3, 6), (3, 7), (3, 8)])
    puzzle.add_thermometer([(1, 5), (0, 5), (0, 6)])
    puzzle.add_thermometer([(7, 0), (6, 0), (5, 0)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2)])

    return puzzle
