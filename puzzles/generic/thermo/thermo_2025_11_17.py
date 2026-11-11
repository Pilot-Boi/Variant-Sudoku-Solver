"""PuzzleMadness Thermometer Sudoku — 2025-11-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 0), (7, 1), (8, 1), (8, 2), (7, 2), (6, 2)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 5), (8, 5), (8, 6), (7, 6)])
    puzzle.add_thermometer([(2, 6), (3, 6), (3, 5), (2, 5), (1, 5), (1, 4)])
    puzzle.add_thermometer([(6, 8), (6, 7), (6, 6), (6, 5), (6, 4)])
    puzzle.add_thermometer([(1, 7), (1, 6), (0, 6), (0, 7), (0, 8)])
    puzzle.add_thermometer([(5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2), (1, 3)])
    puzzle.add_thermometer([(8, 8), (8, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 4), (5, 5)])
    puzzle.add_thermometer([(3, 2), (2, 2), (2, 3), (3, 3)])
    puzzle.add_thermometer([(4, 3), (4, 4), (3, 4)])
    puzzle.add_thermometer([(4, 5), (4, 6), (5, 6)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 0)])
    puzzle.add_thermometer([(1, 8), (2, 8), (2, 7)])

    return puzzle
