"""PuzzleMadness Thermometer Sudoku — 2025-12-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 5), (1, 4), (1, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_thermometer([(3, 2), (2, 2), (1, 2), (1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(7, 4), (7, 5), (6, 5), (5, 5), (5, 4), (6, 4)])
    puzzle.add_thermometer([(4, 0), (4, 1), (5, 1), (5, 2), (6, 2)])
    puzzle.add_thermometer([(4, 7), (5, 7), (6, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(7, 3), (8, 3), (8, 4), (8, 5), (8, 6)])
    puzzle.add_thermometer([(2, 6), (3, 6), (3, 7), (2, 7), (1, 7)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(0, 8), (1, 8), (2, 8)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8)])
    puzzle.add_thermometer([(3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(4, 4), (4, 5), (4, 6)])
    puzzle.add_thermometer([(5, 3), (4, 3), (4, 2)])

    return puzzle
