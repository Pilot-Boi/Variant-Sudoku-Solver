"""PuzzleMadness Thermometer Sudoku — 2025-04-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 2, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 6), (4, 5), (4, 4), (4, 3), (5, 3), (5, 4)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 7), (1, 8), (2, 8), (3, 8)])
    puzzle.add_thermometer([(2, 0), (3, 0), (3, 1), (3, 2), (2, 2)])
    puzzle.add_thermometer([(3, 4), (2, 4), (2, 5), (3, 5), (3, 6)])
    puzzle.add_thermometer([(7, 2), (7, 3), (7, 4), (8, 4), (8, 3)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7), (7, 6), (7, 5)])
    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8), (4, 7)])
    puzzle.add_thermometer([(6, 3), (6, 2), (5, 2), (4, 2)])
    puzzle.add_thermometer([(4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_thermometer([(6, 5), (6, 6), (5, 6)])
    puzzle.add_thermometer([(1, 3), (1, 4), (1, 5)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(0, 4), (0, 5), (0, 6)])

    return puzzle
