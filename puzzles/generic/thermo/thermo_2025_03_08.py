"""PuzzleMadness Thermometer Sudoku — 2025-03-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 4, 0, 0, 2, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 4), (1, 3), (2, 3), (2, 4), (2, 5), (2, 6)])
    puzzle.add_thermometer([(6, 4), (5, 4), (5, 3), (4, 3), (4, 4)])
    puzzle.add_thermometer([(7, 5), (6, 5), (6, 6), (5, 6), (5, 5)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 2), (6, 2), (6, 3)])
    puzzle.add_thermometer([(0, 1), (0, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0), (5, 1), (4, 1)])
    puzzle.add_thermometer([(2, 8), (2, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(4, 7), (4, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(3, 3), (3, 4), (3, 5)])
    puzzle.add_thermometer([(5, 8), (5, 7), (6, 7)])
    puzzle.add_thermometer([(2, 0), (2, 1), (3, 1)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0)])

    return puzzle
