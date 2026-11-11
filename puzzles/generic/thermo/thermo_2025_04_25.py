"""PuzzleMadness Thermometer Sudoku — 2025-04-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (5, 5)])
    puzzle.add_thermometer([(4, 0), (5, 0), (6, 0), (6, 1), (7, 1), (8, 1)])
    puzzle.add_thermometer([(3, 5), (2, 5), (1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7), (5, 7), (4, 7)])
    puzzle.add_thermometer([(7, 4), (7, 5), (8, 5), (8, 6), (7, 6)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(4, 3), (4, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(8, 7), (7, 7), (7, 8), (8, 8)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 3)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(5, 3), (6, 3), (6, 4)])

    return puzzle
