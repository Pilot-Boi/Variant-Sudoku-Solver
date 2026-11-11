"""PuzzleMadness Thermometer Sudoku — 2025-09-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 4), (7, 5), (6, 5), (5, 5), (5, 6), (5, 7)])
    puzzle.add_thermometer([(1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2)])
    puzzle.add_thermometer([(5, 3), (5, 2), (4, 2), (4, 3)])
    puzzle.add_thermometer([(1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(2, 7), (2, 6), (3, 6), (3, 5)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (7, 7)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 4)])
    puzzle.add_thermometer([(4, 6), (4, 5), (4, 4)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(6, 6), (7, 6), (8, 6)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1)])
    puzzle.add_thermometer([(6, 1), (5, 1), (4, 1)])
    puzzle.add_thermometer([(3, 7), (3, 8), (2, 8)])
    puzzle.add_thermometer([(0, 2), (0, 1), (0, 0)])
    puzzle.add_thermometer([(4, 8), (5, 8), (6, 8)])

    return puzzle
