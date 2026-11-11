"""PuzzleMadness Thermometer Sudoku — 2025-11-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 7, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 1, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8), (7, 7), (7, 6), (6, 6)])
    puzzle.add_thermometer([(4, 4), (4, 5), (3, 5), (3, 6), (3, 7)])
    puzzle.add_thermometer([(7, 0), (7, 1), (8, 1), (8, 2), (7, 2)])
    puzzle.add_thermometer([(4, 1), (5, 1), (5, 2), (4, 2), (4, 3)])
    puzzle.add_thermometer([(3, 2), (2, 2), (2, 1), (3, 1)])
    puzzle.add_thermometer([(0, 5), (0, 6), (0, 7), (1, 7)])
    puzzle.add_thermometer([(1, 2), (1, 3), (1, 4), (0, 4)])
    puzzle.add_thermometer([(5, 7), (4, 7), (4, 8), (5, 8)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(2, 6), (2, 7), (2, 8)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0)])
    puzzle.add_thermometer([(7, 5), (6, 5), (5, 5)])
    puzzle.add_thermometer([(2, 3), (2, 4), (3, 4)])

    return puzzle
