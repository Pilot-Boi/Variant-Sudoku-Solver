"""PuzzleMadness Thermometer Sudoku — 2025-09-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 4), (8, 5), (8, 6), (7, 6), (6, 6), (6, 7)])
    puzzle.add_thermometer([(7, 0), (7, 1), (7, 2), (8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(1, 4), (2, 4), (2, 5), (3, 5), (3, 4), (4, 4)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(5, 2), (4, 2), (4, 1), (3, 1), (3, 0)])
    puzzle.add_thermometer([(5, 6), (5, 7), (4, 7), (4, 6), (3, 6)])
    puzzle.add_thermometer([(4, 3), (5, 3), (6, 3), (6, 2)])
    puzzle.add_thermometer([(0, 6), (0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(0, 1), (0, 2), (1, 2), (2, 2)])
    puzzle.add_thermometer([(6, 0), (6, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(6, 5), (6, 4), (5, 4), (5, 5)])
    puzzle.add_thermometer([(3, 2), (3, 3), (2, 3)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 5)])

    return puzzle
