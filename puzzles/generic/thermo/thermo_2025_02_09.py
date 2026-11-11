"""PuzzleMadness Thermometer Sudoku — 2025-02-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 5, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(3, 3), (3, 2), (3, 1), (2, 1), (1, 1), (0, 1)])
    puzzle.add_thermometer([(6, 5), (5, 5), (5, 4), (5, 3), (4, 3)])
    puzzle.add_thermometer([(5, 1), (6, 1), (7, 1), (7, 2), (6, 2)])
    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4), (7, 5), (8, 5)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (0, 3)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (7, 7)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6), (1, 6)])
    puzzle.add_thermometer([(4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(8, 0), (8, 1), (8, 2)])
    puzzle.add_thermometer([(4, 5), (4, 4), (3, 4)])
    puzzle.add_thermometer([(5, 2), (4, 2), (4, 1)])
    puzzle.add_thermometer([(0, 2), (1, 2), (2, 2)])

    return puzzle
