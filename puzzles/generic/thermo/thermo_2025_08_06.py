"""PuzzleMadness Thermometer Sudoku — 2025-08-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)])
    puzzle.add_thermometer([(4, 6), (4, 5), (3, 5), (2, 5), (2, 4), (3, 4)])
    puzzle.add_thermometer([(2, 8), (3, 8), (3, 7), (4, 7), (5, 7)])
    puzzle.add_thermometer([(7, 5), (7, 6), (7, 7), (7, 8), (6, 8)])
    puzzle.add_thermometer([(1, 4), (0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_thermometer([(7, 3), (6, 3), (6, 4), (7, 4)])
    puzzle.add_thermometer([(3, 0), (4, 0), (4, 1), (3, 1)])
    puzzle.add_thermometer([(6, 1), (6, 2), (5, 2)])
    puzzle.add_thermometer([(1, 2), (1, 3), (2, 3)])
    puzzle.add_thermometer([(5, 4), (5, 3), (4, 3)])
    puzzle.add_thermometer([(5, 6), (5, 5), (6, 5)])
    puzzle.add_thermometer([(1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(2, 1), (2, 2), (3, 2)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 5)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])

    return puzzle
