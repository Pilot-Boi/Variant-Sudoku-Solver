"""PuzzleMadness Thermometer Sudoku — 2025-02-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 2, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 4), (0, 4), (0, 5), (1, 5), (1, 6), (2, 6)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3), (7, 4), (8, 4), (8, 5)])
    puzzle.add_thermometer([(4, 5), (5, 5), (5, 4), (5, 3), (5, 2)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8), (0, 8), (0, 7)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 2), (2, 3), (3, 3)])
    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0), (4, 1), (3, 1)])
    puzzle.add_thermometer([(7, 1), (6, 1), (6, 0), (7, 0)])
    puzzle.add_thermometer([(3, 6), (3, 5), (3, 4), (4, 4)])
    puzzle.add_thermometer([(4, 3), (4, 2), (3, 2)])
    puzzle.add_thermometer([(6, 6), (6, 5), (6, 4)])
    puzzle.add_thermometer([(2, 7), (3, 7), (4, 7)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])

    return puzzle
