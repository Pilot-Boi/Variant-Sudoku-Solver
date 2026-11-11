"""PuzzleMadness Thermometer Sudoku — 2025-02-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2), (4, 2), (4, 1), (4, 0)])
    puzzle.add_thermometer([(3, 7), (3, 6), (3, 5), (2, 5), (2, 6), (2, 7)])
    puzzle.add_thermometer([(5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(8, 4), (7, 4), (6, 4), (6, 5)])
    puzzle.add_thermometer([(1, 3), (1, 4), (0, 4), (0, 5)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 1), (8, 1)])
    puzzle.add_thermometer([(6, 6), (6, 7), (6, 8), (5, 8)])
    puzzle.add_thermometer([(4, 8), (4, 7), (5, 7), (5, 6)])
    puzzle.add_thermometer([(0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(4, 4), (4, 5), (5, 5), (5, 4)])
    puzzle.add_thermometer([(2, 4), (2, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(0, 8), (0, 7), (1, 7)])
    puzzle.add_thermometer([(8, 7), (7, 7), (7, 6)])

    return puzzle
