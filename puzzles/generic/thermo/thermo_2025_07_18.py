"""PuzzleMadness Thermometer Sudoku — 2025-07-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (2, 2)])
    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8), (5, 8), (5, 7), (4, 7)])
    puzzle.add_thermometer([(0, 6), (0, 7), (1, 7), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(1, 0), (1, 1), (2, 1), (3, 1), (3, 0)])
    puzzle.add_thermometer([(7, 5), (7, 4), (8, 4), (8, 5), (8, 6)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0), (7, 0), (6, 0)])
    puzzle.add_thermometer([(5, 4), (4, 4), (4, 5), (5, 5)])
    puzzle.add_thermometer([(5, 2), (6, 2), (7, 2), (7, 1)])
    puzzle.add_thermometer([(0, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(6, 3), (5, 3), (4, 3)])
    puzzle.add_thermometer([(2, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(4, 6), (5, 6), (6, 6)])
    puzzle.add_thermometer([(2, 5), (3, 5), (3, 6)])

    return puzzle
