"""PuzzleMadness Thermometer Sudoku — 2025-04-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 3, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4)])
    puzzle.add_thermometer([(2, 1), (1, 1), (1, 2), (0, 2), (0, 3), (1, 3)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3), (7, 2), (7, 1)])
    puzzle.add_thermometer([(4, 8), (4, 7), (5, 7), (6, 7), (6, 8)])
    puzzle.add_thermometer([(7, 6), (6, 6), (6, 5), (6, 4)])
    puzzle.add_thermometer([(3, 2), (3, 1), (4, 1), (4, 2)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8)])
    puzzle.add_thermometer([(2, 3), (2, 4), (1, 4)])
    puzzle.add_thermometer([(1, 6), (2, 6), (3, 6)])
    puzzle.add_thermometer([(0, 7), (1, 7), (2, 7)])
    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0)])
    puzzle.add_thermometer([(5, 3), (4, 3), (4, 4)])
    puzzle.add_thermometer([(0, 4), (0, 5), (0, 6)])

    return puzzle
