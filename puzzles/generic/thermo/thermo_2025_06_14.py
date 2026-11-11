"""PuzzleMadness Thermometer Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 7), (7, 8), (8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_thermometer([(2, 1), (2, 0), (1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(4, 4), (4, 3), (4, 2), (4, 1), (5, 1)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1), (8, 0), (7, 0)])
    puzzle.add_thermometer([(3, 6), (3, 5), (4, 5), (4, 6), (4, 7)])
    puzzle.add_thermometer([(5, 8), (5, 7), (6, 7), (6, 6)])
    puzzle.add_thermometer([(2, 4), (2, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4), (8, 4)])
    puzzle.add_thermometer([(0, 4), (0, 3), (1, 3), (1, 4)])
    puzzle.add_thermometer([(1, 1), (1, 2), (2, 2), (3, 2)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(7, 1), (7, 2), (7, 3)])
    puzzle.add_thermometer([(6, 2), (5, 2), (5, 3)])
    puzzle.add_thermometer([(1, 7), (1, 8), (2, 8)])

    return puzzle
