"""PuzzleMadness Thermometer Sudoku — 2025-06-13."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-13'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/13'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 4), (4, 5), (3, 5), (3, 4), (3, 3), (2, 3)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 6), (7, 7), (6, 7), (6, 8)])
    puzzle.add_thermometer([(2, 7), (3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_thermometer([(6, 0), (6, 1), (6, 2), (6, 3)])
    puzzle.add_thermometer([(3, 0), (3, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(0, 4), (0, 5), (0, 6), (0, 7)])
    puzzle.add_thermometer([(5, 8), (5, 7), (4, 7), (4, 8)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(1, 3), (1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(0, 1), (1, 1), (2, 1)])
    puzzle.add_thermometer([(4, 3), (4, 2), (5, 2)])
    puzzle.add_thermometer([(1, 6), (2, 6), (3, 6)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2)])

    return puzzle
