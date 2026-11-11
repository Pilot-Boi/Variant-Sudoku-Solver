"""PuzzleMadness Thermometer Sudoku — 2025-12-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2)])
    puzzle.add_thermometer([(0, 2), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1)])
    puzzle.add_thermometer([(4, 8), (4, 7), (3, 7), (3, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(8, 8), (8, 7), (7, 7), (6, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_thermometer([(7, 1), (7, 2), (8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(3, 2), (4, 2), (4, 3), (4, 4), (3, 4)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6), (1, 6)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0), (5, 0)])
    puzzle.add_thermometer([(1, 4), (0, 4), (0, 3), (1, 3)])
    puzzle.add_thermometer([(1, 8), (2, 8), (3, 8)])

    return puzzle
