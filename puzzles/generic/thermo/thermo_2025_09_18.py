"""PuzzleMadness Thermometer Sudoku — 2025-09-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [3, 0, 5, 0, 0, 0, 9, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 8), (5, 8), (5, 7), (5, 6), (4, 6), (3, 6)])
    puzzle.add_thermometer([(0, 5), (0, 4), (1, 4), (1, 5), (2, 5), (2, 4)])
    puzzle.add_thermometer([(7, 2), (7, 1), (7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])
    puzzle.add_thermometer([(1, 1), (1, 2), (1, 3), (0, 3), (0, 2)])
    puzzle.add_thermometer([(7, 5), (8, 5), (8, 4), (7, 4), (6, 4)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7), (8, 7)])
    puzzle.add_thermometer([(2, 6), (1, 6), (0, 6)])
    puzzle.add_thermometer([(6, 6), (6, 5), (5, 5)])

    return puzzle
