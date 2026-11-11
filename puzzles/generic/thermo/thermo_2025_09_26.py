"""PuzzleMadness Thermometer Sudoku — 2025-09-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 3), (4, 2), (5, 2), (5, 1), (4, 1), (3, 1)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7), (7, 6), (8, 6)])
    puzzle.add_thermometer([(1, 7), (2, 7), (2, 6), (2, 5), (1, 5)])
    puzzle.add_thermometer([(5, 5), (4, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(2, 2), (2, 1), (1, 1), (1, 0), (2, 0)])
    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8), (4, 7), (5, 7)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 2)])
    puzzle.add_thermometer([(6, 6), (5, 6), (4, 6), (3, 6)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(7, 4), (6, 4), (5, 4), (5, 3)])
    puzzle.add_thermometer([(7, 0), (7, 1), (7, 2), (7, 3)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 7), (0, 8)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1)])

    return puzzle
