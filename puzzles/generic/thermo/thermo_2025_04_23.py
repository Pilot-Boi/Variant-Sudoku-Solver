"""PuzzleMadness Thermometer Sudoku — 2025-04-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 2, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8), (3, 8), (3, 7), (2, 7)])
    puzzle.add_thermometer([(1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0)])
    puzzle.add_thermometer([(6, 0), (6, 1), (7, 1), (7, 2), (6, 2)])
    puzzle.add_thermometer([(7, 3), (7, 4), (6, 4), (6, 3), (5, 3)])
    puzzle.add_thermometer([(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)])
    puzzle.add_thermometer([(7, 7), (8, 7), (8, 8), (7, 8)])
    puzzle.add_thermometer([(1, 6), (2, 6), (3, 6), (4, 6)])
    puzzle.add_thermometer([(8, 6), (8, 5), (7, 5), (6, 5)])
    puzzle.add_thermometer([(4, 1), (4, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(3, 4), (3, 5), (4, 5), (4, 4)])
    puzzle.add_thermometer([(4, 7), (5, 7), (6, 7)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2)])
    puzzle.add_thermometer([(5, 2), (4, 2), (3, 2)])

    return puzzle
