"""PuzzleMadness Thermometer Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 5, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 6), (6, 6), (6, 7), (5, 7), (4, 7), (3, 7)])
    puzzle.add_thermometer([(6, 1), (5, 1), (5, 0), (4, 0), (3, 0), (2, 0)])
    puzzle.add_thermometer([(7, 8), (7, 7), (8, 7), (8, 6), (7, 6), (7, 5)])
    puzzle.add_thermometer([(3, 5), (4, 5), (5, 5), (6, 5), (6, 4), (5, 4)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 6), (2, 6), (2, 5)])
    puzzle.add_thermometer([(4, 2), (4, 3), (5, 3), (5, 2)])
    puzzle.add_thermometer([(1, 4), (0, 4), (0, 5), (0, 6)])
    puzzle.add_thermometer([(1, 2), (0, 2), (0, 3), (1, 3)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4), (7, 3)])
    puzzle.add_thermometer([(7, 2), (7, 1), (8, 1), (8, 2)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8)])

    return puzzle
