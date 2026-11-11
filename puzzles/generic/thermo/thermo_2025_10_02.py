"""PuzzleMadness Thermometer Sudoku — 2025-10-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 7), (5, 6), (5, 5), (6, 5), (7, 5), (7, 4)])
    puzzle.add_thermometer([(7, 0), (7, 1), (6, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(2, 1), (2, 0), (1, 0), (1, 1), (1, 2)])
    puzzle.add_thermometer([(3, 3), (3, 2), (2, 2), (2, 3)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(7, 7), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(1, 4), (2, 4), (3, 4), (4, 4)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3), (7, 3)])
    puzzle.add_thermometer([(0, 5), (1, 5), (2, 5)])
    puzzle.add_thermometer([(6, 4), (6, 3), (5, 3)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(6, 8), (6, 7), (6, 6)])

    return puzzle
