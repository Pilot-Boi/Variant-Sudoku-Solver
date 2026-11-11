"""PuzzleMadness Thermometer Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(0, 0), (0, 1), (1, 1), (1, 2), (0, 2)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(7, 4), (7, 5), (6, 5), (5, 5), (5, 6)])
    puzzle.add_thermometer([(2, 7), (3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6), (2, 5)])
    puzzle.add_thermometer([(1, 5), (1, 4), (0, 4), (0, 3)])
    puzzle.add_thermometer([(5, 1), (4, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(6, 6), (6, 7), (5, 7), (4, 7)])
    puzzle.add_thermometer([(4, 2), (5, 2), (5, 3)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4)])
    puzzle.add_thermometer([(2, 1), (2, 2), (2, 3)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0)])
    puzzle.add_thermometer([(6, 2), (6, 3), (6, 4)])

    return puzzle
