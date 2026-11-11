"""PuzzleMadness Thermometer Sudoku — 2025-07-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 1), (6, 1), (7, 1), (8, 1), (8, 0), (7, 0)])
    puzzle.add_thermometer([(2, 7), (2, 8), (1, 8), (1, 7), (1, 6)])
    puzzle.add_thermometer([(5, 7), (6, 7), (6, 6), (6, 5), (6, 4)])
    puzzle.add_thermometer([(3, 8), (4, 8), (4, 7), (3, 7)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(1, 5), (1, 4), (0, 4), (0, 5)])
    puzzle.add_thermometer([(2, 0), (3, 0), (3, 1), (2, 1)])
    puzzle.add_thermometer([(3, 6), (3, 5), (2, 5), (2, 4)])
    puzzle.add_thermometer([(8, 6), (8, 7), (8, 8)])
    puzzle.add_thermometer([(6, 3), (6, 2), (5, 2)])
    puzzle.add_thermometer([(2, 2), (1, 2), (1, 3)])
    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8)])
    puzzle.add_thermometer([(4, 0), (5, 0), (6, 0)])

    return puzzle
