"""PuzzleMadness Thermometer Sudoku — 2025-01-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 3, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4), (7, 5), (7, 6), (8, 6)])
    puzzle.add_thermometer([(1, 6), (1, 7), (1, 8), (0, 8), (0, 7)])
    puzzle.add_thermometer([(2, 5), (2, 6), (3, 6), (3, 5), (3, 4)])
    puzzle.add_thermometer([(7, 1), (7, 2), (8, 2), (8, 3)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 2), (6, 2)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (1, 2)])
    puzzle.add_thermometer([(6, 8), (7, 8), (7, 7), (6, 7)])
    puzzle.add_thermometer([(4, 8), (4, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(3, 2), (3, 3), (2, 3)])
    puzzle.add_thermometer([(4, 3), (4, 2), (4, 1)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])
    puzzle.add_thermometer([(5, 6), (5, 5), (6, 5)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0)])

    return puzzle
