"""PuzzleMadness Thermometer Sudoku — 2025-01-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 4), (1, 4), (1, 3), (0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7), (1, 6), (1, 5), (2, 5)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1)])
    puzzle.add_thermometer([(3, 0), (3, 1), (4, 1), (4, 0), (5, 0)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 2), (8, 1), (7, 1)])
    puzzle.add_thermometer([(5, 6), (5, 7), (5, 8), (6, 8), (6, 7)])
    puzzle.add_thermometer([(4, 2), (5, 2), (5, 3), (4, 3)])
    puzzle.add_thermometer([(6, 4), (7, 4), (7, 5), (7, 6)])
    puzzle.add_thermometer([(4, 5), (5, 5), (5, 4)])
    puzzle.add_thermometer([(3, 6), (4, 6), (4, 7)])
    puzzle.add_thermometer([(6, 2), (6, 1), (5, 1)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6)])

    return puzzle
