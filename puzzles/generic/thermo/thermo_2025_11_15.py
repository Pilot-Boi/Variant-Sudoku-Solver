"""PuzzleMadness Thermometer Sudoku — 2025-11-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 3), (6, 2), (6, 1), (5, 1), (5, 2), (5, 3)])
    puzzle.add_thermometer([(2, 7), (1, 7), (0, 7), (0, 8), (1, 8), (2, 8)])
    puzzle.add_thermometer([(1, 4), (1, 3), (2, 3), (2, 2), (1, 2)])
    puzzle.add_thermometer([(6, 6), (5, 6), (5, 5), (5, 4), (4, 4)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (8, 6), (7, 6)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (1, 0), (2, 0)])
    puzzle.add_thermometer([(4, 1), (4, 0), (3, 0), (3, 1), (3, 2)])
    puzzle.add_thermometer([(5, 8), (4, 8), (3, 8), (3, 7), (4, 7)])
    puzzle.add_thermometer([(3, 5), (3, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(7, 4), (7, 5), (6, 5), (6, 4)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(2, 4), (2, 5), (1, 5)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3)])

    return puzzle
