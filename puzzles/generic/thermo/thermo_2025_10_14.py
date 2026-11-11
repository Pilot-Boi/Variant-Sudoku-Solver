"""PuzzleMadness Thermometer Sudoku — 2025-10-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 1, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 3), (4, 3), (4, 4), (3, 4), (3, 5), (4, 5)])
    puzzle.add_thermometer([(4, 1), (4, 2), (3, 2), (3, 1), (3, 0), (4, 0)])
    puzzle.add_thermometer([(8, 5), (7, 5), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 4), (2, 3), (2, 2)])
    puzzle.add_thermometer([(3, 6), (3, 7), (2, 7), (1, 7)])
    puzzle.add_thermometer([(7, 7), (7, 8), (6, 8), (5, 8)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1)])
    puzzle.add_thermometer([(0, 7), (0, 6), (1, 6), (2, 6)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 4), (7, 4)])
    puzzle.add_thermometer([(1, 2), (1, 3), (0, 3), (0, 2)])
    puzzle.add_thermometer([(6, 4), (6, 5), (6, 6)])
    puzzle.add_thermometer([(6, 2), (7, 2), (8, 2)])
    puzzle.add_thermometer([(2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1)])

    return puzzle
