"""PuzzleMadness Thermometer Sudoku — 2025-05-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 8), (1, 7), (1, 6), (1, 5), (1, 4)])
    puzzle.add_thermometer([(1, 2), (1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0), (8, 1), (7, 1)])
    puzzle.add_thermometer([(5, 4), (5, 3), (6, 3), (7, 3)])
    puzzle.add_thermometer([(4, 6), (5, 6), (6, 6), (6, 7)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4), (8, 4)])
    puzzle.add_thermometer([(2, 1), (2, 2), (3, 2)])
    puzzle.add_thermometer([(5, 2), (5, 1), (6, 1)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0)])
    puzzle.add_thermometer([(0, 3), (1, 3), (2, 3)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6)])

    return puzzle
