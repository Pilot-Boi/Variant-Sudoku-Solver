"""PuzzleMadness Thermometer Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 2, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 6), (7, 6), (7, 7), (6, 7), (5, 7)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6), (1, 5), (1, 4)])
    puzzle.add_thermometer([(4, 7), (4, 6), (3, 6), (3, 5), (4, 5)])
    puzzle.add_thermometer([(5, 3), (5, 4), (6, 4), (7, 4), (7, 3)])
    puzzle.add_thermometer([(7, 5), (6, 5), (5, 5), (5, 6)])
    puzzle.add_thermometer([(1, 2), (2, 2), (2, 1), (2, 0)])
    puzzle.add_thermometer([(7, 1), (7, 2), (6, 2), (5, 2)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])
    puzzle.add_thermometer([(3, 4), (2, 4), (2, 3)])
    puzzle.add_thermometer([(8, 4), (8, 3), (8, 2)])
    puzzle.add_thermometer([(2, 5), (2, 6), (2, 7)])

    return puzzle
