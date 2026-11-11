"""PuzzleMadness Thermometer Sudoku — 2025-10-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 3, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (6, 4), (5, 4), (4, 4), (4, 3), (5, 3)])
    puzzle.add_thermometer([(3, 8), (3, 7), (3, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_thermometer([(1, 6), (2, 6), (2, 5), (1, 5), (1, 4)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7), (6, 7), (6, 8)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 5), (8, 5), (8, 4)])
    puzzle.add_thermometer([(4, 1), (4, 2), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(6, 1), (6, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0), (3, 0)])
    puzzle.add_thermometer([(3, 3), (3, 4), (3, 5)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1)])
    puzzle.add_thermometer([(5, 7), (5, 6), (5, 5)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])

    return puzzle
