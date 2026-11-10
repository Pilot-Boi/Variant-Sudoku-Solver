"""PuzzleMadness Thermometer Sudoku — 2026-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 3), (5, 4), (4, 4), (3, 4), (3, 3), (3, 2)])
    puzzle.add_thermometer([(3, 6), (4, 6), (5, 6), (5, 7), (5, 8), (4, 8)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (8, 2), (8, 1)])
    puzzle.add_thermometer([(1, 5), (1, 6), (2, 6), (2, 7), (1, 7)])
    puzzle.add_thermometer([(2, 2), (2, 3), (1, 3), (1, 4), (2, 4)])
    puzzle.add_thermometer([(7, 4), (8, 4), (8, 3), (7, 3), (6, 3)])
    puzzle.add_thermometer([(2, 0), (1, 0), (1, 1), (2, 1)])
    puzzle.add_thermometer([(3, 1), (4, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(6, 7), (6, 8), (7, 8), (7, 7)])
    puzzle.add_thermometer([(5, 5), (6, 5), (7, 5)])
    puzzle.add_thermometer([(8, 8), (8, 7), (8, 6)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(1, 8), (2, 8), (3, 8)])

    return puzzle
