"""PuzzleMadness Thermometer Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 6), (3, 6), (3, 5), (3, 4), (3, 3), (3, 2)])
    puzzle.add_thermometer([(5, 5), (6, 5), (6, 6), (5, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(0, 1), (0, 2), (0, 3), (0, 4), (1, 4)])
    puzzle.add_thermometer([(2, 3), (2, 2), (2, 1), (2, 0), (3, 0)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3), (8, 3)])
    puzzle.add_thermometer([(4, 2), (4, 3), (5, 3), (5, 2)])
    puzzle.add_thermometer([(1, 6), (1, 7), (2, 7), (2, 8)])
    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8)])
    puzzle.add_thermometer([(7, 0), (6, 0), (5, 0)])
    puzzle.add_thermometer([(3, 7), (4, 7), (5, 7)])
    puzzle.add_thermometer([(8, 1), (8, 2), (7, 2)])
    puzzle.add_thermometer([(1, 3), (1, 2), (1, 1)])
    puzzle.add_thermometer([(0, 5), (1, 5), (2, 5)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6)])

    return puzzle
