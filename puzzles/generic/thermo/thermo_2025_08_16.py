"""PuzzleMadness Thermometer Sudoku — 2025-08-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 9, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 5), (0, 5), (0, 4), (1, 4), (2, 4), (3, 4)])
    puzzle.add_thermometer([(5, 5), (5, 4), (5, 3), (5, 2), (5, 1)])
    puzzle.add_thermometer([(3, 7), (4, 7), (4, 6), (3, 6), (2, 6)])
    puzzle.add_thermometer([(0, 1), (1, 1), (2, 1), (2, 0), (1, 0)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(7, 2), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3), (7, 4)])
    puzzle.add_thermometer([(6, 6), (7, 6), (7, 5), (6, 5)])
    puzzle.add_thermometer([(2, 3), (2, 2), (3, 2), (3, 1)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 7)])
    puzzle.add_thermometer([(4, 3), (4, 2), (4, 1)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8)])

    return puzzle
