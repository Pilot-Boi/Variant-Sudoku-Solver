"""PuzzleMadness Thermometer Sudoku — 2025-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 1), (5, 1), (5, 2), (4, 2), (4, 3), (5, 3)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(6, 8), (6, 7), (7, 7), (7, 6), (8, 6)])
    puzzle.add_thermometer([(0, 4), (0, 3), (1, 3), (1, 4), (1, 5)])
    puzzle.add_thermometer([(2, 0), (1, 0), (1, 1), (1, 2)])
    puzzle.add_thermometer([(4, 8), (3, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(7, 5), (7, 4), (8, 4), (8, 5)])
    puzzle.add_thermometer([(2, 2), (2, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(4, 5), (3, 5), (3, 4), (4, 4)])
    puzzle.add_thermometer([(1, 8), (1, 7), (0, 7)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 5)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(7, 1), (7, 2), (6, 2)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8)])
    puzzle.add_thermometer([(4, 0), (5, 0), (6, 0)])

    return puzzle
