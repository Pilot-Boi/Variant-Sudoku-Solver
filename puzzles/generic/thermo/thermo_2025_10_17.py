"""PuzzleMadness Thermometer Sudoku — 2025-10-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 4, 0, 7, 0, 0, 0],
        [5, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 5), (5, 6), (6, 6), (6, 5), (6, 4), (5, 4)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(3, 3), (2, 3), (2, 4), (2, 5), (1, 5), (0, 5)])
    puzzle.add_thermometer([(6, 8), (5, 8), (5, 7), (6, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(4, 2), (4, 1), (4, 0), (3, 0), (2, 0)])
    puzzle.add_thermometer([(6, 2), (6, 3), (5, 3), (5, 2), (5, 1)])
    puzzle.add_thermometer([(1, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(7, 4), (7, 5), (7, 6)])
    puzzle.add_thermometer([(2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(3, 6), (3, 5), (3, 4)])
    puzzle.add_thermometer([(0, 1), (0, 2), (0, 3)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3)])
    puzzle.add_thermometer([(8, 7), (8, 6), (8, 5)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6)])

    return puzzle
