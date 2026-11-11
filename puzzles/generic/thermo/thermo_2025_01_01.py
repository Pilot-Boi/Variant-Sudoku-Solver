"""PuzzleMadness Thermometer Sudoku — 2025-01-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 4, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 2), (3, 2), (2, 2), (2, 1), (3, 1), (3, 0)])
    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4), (8, 4), (8, 5), (7, 5)])
    puzzle.add_thermometer([(2, 7), (1, 7), (0, 7), (0, 6), (1, 6), (2, 6)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 2), (6, 2), (7, 2)])
    puzzle.add_thermometer([(3, 8), (4, 8), (4, 7), (5, 7)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(2, 3), (1, 3), (1, 4), (2, 4)])
    puzzle.add_thermometer([(7, 8), (7, 7), (8, 7), (8, 6)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(3, 6), (4, 6), (5, 6)])
    puzzle.add_thermometer([(3, 4), (4, 4), (4, 3)])
    puzzle.add_thermometer([(7, 6), (6, 6), (6, 7)])
    puzzle.add_thermometer([(1, 5), (2, 5), (3, 5)])

    return puzzle
