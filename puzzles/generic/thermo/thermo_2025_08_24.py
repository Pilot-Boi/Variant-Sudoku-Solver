"""PuzzleMadness Thermometer Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 8, 0, 0, 3],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0), (8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 5), (2, 5), (3, 5)])
    puzzle.add_thermometer([(4, 5), (4, 4), (5, 4), (5, 3), (4, 3)])
    puzzle.add_thermometer([(3, 2), (4, 2), (4, 1), (4, 0), (5, 0)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 5), (7, 4)])
    puzzle.add_thermometer([(3, 7), (4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(1, 8), (2, 8), (2, 7), (1, 7)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 0), (2, 0)])
    puzzle.add_thermometer([(7, 8), (7, 7), (8, 7)])
    puzzle.add_thermometer([(6, 2), (6, 3), (6, 4)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 2)])

    return puzzle
