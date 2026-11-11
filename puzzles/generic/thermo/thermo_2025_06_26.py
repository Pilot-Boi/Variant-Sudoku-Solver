"""PuzzleMadness Thermometer Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 6, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 8), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5)])
    puzzle.add_thermometer([(6, 6), (7, 6), (8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(5, 3), (5, 2), (6, 2), (7, 2), (8, 2), (8, 1)])
    puzzle.add_thermometer([(4, 2), (3, 2), (3, 3), (2, 3), (2, 4)])
    puzzle.add_thermometer([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(2, 6), (2, 5), (3, 5), (3, 6)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0)])
    puzzle.add_thermometer([(8, 5), (7, 5), (7, 4)])
    puzzle.add_thermometer([(6, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(5, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3)])
    puzzle.add_thermometer([(2, 8), (1, 8), (0, 8)])

    return puzzle
