"""PuzzleMadness Thermometer Sudoku — 2025-02-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 8, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 2, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 7), (6, 7), (5, 7), (4, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(0, 1), (0, 2), (1, 2), (1, 1), (2, 1)])
    puzzle.add_thermometer([(3, 3), (4, 3), (5, 3), (6, 3), (6, 2)])
    puzzle.add_thermometer([(2, 5), (2, 4), (1, 4), (0, 4), (0, 3)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 5), (7, 4), (6, 4)])
    puzzle.add_thermometer([(4, 0), (4, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(2, 7), (2, 6), (1, 6), (1, 7)])
    puzzle.add_thermometer([(5, 6), (5, 5), (4, 5), (4, 4)])
    puzzle.add_thermometer([(6, 1), (6, 0), (7, 0)])
    puzzle.add_thermometer([(1, 0), (2, 0), (3, 0)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8)])

    return puzzle
