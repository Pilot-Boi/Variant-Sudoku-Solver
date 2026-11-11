"""PuzzleMadness Thermometer Sudoku — 2025-06-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 2, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 0), (3, 0), (3, 1), (2, 1), (2, 2), (3, 2)])
    puzzle.add_thermometer([(5, 4), (5, 5), (5, 6), (6, 6), (7, 6)])
    puzzle.add_thermometer([(3, 6), (3, 5), (2, 5), (2, 4)])
    puzzle.add_thermometer([(7, 2), (7, 3), (7, 4), (8, 4)])
    puzzle.add_thermometer([(6, 0), (7, 0), (7, 1), (6, 1)])
    puzzle.add_thermometer([(6, 7), (6, 8), (5, 8), (5, 7)])
    puzzle.add_thermometer([(1, 1), (1, 2), (0, 2), (0, 1)])
    puzzle.add_thermometer([(2, 3), (3, 3), (3, 4)])
    puzzle.add_thermometer([(4, 8), (4, 7), (3, 7)])
    puzzle.add_thermometer([(5, 2), (6, 2), (6, 3)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8)])
    puzzle.add_thermometer([(1, 5), (1, 4), (1, 3)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0)])

    return puzzle
