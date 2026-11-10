"""PuzzleMadness Thermometer Sudoku — 2026-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [4, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8), (7, 7), (7, 6), (6, 6)])
    puzzle.add_thermometer([(4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(5, 7), (5, 6), (5, 5), (5, 4), (4, 4), (3, 4)])
    puzzle.add_thermometer([(7, 1), (7, 2), (6, 2), (6, 3), (6, 4)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3), (8, 3)])
    puzzle.add_thermometer([(1, 8), (2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(3, 0), (2, 0), (1, 0)])
    puzzle.add_thermometer([(7, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(8, 6), (8, 5), (7, 5)])

    return puzzle
