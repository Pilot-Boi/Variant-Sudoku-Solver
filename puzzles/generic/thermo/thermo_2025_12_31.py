"""PuzzleMadness Thermometer Sudoku — 2025-12-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 6), (5, 6), (4, 6), (3, 6), (3, 7), (4, 7)])
    puzzle.add_thermometer([(4, 2), (3, 2), (3, 1), (2, 1), (2, 0), (3, 0)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0), (4, 1), (5, 1), (6, 1)])
    puzzle.add_thermometer([(0, 5), (0, 4), (1, 4), (1, 3), (0, 3)])
    puzzle.add_thermometer([(5, 3), (6, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(3, 4), (4, 4), (5, 4), (5, 5)])
    puzzle.add_thermometer([(7, 4), (7, 5), (6, 5), (6, 4)])
    puzzle.add_thermometer([(7, 6), (7, 7), (8, 7), (8, 6)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(6, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(2, 3), (3, 3), (4, 3)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1)])

    return puzzle
