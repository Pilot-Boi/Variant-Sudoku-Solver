"""PuzzleMadness Thermometer Sudoku — 2026-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (3, 3)])
    puzzle.add_thermometer([(2, 6), (3, 6), (4, 6), (5, 6), (5, 7), (4, 7)])
    puzzle.add_thermometer([(7, 7), (7, 6), (8, 6), (8, 7), (8, 8)])
    puzzle.add_thermometer([(1, 5), (1, 6), (1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(7, 4), (6, 4), (5, 4), (5, 5)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 3), (6, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7), (6, 6)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(3, 4), (3, 5), (2, 5)])
    puzzle.add_thermometer([(8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0)])
    puzzle.add_thermometer([(0, 3), (1, 3), (1, 4)])

    return puzzle
