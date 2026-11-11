"""PuzzleMadness Thermometer Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 7, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 5, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 5), (5, 6), (6, 6), (7, 6), (7, 5), (8, 5)])
    puzzle.add_thermometer([(4, 7), (3, 7), (3, 8), (4, 8), (5, 8), (5, 7)])
    puzzle.add_thermometer([(3, 3), (2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_thermometer([(4, 1), (5, 1), (5, 2), (5, 3), (4, 3), (4, 2)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3), (6, 3)])
    puzzle.add_thermometer([(6, 5), (6, 4), (5, 4)])
    puzzle.add_thermometer([(5, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(0, 1), (1, 1), (1, 0)])
    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(7, 7), (8, 7), (8, 6)])
    puzzle.add_thermometer([(3, 2), (3, 1), (3, 0)])
    puzzle.add_thermometer([(1, 7), (2, 7), (2, 8)])

    return puzzle
