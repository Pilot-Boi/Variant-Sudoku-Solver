"""PuzzleMadness Thermometer Sudoku — 2025-12-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 3), (1, 3), (0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_thermometer([(6, 1), (6, 2), (6, 3), (5, 3), (4, 3), (4, 4)])
    puzzle.add_thermometer([(6, 6), (7, 6), (8, 6), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1)])
    puzzle.add_thermometer([(2, 7), (3, 7), (4, 7), (4, 6), (3, 6)])
    puzzle.add_thermometer([(4, 2), (3, 2), (3, 1), (4, 1), (5, 1)])
    puzzle.add_thermometer([(7, 2), (7, 1), (8, 1), (8, 2)])
    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4), (7, 3)])
    puzzle.add_thermometer([(0, 8), (1, 8), (2, 8), (3, 8)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 5), (2, 5)])
    puzzle.add_thermometer([(4, 5), (5, 5), (5, 6)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])
    puzzle.add_thermometer([(5, 7), (5, 8), (6, 8)])
    puzzle.add_thermometer([(7, 5), (8, 5), (8, 4)])

    return puzzle
