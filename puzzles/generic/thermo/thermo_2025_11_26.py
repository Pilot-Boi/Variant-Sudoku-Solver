"""PuzzleMadness Thermometer Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 2), (2, 2), (3, 2), (3, 1), (4, 1), (5, 1)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8), (1, 7), (2, 7), (3, 7)])
    puzzle.add_thermometer([(4, 4), (4, 5), (4, 6), (3, 6), (3, 5)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6), (2, 5), (1, 5)])
    puzzle.add_thermometer([(4, 7), (5, 7), (5, 6), (6, 6)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (8, 2)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0), (7, 1)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 2)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 3)])
    puzzle.add_thermometer([(7, 5), (6, 5), (6, 4)])
    puzzle.add_thermometer([(7, 7), (7, 8), (8, 8)])
    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])

    return puzzle
