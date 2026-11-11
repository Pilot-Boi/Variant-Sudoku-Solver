"""PuzzleMadness Thermometer Sudoku — 2025-01-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 8), (3, 7), (2, 7), (2, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(1, 0), (1, 1), (1, 2), (2, 2), (2, 3), (2, 4)])
    puzzle.add_thermometer([(4, 3), (5, 3), (5, 2), (6, 2), (6, 1)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7), (7, 7)])
    puzzle.add_thermometer([(5, 1), (4, 1), (4, 0), (3, 0)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 5), (0, 5)])
    puzzle.add_thermometer([(7, 2), (7, 3), (7, 4), (7, 5)])
    puzzle.add_thermometer([(7, 8), (6, 8), (5, 8), (5, 7)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(6, 4), (5, 4), (4, 4)])
    puzzle.add_thermometer([(4, 8), (4, 7), (4, 6)])

    return puzzle
