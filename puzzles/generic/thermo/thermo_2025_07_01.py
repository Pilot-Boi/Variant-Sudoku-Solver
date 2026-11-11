"""PuzzleMadness Thermometer Sudoku — 2025-07-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [5, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8), (4, 7), (4, 6), (5, 6)])
    puzzle.add_thermometer([(5, 7), (6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_thermometer([(1, 5), (0, 5), (0, 4), (1, 4), (1, 3)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(1, 0), (2, 0), (3, 0), (3, 1), (4, 1)])
    puzzle.add_thermometer([(4, 2), (3, 2), (3, 3), (2, 3), (2, 2)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 4), (5, 5)])
    puzzle.add_thermometer([(1, 8), (1, 7), (0, 7), (0, 8)])
    puzzle.add_thermometer([(3, 4), (4, 4), (4, 5), (3, 5)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(3, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(5, 1), (5, 2), (6, 2)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(8, 8), (8, 7), (7, 7)])

    return puzzle
