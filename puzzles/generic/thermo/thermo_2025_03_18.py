"""PuzzleMadness Thermometer Sudoku — 2025-03-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)])
    puzzle.add_thermometer([(8, 8), (8, 7), (8, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4), (6, 4), (5, 4)])
    puzzle.add_thermometer([(2, 4), (2, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(1, 0), (1, 1), (2, 1), (2, 0)])
    puzzle.add_thermometer([(1, 2), (1, 3), (2, 3), (2, 2)])
    puzzle.add_thermometer([(6, 8), (5, 8), (5, 7), (6, 7)])
    puzzle.add_thermometer([(0, 7), (0, 6), (1, 6), (2, 6)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 7), (3, 8)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(7, 1), (6, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(5, 3), (6, 3), (7, 3)])

    return puzzle
