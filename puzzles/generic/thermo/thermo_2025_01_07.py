"""PuzzleMadness Thermometer Sudoku — 2025-01-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 1, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (8, 6)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)])
    puzzle.add_thermometer([(7, 2), (6, 2), (6, 3), (7, 3)])
    puzzle.add_thermometer([(8, 3), (8, 4), (8, 5), (7, 5)])
    puzzle.add_thermometer([(5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_thermometer([(1, 7), (1, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(2, 2), (1, 2), (0, 2), (0, 3)])
    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1), (7, 1)])
    puzzle.add_thermometer([(1, 0), (2, 0), (2, 1), (1, 1)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 7), (3, 8)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])

    return puzzle
