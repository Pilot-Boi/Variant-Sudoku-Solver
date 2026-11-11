"""PuzzleMadness Thermometer Sudoku — 2025-08-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 1, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (0, 6)])
    puzzle.add_thermometer([(7, 2), (6, 2), (6, 1), (7, 1), (7, 0)])
    puzzle.add_thermometer([(6, 6), (7, 6), (7, 7), (6, 7), (6, 8)])
    puzzle.add_thermometer([(2, 1), (3, 1), (4, 1), (5, 1), (5, 2)])
    puzzle.add_thermometer([(0, 1), (0, 0), (1, 0), (2, 0), (3, 0)])
    puzzle.add_thermometer([(2, 3), (3, 3), (3, 2), (2, 2)])
    puzzle.add_thermometer([(1, 7), (1, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(5, 6), (5, 7), (5, 8)])
    puzzle.add_thermometer([(3, 8), (4, 8), (4, 7)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3)])
    puzzle.add_thermometer([(0, 3), (0, 4), (0, 5)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7)])

    return puzzle
