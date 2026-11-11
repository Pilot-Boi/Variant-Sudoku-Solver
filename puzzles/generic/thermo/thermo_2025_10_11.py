"""PuzzleMadness Thermometer Sudoku — 2025-10-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 4, 0, 0, 9, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])
    puzzle.add_thermometer([(0, 4), (1, 4), (1, 3), (1, 2), (1, 1), (0, 1)])
    puzzle.add_thermometer([(7, 2), (7, 1), (6, 1), (6, 0), (7, 0)])
    puzzle.add_thermometer([(4, 3), (5, 3), (5, 2), (6, 2), (6, 3)])
    puzzle.add_thermometer([(6, 7), (6, 6), (7, 6), (7, 5), (6, 5)])
    puzzle.add_thermometer([(8, 5), (8, 4), (7, 4), (6, 4), (5, 4)])
    puzzle.add_thermometer([(5, 8), (4, 8), (4, 7), (5, 7), (5, 6)])
    puzzle.add_thermometer([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(2, 2), (2, 3), (2, 4), (2, 5)])
    puzzle.add_thermometer([(1, 0), (2, 0), (3, 0), (4, 0)])
    puzzle.add_thermometer([(6, 8), (7, 8), (7, 7), (8, 7)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6), (1, 6)])
    puzzle.add_thermometer([(4, 6), (4, 5), (4, 4)])

    return puzzle
