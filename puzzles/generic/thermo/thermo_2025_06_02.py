"""PuzzleMadness Thermometer Sudoku — 2025-06-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 5), (0, 4), (1, 4), (2, 4), (2, 3), (3, 3)])
    puzzle.add_thermometer([(5, 1), (5, 2), (5, 3), (6, 3), (6, 4), (7, 4)])
    puzzle.add_thermometer([(4, 3), (4, 4), (4, 5), (5, 5), (5, 6), (6, 6)])
    puzzle.add_thermometer([(2, 0), (2, 1), (3, 1), (3, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (5, 7)])
    puzzle.add_thermometer([(7, 1), (6, 1), (6, 2), (7, 2), (8, 2)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8), (7, 7), (7, 6)])
    puzzle.add_thermometer([(1, 0), (1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(1, 7), (2, 7), (2, 8)])
    puzzle.add_thermometer([(8, 4), (8, 5), (8, 6)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(6, 7), (6, 8), (5, 8)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 5)])

    return puzzle
