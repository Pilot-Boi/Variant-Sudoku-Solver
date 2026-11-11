"""PuzzleMadness Thermometer Sudoku — 2025-06-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 4, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 5), (3, 5), (3, 6), (4, 6), (4, 7)])
    puzzle.add_thermometer([(3, 3), (2, 3), (2, 2), (1, 2), (1, 1)])
    puzzle.add_thermometer([(1, 7), (1, 6), (1, 5), (1, 4), (1, 3)])
    puzzle.add_thermometer([(5, 6), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_thermometer([(5, 1), (6, 1), (7, 1), (7, 0)])
    puzzle.add_thermometer([(7, 5), (6, 5), (6, 6), (6, 7)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 3), (8, 3)])
    puzzle.add_thermometer([(4, 2), (4, 3), (5, 3), (5, 4)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8)])
    puzzle.add_thermometer([(1, 0), (2, 0), (3, 0)])
    puzzle.add_thermometer([(2, 4), (2, 5), (2, 6)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(0, 6), (0, 7), (0, 8)])
    puzzle.add_thermometer([(7, 4), (8, 4), (8, 5)])

    return puzzle
