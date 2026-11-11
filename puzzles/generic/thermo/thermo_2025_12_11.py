"""PuzzleMadness Thermometer Sudoku — 2025-12-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 4, 1, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (4, 6)])
    puzzle.add_thermometer([(5, 2), (4, 2), (4, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_thermometer([(2, 3), (2, 2), (1, 2), (1, 1), (0, 1), (0, 2)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 5), (7, 6), (7, 7)])
    puzzle.add_thermometer([(7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(1, 5), (1, 6), (2, 6), (2, 5)])
    puzzle.add_thermometer([(6, 6), (6, 7), (6, 8), (7, 8)])
    puzzle.add_thermometer([(6, 3), (6, 2), (6, 1)])
    puzzle.add_thermometer([(0, 8), (1, 8), (2, 8)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(3, 5), (3, 6), (3, 7)])

    return puzzle
