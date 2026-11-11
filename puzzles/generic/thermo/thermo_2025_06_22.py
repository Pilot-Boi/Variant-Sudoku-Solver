"""PuzzleMadness Thermometer Sudoku — 2025-06-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 9, 7, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 7), (6, 7), (6, 6), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(2, 8), (3, 8), (3, 7), (4, 7), (4, 8), (5, 8)])
    puzzle.add_thermometer([(3, 6), (4, 6), (5, 6), (5, 5), (4, 5)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4), (2, 4), (2, 3)])
    puzzle.add_thermometer([(8, 4), (8, 5), (7, 5), (7, 4), (6, 4)])
    puzzle.add_thermometer([(5, 1), (6, 1), (6, 0), (7, 0)])
    puzzle.add_thermometer([(1, 4), (1, 3), (1, 2), (1, 1)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(2, 5), (1, 5), (0, 5), (0, 4)])
    puzzle.add_thermometer([(2, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(4, 2), (5, 2), (6, 2)])

    return puzzle
