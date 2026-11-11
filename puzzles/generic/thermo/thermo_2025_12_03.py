"""PuzzleMadness Thermometer Sudoku — 2025-12-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 5, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (4, 0)])
    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7), (6, 6), (6, 5), (6, 4)])
    puzzle.add_thermometer([(4, 6), (5, 6), (5, 5), (5, 4), (5, 3)])
    puzzle.add_thermometer([(2, 8), (2, 7), (2, 6), (3, 6), (3, 7)])
    puzzle.add_thermometer([(1, 3), (1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(7, 8), (6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 2), (1, 2)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 1)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])

    return puzzle
