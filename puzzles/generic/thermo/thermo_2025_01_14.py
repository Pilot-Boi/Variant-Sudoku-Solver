"""PuzzleMadness Thermometer Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 0, 0, 8, 0, 0, 0],
        [0, 4, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(5, 7), (5, 6), (4, 6), (4, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(6, 3), (6, 4), (7, 4), (7, 3), (8, 3), (8, 2)])
    puzzle.add_thermometer([(2, 2), (2, 3), (2, 4), (1, 4), (1, 3), (1, 2)])
    puzzle.add_thermometer([(4, 4), (4, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(8, 0), (8, 1), (7, 1), (7, 2)])
    puzzle.add_thermometer([(1, 6), (1, 7), (0, 7), (0, 6)])
    puzzle.add_thermometer([(6, 2), (5, 2), (5, 3), (5, 4)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_thermometer([(3, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(2, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(1, 1), (1, 0), (2, 0)])
    puzzle.add_thermometer([(7, 0), (6, 0), (5, 0)])
    puzzle.add_thermometer([(0, 5), (1, 5), (2, 5)])

    return puzzle
