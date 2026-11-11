"""PuzzleMadness Thermometer Sudoku — 2025-03-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 5, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 8), (2, 8), (2, 7), (1, 7), (1, 6), (0, 6)])
    puzzle.add_thermometer([(1, 4), (1, 3), (0, 3), (0, 2), (0, 1), (1, 1)])
    puzzle.add_thermometer([(4, 0), (4, 1), (3, 1), (3, 0), (2, 0)])
    puzzle.add_thermometer([(5, 5), (5, 4), (4, 4), (4, 5), (3, 5)])
    puzzle.add_thermometer([(7, 1), (6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_thermometer([(3, 6), (4, 6), (5, 6), (5, 7), (4, 7)])
    puzzle.add_thermometer([(7, 5), (7, 4), (7, 3), (7, 2)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (7, 7)])
    puzzle.add_thermometer([(2, 6), (2, 5), (2, 4)])
    puzzle.add_thermometer([(2, 2), (3, 2), (4, 2)])
    puzzle.add_thermometer([(8, 2), (8, 3), (8, 4)])
    puzzle.add_thermometer([(8, 6), (7, 6), (6, 6)])

    return puzzle
