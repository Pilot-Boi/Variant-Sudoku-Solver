"""PuzzleMadness Thermometer Sudoku — 2025-04-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [7, 0, 4, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 7), (4, 7), (3, 7), (3, 6), (3, 5), (3, 4)])
    puzzle.add_thermometer([(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 5), (1, 5), (1, 4)])
    puzzle.add_thermometer([(5, 4), (5, 3), (5, 2), (5, 1), (4, 1)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (5, 8)])
    puzzle.add_thermometer([(6, 5), (6, 4), (7, 4), (7, 3)])
    puzzle.add_thermometer([(1, 8), (1, 7), (0, 7), (0, 8)])
    puzzle.add_thermometer([(4, 4), (4, 5), (4, 6)])
    puzzle.add_thermometer([(3, 1), (3, 0), (2, 0)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(2, 3), (3, 3), (4, 3)])
    puzzle.add_thermometer([(5, 6), (6, 6), (6, 7)])

    return puzzle
