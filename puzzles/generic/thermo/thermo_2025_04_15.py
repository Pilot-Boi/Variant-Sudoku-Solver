"""PuzzleMadness Thermometer Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 6), (2, 6), (2, 7), (1, 7), (0, 7), (0, 6)])
    puzzle.add_thermometer([(6, 7), (6, 8), (5, 8), (5, 7), (4, 7), (3, 7)])
    puzzle.add_thermometer([(5, 1), (4, 1), (4, 0), (3, 0), (3, 1), (2, 1)])
    puzzle.add_thermometer([(2, 3), (2, 4), (2, 5), (3, 5), (4, 5)])
    puzzle.add_thermometer([(8, 2), (8, 1), (7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(6, 4), (6, 3), (6, 2), (7, 2), (7, 3)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1), (1, 1)])
    puzzle.add_thermometer([(7, 5), (8, 5), (8, 4), (7, 4)])
    puzzle.add_thermometer([(5, 5), (5, 4), (4, 4), (4, 3)])
    puzzle.add_thermometer([(4, 8), (3, 8), (2, 8), (1, 8)])
    puzzle.add_thermometer([(4, 6), (5, 6), (6, 6)])
    puzzle.add_thermometer([(7, 7), (7, 6), (8, 6)])
    puzzle.add_thermometer([(3, 2), (4, 2), (5, 2)])

    return puzzle
