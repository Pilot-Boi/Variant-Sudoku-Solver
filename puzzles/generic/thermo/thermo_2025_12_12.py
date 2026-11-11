"""PuzzleMadness Thermometer Sudoku — 2025-12-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [3, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 2, 6, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (6, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6), (1, 5), (0, 5)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 2), (5, 1), (6, 1)])
    puzzle.add_thermometer([(3, 1), (2, 1), (1, 1), (1, 2), (0, 2)])
    puzzle.add_thermometer([(8, 5), (8, 4), (7, 4), (7, 5)])
    puzzle.add_thermometer([(4, 0), (4, 1), (4, 2), (4, 3)])
    puzzle.add_thermometer([(5, 4), (5, 5), (5, 6), (6, 6)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(7, 6), (7, 7), (8, 7), (8, 6)])
    puzzle.add_thermometer([(3, 8), (3, 7), (4, 7)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0)])
    puzzle.add_thermometer([(1, 8), (2, 8), (2, 7)])

    return puzzle
