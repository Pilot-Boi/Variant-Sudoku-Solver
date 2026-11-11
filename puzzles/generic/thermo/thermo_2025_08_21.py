"""PuzzleMadness Thermometer Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 4, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 3), (1, 3), (1, 4), (1, 5), (0, 5), (0, 4)])
    puzzle.add_thermometer([(2, 3), (2, 2), (1, 2), (1, 1), (2, 1)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_thermometer([(6, 6), (6, 5), (6, 4), (6, 3), (6, 2)])
    puzzle.add_thermometer([(4, 8), (5, 8), (6, 8), (6, 7), (7, 7)])
    puzzle.add_thermometer([(3, 5), (4, 5), (4, 4), (5, 4)])
    puzzle.add_thermometer([(7, 4), (8, 4), (8, 3), (7, 3)])
    puzzle.add_thermometer([(1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_thermometer([(6, 1), (5, 1), (5, 2), (4, 2)])
    puzzle.add_thermometer([(0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(3, 4), (2, 4), (2, 5)])
    puzzle.add_thermometer([(8, 0), (7, 0), (6, 0)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8)])
    puzzle.add_thermometer([(2, 7), (3, 7), (4, 7)])
    puzzle.add_thermometer([(5, 3), (4, 3), (3, 3)])

    return puzzle
