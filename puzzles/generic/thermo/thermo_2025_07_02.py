"""PuzzleMadness Thermometer Sudoku — 2025-07-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 9, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 0), (7, 0), (6, 0), (6, 1), (6, 2), (7, 2)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (2, 1), (2, 0)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4), (6, 4), (5, 4)])
    puzzle.add_thermometer([(1, 5), (1, 4), (2, 4), (2, 3), (3, 3)])
    puzzle.add_thermometer([(2, 8), (2, 7), (3, 7), (3, 8)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 5), (2, 5)])
    puzzle.add_thermometer([(3, 4), (4, 4), (4, 3), (5, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7), (5, 7)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(7, 7), (7, 6), (6, 6)])
    puzzle.add_thermometer([(2, 2), (3, 2), (4, 2)])
    puzzle.add_thermometer([(5, 6), (5, 5), (4, 5)])

    return puzzle
