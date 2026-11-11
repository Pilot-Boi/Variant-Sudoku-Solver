"""PuzzleMadness Thermometer Sudoku — 2025-09-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 8, 0, 0, 0, 0, 0, 4, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 1)])
    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(4, 3), (4, 2), (4, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(4, 6), (5, 6), (6, 6), (7, 6), (7, 5)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(6, 2), (6, 1), (6, 0), (7, 0)])
    puzzle.add_thermometer([(3, 5), (3, 4), (2, 4), (1, 4)])
    puzzle.add_thermometer([(2, 0), (1, 0), (1, 1), (2, 1)])
    puzzle.add_thermometer([(3, 1), (3, 0), (4, 0)])
    puzzle.add_thermometer([(2, 2), (3, 2), (3, 3)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(6, 5), (5, 5), (4, 5)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(1, 7), (1, 6), (0, 6)])

    return puzzle
