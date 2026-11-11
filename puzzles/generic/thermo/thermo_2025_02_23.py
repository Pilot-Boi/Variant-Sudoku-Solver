"""PuzzleMadness Thermometer Sudoku — 2025-02-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 7, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 3), (6, 3), (7, 3), (7, 4), (7, 5), (7, 6)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0), (3, 0), (2, 0)])
    puzzle.add_thermometer([(4, 5), (4, 4), (3, 4), (3, 3), (4, 3)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 4), (0, 4)])
    puzzle.add_thermometer([(7, 2), (7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(3, 2), (4, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7), (5, 7)])
    puzzle.add_thermometer([(3, 6), (3, 7), (4, 7), (4, 6)])
    puzzle.add_thermometer([(1, 0), (1, 1), (2, 1), (3, 1)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6)])
    puzzle.add_thermometer([(0, 8), (0, 7), (1, 7)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(1, 5), (2, 5), (3, 5)])

    return puzzle
