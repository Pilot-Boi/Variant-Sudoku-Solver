"""PuzzleMadness Thermometer Sudoku — 2025-08-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0), (4, 1), (4, 2), (4, 3)])
    puzzle.add_thermometer([(4, 8), (3, 8), (3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 5), (7, 4), (8, 4)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 6), (0, 6), (0, 7)])
    puzzle.add_thermometer([(8, 7), (7, 7), (7, 8), (8, 8)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 2), (8, 1)])
    puzzle.add_thermometer([(2, 0), (2, 1), (2, 2), (2, 3)])
    puzzle.add_thermometer([(5, 5), (4, 5), (3, 5), (2, 5)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 2), (1, 2)])
    puzzle.add_thermometer([(6, 2), (5, 2), (5, 3), (6, 3)])
    puzzle.add_thermometer([(7, 1), (6, 1), (5, 1)])
    puzzle.add_thermometer([(5, 4), (4, 4), (3, 4)])

    return puzzle
