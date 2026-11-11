"""PuzzleMadness Thermometer Sudoku — 2025-06-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 4), (4, 4), (4, 3), (4, 2), (3, 2), (3, 3)])
    puzzle.add_thermometer([(0, 6), (0, 5), (0, 4), (1, 4), (1, 3), (0, 3)])
    puzzle.add_thermometer([(4, 7), (3, 7), (3, 8), (2, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(4, 0), (4, 1), (3, 1), (3, 0), (2, 0)])
    puzzle.add_thermometer([(8, 3), (8, 2), (7, 2), (6, 2), (5, 2)])
    puzzle.add_thermometer([(8, 5), (7, 5), (6, 5), (6, 4), (7, 4)])
    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(8, 6), (7, 6), (6, 6)])
    puzzle.add_thermometer([(3, 5), (3, 6), (4, 6)])
    puzzle.add_thermometer([(7, 3), (6, 3), (5, 3)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(7, 7), (6, 7), (5, 7)])

    return puzzle
