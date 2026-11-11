"""PuzzleMadness Thermometer Sudoku — 2025-08-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 3), (5, 3), (6, 3), (6, 4), (7, 4), (7, 5)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_thermometer([(6, 1), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2)])
    puzzle.add_thermometer([(3, 8), (3, 7), (2, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(4, 7), (5, 7), (5, 6), (4, 6), (3, 6)])
    puzzle.add_thermometer([(1, 4), (2, 4), (3, 4), (3, 3), (2, 3)])
    puzzle.add_thermometer([(6, 5), (6, 6), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(0, 2), (1, 2), (1, 1), (0, 1)])
    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8), (6, 7)])
    puzzle.add_thermometer([(2, 0), (3, 0), (3, 1), (2, 1)])
    puzzle.add_thermometer([(5, 1), (4, 1), (4, 0), (5, 0)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 1)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 4)])

    return puzzle
