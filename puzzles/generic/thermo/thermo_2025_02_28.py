"""PuzzleMadness Thermometer Sudoku — 2025-02-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 2), (4, 3), (5, 3), (5, 4), (5, 5), (4, 5)])
    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7), (6, 8), (7, 8)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 5), (1, 6), (1, 7)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(0, 6), (0, 5), (0, 4), (0, 3), (1, 3)])
    puzzle.add_thermometer([(5, 2), (6, 2), (6, 1), (5, 1)])
    puzzle.add_thermometer([(2, 1), (3, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(1, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(5, 8), (4, 8), (3, 8), (2, 8)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(7, 3), (7, 2), (8, 2)])
    puzzle.add_thermometer([(1, 8), (0, 8), (0, 7)])

    return puzzle
