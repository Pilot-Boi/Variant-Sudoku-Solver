"""PuzzleMadness Thermometer Sudoku — 2025-02-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 5), (6, 5), (6, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_thermometer([(3, 7), (4, 7), (4, 6), (4, 5), (3, 5), (2, 5)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 7), (6, 7), (6, 6), (5, 6)])
    puzzle.add_thermometer([(5, 1), (6, 1), (7, 1), (7, 0), (6, 0), (5, 0)])
    puzzle.add_thermometer([(3, 3), (4, 3), (5, 3), (5, 4), (4, 4)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_thermometer([(2, 2), (1, 2), (0, 2), (0, 1), (1, 1)])
    puzzle.add_thermometer([(4, 8), (3, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 4)])
    puzzle.add_thermometer([(1, 7), (1, 6), (0, 6), (0, 7)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])

    return puzzle
