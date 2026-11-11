"""PuzzleMadness Thermometer Sudoku — 2025-04-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 9, 5, 2, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_thermometer([(6, 4), (6, 5), (6, 6), (5, 6), (4, 6)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 2), (1, 2), (2, 2)])
    puzzle.add_thermometer([(0, 6), (0, 7), (0, 8), (1, 8)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2), (4, 2)])
    puzzle.add_thermometer([(7, 6), (7, 7), (6, 7), (5, 7)])
    puzzle.add_thermometer([(7, 2), (6, 2), (6, 3), (5, 3)])
    puzzle.add_thermometer([(4, 3), (4, 4), (3, 4), (3, 3)])
    puzzle.add_thermometer([(5, 0), (5, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7), (1, 6)])
    puzzle.add_thermometer([(1, 5), (2, 5), (3, 5)])
    puzzle.add_thermometer([(7, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(1, 0), (1, 1), (0, 1)])
    puzzle.add_thermometer([(2, 4), (1, 4), (0, 4)])

    return puzzle
