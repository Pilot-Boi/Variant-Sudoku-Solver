"""PuzzleMadness Thermometer Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [4, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 3), (2, 2), (3, 2), (3, 1), (3, 0)])
    puzzle.add_thermometer([(6, 8), (6, 7), (5, 7), (4, 7), (4, 8)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 2), (0, 3), (1, 3)])
    puzzle.add_thermometer([(1, 5), (1, 6), (1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(7, 6), (7, 5), (7, 4), (7, 3), (7, 2)])
    puzzle.add_thermometer([(3, 5), (3, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(4, 4), (4, 5), (5, 5), (6, 5)])
    puzzle.add_thermometer([(4, 2), (4, 3), (5, 3), (5, 2)])
    puzzle.add_thermometer([(0, 4), (1, 4), (2, 4), (3, 4)])
    puzzle.add_thermometer([(8, 4), (8, 3), (8, 2), (8, 1)])
    puzzle.add_thermometer([(5, 0), (5, 1), (6, 1)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8)])
    puzzle.add_thermometer([(6, 2), (6, 3), (6, 4)])
    puzzle.add_thermometer([(2, 0), (1, 0), (0, 0)])

    return puzzle
