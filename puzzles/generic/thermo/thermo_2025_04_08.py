"""PuzzleMadness Thermometer Sudoku — 2025-04-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8), (6, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(3, 7), (3, 6), (4, 6), (4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(2, 4), (2, 3), (3, 3), (3, 2), (4, 2), (4, 3)])
    puzzle.add_thermometer([(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(4, 4), (4, 5), (5, 5), (5, 6), (6, 6)])
    puzzle.add_thermometer([(3, 0), (3, 1), (4, 1), (4, 0), (5, 0)])
    puzzle.add_thermometer([(1, 3), (1, 4), (0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(5, 1), (5, 2), (6, 2), (6, 1), (7, 1)])
    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4), (7, 5)])
    puzzle.add_thermometer([(0, 5), (0, 6), (1, 6), (2, 6)])
    puzzle.add_thermometer([(2, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 1)])
    puzzle.add_thermometer([(2, 5), (3, 5), (3, 4)])

    return puzzle
