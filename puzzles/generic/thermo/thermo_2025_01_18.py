"""PuzzleMadness Thermometer Sudoku — 2025-01-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 4), (3, 3), (2, 3), (2, 2), (1, 2), (1, 1)])
    puzzle.add_thermometer([(8, 6), (8, 7), (7, 7), (6, 7), (6, 6), (5, 6)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3), (7, 3), (7, 2), (8, 2)])
    puzzle.add_thermometer([(7, 1), (6, 1), (5, 1), (4, 1), (4, 2), (4, 3)])
    puzzle.add_thermometer([(4, 7), (4, 6), (3, 6), (2, 6), (2, 5)])
    puzzle.add_thermometer([(2, 1), (2, 0), (1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(6, 2), (5, 2), (5, 3), (6, 3)])
    puzzle.add_thermometer([(5, 8), (4, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0)])
    puzzle.add_thermometer([(1, 4), (1, 5), (1, 6)])
    puzzle.add_thermometer([(0, 3), (0, 4), (0, 5)])
    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8)])
    puzzle.add_thermometer([(3, 2), (3, 1), (3, 0)])

    return puzzle
