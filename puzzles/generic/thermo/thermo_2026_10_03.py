"""PuzzleMadness Thermometer Sudoku — 2026-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)])
    puzzle.add_thermometer([(7, 6), (7, 5), (7, 4), (7, 3), (6, 3)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 5), (1, 5), (2, 5)])
    puzzle.add_thermometer([(2, 1), (1, 1), (1, 0), (2, 0), (3, 0)])
    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(3, 5), (3, 4), (2, 4), (1, 4)])
    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8), (4, 7)])
    puzzle.add_thermometer([(5, 7), (6, 7), (7, 7)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7)])
    puzzle.add_thermometer([(4, 6), (4, 5), (4, 4)])
    puzzle.add_thermometer([(2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(4, 2), (3, 2), (2, 2)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 1)])
    puzzle.add_thermometer([(6, 4), (6, 5), (6, 6)])

    return puzzle
