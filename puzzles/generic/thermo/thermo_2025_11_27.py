"""PuzzleMadness Thermometer Sudoku — 2025-11-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 3, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [5, 7, 0, 3, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 6), (7, 6), (7, 7), (7, 8), (6, 8), (6, 7)])
    puzzle.add_thermometer([(4, 2), (4, 1), (3, 1), (3, 0), (4, 0)])
    puzzle.add_thermometer([(5, 4), (6, 4), (6, 5), (5, 5), (5, 6)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 3), (0, 3), (0, 4)])
    puzzle.add_thermometer([(1, 2), (0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6), (1, 6), (1, 7)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 2), (7, 2)])
    puzzle.add_thermometer([(3, 3), (3, 4), (3, 5), (3, 6)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3)])
    puzzle.add_thermometer([(2, 7), (3, 7), (4, 7)])
    puzzle.add_thermometer([(6, 1), (6, 2), (5, 2)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])

    return puzzle
