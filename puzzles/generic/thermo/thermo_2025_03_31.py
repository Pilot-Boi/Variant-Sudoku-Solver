"""PuzzleMadness Thermometer Sudoku — 2025-03-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 1, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 0), (2, 1), (1, 1), (0, 1), (0, 2), (0, 3)])
    puzzle.add_thermometer([(1, 4), (1, 5), (2, 5), (2, 4), (2, 3), (2, 2)])
    puzzle.add_thermometer([(3, 8), (3, 7), (4, 7), (4, 8), (5, 8)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_thermometer([(5, 2), (6, 2), (6, 3), (6, 4), (7, 4)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 7), (1, 8)])
    puzzle.add_thermometer([(8, 6), (8, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0)])
    puzzle.add_thermometer([(3, 4), (3, 5), (3, 6)])
    puzzle.add_thermometer([(8, 3), (8, 4), (8, 5)])
    puzzle.add_thermometer([(4, 3), (4, 2), (3, 2)])
    puzzle.add_thermometer([(7, 5), (6, 5), (5, 5)])

    return puzzle
