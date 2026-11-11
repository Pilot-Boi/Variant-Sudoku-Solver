"""PuzzleMadness Thermometer Sudoku — 2025-03-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 7, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 3), (7, 2), (7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(5, 8), (5, 7), (5, 6), (5, 5), (4, 5)])
    puzzle.add_thermometer([(2, 5), (3, 5), (3, 4), (3, 3), (4, 3)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 6), (1, 5), (1, 4)])
    puzzle.add_thermometer([(4, 0), (4, 1), (3, 1), (2, 1), (2, 2)])
    puzzle.add_thermometer([(6, 0), (6, 1), (6, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(6, 4), (6, 5), (7, 5), (7, 6)])
    puzzle.add_thermometer([(4, 8), (4, 7), (3, 7), (3, 8)])
    puzzle.add_thermometer([(0, 2), (0, 3), (0, 4)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8)])
    puzzle.add_thermometer([(1, 1), (1, 2), (1, 3)])

    return puzzle
