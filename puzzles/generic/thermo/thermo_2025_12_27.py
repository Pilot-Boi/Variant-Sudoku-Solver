"""PuzzleMadness Thermometer Sudoku — 2025-12-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 0, 0, 0, 0, 3, 5],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(1, 3), (1, 2), (1, 1), (2, 1), (2, 2), (2, 3)])
    puzzle.add_thermometer([(4, 2), (5, 2), (5, 3), (6, 3), (6, 4)])
    puzzle.add_thermometer([(4, 7), (4, 6), (4, 5), (4, 4), (4, 3)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6), (1, 6), (1, 7)])
    puzzle.add_thermometer([(7, 7), (6, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(3, 0), (4, 0), (4, 1), (3, 1)])
    puzzle.add_thermometer([(2, 4), (1, 4), (0, 4)])
    puzzle.add_thermometer([(8, 1), (8, 0), (7, 0)])
    puzzle.add_thermometer([(3, 5), (3, 6), (3, 7)])
    puzzle.add_thermometer([(5, 6), (6, 6), (7, 6)])

    return puzzle
