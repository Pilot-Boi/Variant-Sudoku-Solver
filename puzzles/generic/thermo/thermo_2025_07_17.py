"""PuzzleMadness Thermometer Sudoku — 2025-07-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 2), (3, 2), (3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_thermometer([(6, 3), (7, 3), (7, 2), (8, 2), (8, 1), (7, 1)])
    puzzle.add_thermometer([(5, 8), (5, 7), (4, 7), (3, 7), (3, 6), (2, 6)])
    puzzle.add_thermometer([(4, 6), (4, 5), (5, 5), (6, 5), (6, 4)])
    puzzle.add_thermometer([(7, 6), (6, 6), (6, 7), (7, 7), (8, 7)])
    puzzle.add_thermometer([(0, 1), (1, 1), (2, 1), (2, 0), (1, 0)])
    puzzle.add_thermometer([(8, 5), (8, 4), (7, 4), (7, 5)])
    puzzle.add_thermometer([(1, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(3, 5), (3, 4), (3, 3), (2, 3)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 4), (0, 5)])
    puzzle.add_thermometer([(6, 1), (5, 1), (4, 1)])
    puzzle.add_thermometer([(5, 4), (4, 4), (4, 3)])

    return puzzle
