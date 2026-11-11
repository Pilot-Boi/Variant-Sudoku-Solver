"""PuzzleMadness Thermometer Sudoku — 2025-07-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4), (6, 4), (6, 3), (7, 3)])
    puzzle.add_thermometer([(6, 7), (6, 8), (7, 8), (7, 7), (8, 7)])
    puzzle.add_thermometer([(3, 3), (3, 2), (3, 1), (2, 1), (2, 2)])
    puzzle.add_thermometer([(5, 3), (5, 4), (5, 5), (4, 5), (4, 4)])
    puzzle.add_thermometer([(7, 2), (7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_thermometer([(2, 6), (3, 6), (3, 7), (2, 7)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(0, 2), (0, 3), (1, 3)])
    puzzle.add_thermometer([(5, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(2, 4), (2, 5), (3, 5)])

    return puzzle
