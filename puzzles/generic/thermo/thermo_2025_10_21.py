"""PuzzleMadness Thermometer Sudoku — 2025-10-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 3), (4, 3), (4, 4), (4, 5), (3, 5), (3, 6)])
    puzzle.add_thermometer([(7, 5), (6, 5), (6, 4), (6, 3), (7, 3), (7, 4)])
    puzzle.add_thermometer([(4, 7), (3, 7), (3, 8), (2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(5, 2), (5, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(6, 8), (7, 8), (7, 7), (7, 6), (6, 6)])
    puzzle.add_thermometer([(1, 2), (1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(3, 0), (2, 0), (2, 1), (3, 1)])
    puzzle.add_thermometer([(0, 3), (1, 3), (1, 4), (0, 4)])
    puzzle.add_thermometer([(2, 4), (3, 4), (3, 3), (2, 3)])
    puzzle.add_thermometer([(4, 6), (5, 6), (5, 7)])
    puzzle.add_thermometer([(8, 4), (8, 3), (8, 2)])

    return puzzle
