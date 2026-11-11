"""PuzzleMadness Thermometer Sudoku — 2025-08-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 2), (4, 3), (3, 3), (3, 4), (2, 4), (1, 4)])
    puzzle.add_thermometer([(5, 4), (6, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_thermometer([(3, 0), (3, 1), (4, 1), (4, 0), (5, 0)])
    puzzle.add_thermometer([(2, 3), (2, 2), (1, 2), (0, 2), (0, 1)])
    puzzle.add_thermometer([(3, 7), (2, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3), (8, 2)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (8, 6)])
    puzzle.add_thermometer([(1, 6), (1, 5), (2, 5), (2, 6)])
    puzzle.add_thermometer([(5, 8), (4, 8), (4, 7), (5, 7)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1), (7, 1)])
    puzzle.add_thermometer([(1, 1), (1, 0), (0, 0)])
    puzzle.add_thermometer([(6, 2), (5, 2), (5, 3)])
    puzzle.add_thermometer([(0, 3), (0, 4), (0, 5)])

    return puzzle
