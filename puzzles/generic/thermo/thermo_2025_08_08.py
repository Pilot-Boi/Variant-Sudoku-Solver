"""PuzzleMadness Thermometer Sudoku — 2025-08-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 4, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 4), (6, 5), (7, 5), (7, 4), (8, 4), (8, 5)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_thermometer([(7, 6), (6, 6), (6, 7), (6, 8), (5, 8)])
    puzzle.add_thermometer([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_thermometer([(2, 7), (3, 7), (3, 6), (2, 6)])
    puzzle.add_thermometer([(4, 3), (5, 3), (5, 2), (6, 2)])
    puzzle.add_thermometer([(8, 3), (8, 2), (7, 2), (7, 1)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0), (4, 0)])
    puzzle.add_thermometer([(5, 4), (4, 4), (4, 5), (5, 5)])
    puzzle.add_thermometer([(3, 8), (4, 8), (4, 7)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])

    return puzzle
