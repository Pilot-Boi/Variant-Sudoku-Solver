"""PuzzleMadness Thermometer Sudoku — 2025-08-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 3), (6, 3), (6, 2), (6, 1), (7, 1), (7, 2)])
    puzzle.add_thermometer([(1, 4), (1, 3), (1, 2), (2, 2), (2, 1), (1, 1)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_thermometer([(4, 5), (4, 6), (4, 7), (4, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(7, 8), (7, 7), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4)])
    puzzle.add_thermometer([(3, 2), (3, 3), (4, 3), (5, 3)])
    puzzle.add_thermometer([(5, 2), (5, 1), (4, 1), (4, 2)])
    puzzle.add_thermometer([(1, 7), (1, 8), (2, 8)])
    puzzle.add_thermometer([(0, 1), (0, 2), (0, 3)])
    puzzle.add_thermometer([(0, 6), (0, 7), (0, 8)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4)])
    puzzle.add_thermometer([(2, 4), (2, 5), (1, 5)])

    return puzzle
