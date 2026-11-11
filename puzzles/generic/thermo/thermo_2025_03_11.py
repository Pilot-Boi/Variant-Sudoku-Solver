"""PuzzleMadness Thermometer Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 6), (3, 6), (3, 7), (4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2)])
    puzzle.add_thermometer([(6, 3), (6, 2), (7, 2), (7, 1), (7, 0)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(5, 8), (5, 7), (5, 6), (6, 6), (6, 7)])
    puzzle.add_thermometer([(3, 2), (3, 1), (4, 1), (4, 0), (3, 0)])
    puzzle.add_thermometer([(2, 7), (1, 7), (0, 7), (0, 6), (1, 6)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(7, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_thermometer([(1, 3), (2, 3), (3, 3)])
    puzzle.add_thermometer([(6, 5), (5, 5), (4, 5)])
    puzzle.add_thermometer([(2, 4), (1, 4), (0, 4)])

    return puzzle
