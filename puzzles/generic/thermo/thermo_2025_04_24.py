"""PuzzleMadness Thermometer Sudoku — 2025-04-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 6), (3, 5), (4, 5), (4, 4), (3, 4), (3, 3)])
    puzzle.add_thermometer([(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (6, 5)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8), (8, 7), (7, 7), (7, 6)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 5), (0, 5), (0, 4)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)])
    puzzle.add_thermometer([(4, 1), (5, 1), (5, 2), (5, 3)])
    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8), (5, 8)])
    puzzle.add_thermometer([(6, 6), (5, 6), (4, 6), (4, 7)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 8), (1, 8)])
    puzzle.add_thermometer([(2, 8), (2, 7), (2, 6)])
    puzzle.add_thermometer([(6, 4), (5, 4), (5, 5)])
    puzzle.add_thermometer([(7, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1)])

    return puzzle
