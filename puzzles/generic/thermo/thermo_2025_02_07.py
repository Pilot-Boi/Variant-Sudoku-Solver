"""PuzzleMadness Thermometer Sudoku — 2025-02-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6), (1, 6), (0, 6), (0, 7)])
    puzzle.add_thermometer([(8, 7), (8, 6), (8, 5), (7, 5), (7, 6), (6, 6)])
    puzzle.add_thermometer([(7, 1), (7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_thermometer([(3, 4), (3, 3), (4, 3), (5, 3), (6, 3)])
    puzzle.add_thermometer([(2, 1), (2, 2), (3, 2), (3, 1)])
    puzzle.add_thermometer([(2, 5), (2, 4), (1, 4), (1, 5)])
    puzzle.add_thermometer([(5, 0), (5, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(1, 7), (2, 7), (3, 7)])
    puzzle.add_thermometer([(1, 2), (1, 3), (2, 3)])
    puzzle.add_thermometer([(5, 5), (5, 6), (5, 7)])
    puzzle.add_thermometer([(8, 3), (7, 3), (7, 4)])

    return puzzle
