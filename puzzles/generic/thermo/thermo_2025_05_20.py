"""PuzzleMadness Thermometer Sudoku — 2025-05-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 8],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 0), (6, 0), (6, 1), (6, 2), (6, 3), (7, 3)])
    puzzle.add_thermometer([(4, 5), (4, 6), (5, 6), (5, 7), (6, 7), (6, 8)])
    puzzle.add_thermometer([(0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (2, 6)])
    puzzle.add_thermometer([(8, 5), (7, 5), (6, 5), (5, 5), (5, 4)])
    puzzle.add_thermometer([(5, 2), (5, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(2, 3), (2, 2), (2, 1), (1, 1), (1, 0)])
    puzzle.add_thermometer([(1, 7), (1, 6), (0, 6), (0, 5)])
    puzzle.add_thermometer([(4, 8), (3, 8), (2, 8)])
    puzzle.add_thermometer([(6, 4), (7, 4), (8, 4)])
    puzzle.add_thermometer([(4, 3), (3, 3), (3, 2)])
    puzzle.add_thermometer([(7, 7), (7, 6), (6, 6)])

    return puzzle
