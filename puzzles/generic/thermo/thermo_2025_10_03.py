"""PuzzleMadness Thermometer Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 4), (1, 4), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_thermometer([(4, 3), (4, 2), (5, 2), (5, 3), (5, 4), (4, 4)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)])
    puzzle.add_thermometer([(7, 5), (7, 6), (6, 6), (5, 6), (4, 6)])
    puzzle.add_thermometer([(5, 7), (4, 7), (4, 8), (3, 8), (2, 8)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7), (0, 7), (0, 6)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7), (6, 7)])
    puzzle.add_thermometer([(6, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(8, 2), (8, 3), (8, 4), (7, 4)])
    puzzle.add_thermometer([(2, 2), (3, 2), (3, 3)])
    puzzle.add_thermometer([(1, 1), (2, 1), (3, 1)])
    puzzle.add_thermometer([(6, 3), (6, 4), (6, 5)])
    puzzle.add_thermometer([(3, 4), (3, 5), (4, 5)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7)])

    return puzzle
