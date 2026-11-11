"""PuzzleMadness Thermometer Sudoku — 2025-07-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 4, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 4), (4, 5), (5, 5), (5, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(5, 6), (4, 6), (3, 6), (2, 6), (2, 5), (3, 5)])
    puzzle.add_thermometer([(7, 6), (8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(5, 2), (5, 3), (4, 3), (3, 3), (2, 3)])
    puzzle.add_thermometer([(7, 1), (6, 1), (5, 1), (5, 0), (4, 0)])
    puzzle.add_thermometer([(3, 0), (3, 1), (2, 1), (1, 1), (1, 2)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8), (5, 8)])
    puzzle.add_thermometer([(8, 5), (7, 5), (6, 5), (6, 6)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(1, 3), (1, 4), (1, 5)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(8, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6)])

    return puzzle
