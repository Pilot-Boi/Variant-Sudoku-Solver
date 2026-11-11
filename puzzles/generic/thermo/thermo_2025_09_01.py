"""PuzzleMadness Thermometer Sudoku — 2025-09-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 0), (4, 1), (3, 1), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(7, 4), (7, 5), (7, 6), (8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(6, 2), (6, 3), (6, 4), (6, 5), (6, 6)])
    puzzle.add_thermometer([(4, 4), (3, 4), (3, 3), (4, 3), (4, 2)])
    puzzle.add_thermometer([(2, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(5, 3), (5, 2), (5, 1), (6, 1)])
    puzzle.add_thermometer([(3, 5), (2, 5), (2, 6), (3, 6)])
    puzzle.add_thermometer([(6, 0), (7, 0), (7, 1), (7, 2)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 5), (5, 5)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8), (7, 7)])
    puzzle.add_thermometer([(0, 4), (0, 5), (1, 5), (1, 4)])
    puzzle.add_thermometer([(2, 3), (1, 3), (0, 3)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6)])
    puzzle.add_thermometer([(6, 8), (6, 7), (5, 7)])
    puzzle.add_thermometer([(0, 8), (1, 8), (2, 8)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3)])

    return puzzle
