"""PuzzleMadness Thermometer Sudoku — 2025-07-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8), (5, 8), (5, 7), (4, 7)])
    puzzle.add_thermometer([(8, 4), (7, 4), (6, 4), (6, 3), (6, 2), (5, 2)])
    puzzle.add_thermometer([(3, 1), (2, 1), (2, 2), (3, 2), (3, 3)])
    puzzle.add_thermometer([(2, 6), (3, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(4, 3), (4, 4), (3, 4), (2, 4)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(4, 0), (5, 0), (5, 1), (4, 1)])
    puzzle.add_thermometer([(1, 4), (1, 5), (0, 5), (0, 4)])
    puzzle.add_thermometer([(6, 5), (7, 5), (8, 5)])
    puzzle.add_thermometer([(1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(1, 1), (1, 2), (1, 3)])
    puzzle.add_thermometer([(6, 1), (7, 1), (8, 1)])
    puzzle.add_thermometer([(5, 6), (5, 5), (5, 4)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])

    return puzzle
