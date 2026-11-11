"""PuzzleMadness Thermometer Sudoku — 2025-04-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 5), (1, 5), (1, 4), (1, 3), (0, 3), (0, 4)])
    puzzle.add_thermometer([(7, 6), (6, 6), (6, 7), (5, 7), (4, 7), (4, 6)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0), (4, 1), (3, 1), (3, 0)])
    puzzle.add_thermometer([(5, 2), (4, 2), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(3, 6), (3, 7), (2, 7), (2, 6), (2, 5)])
    puzzle.add_thermometer([(6, 1), (7, 1), (8, 1), (8, 2), (7, 2)])
    puzzle.add_thermometer([(7, 4), (6, 4), (6, 5), (5, 5)])
    puzzle.add_thermometer([(8, 7), (7, 7), (7, 8), (8, 8)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(0, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(4, 3), (3, 3), (3, 4)])

    return puzzle
