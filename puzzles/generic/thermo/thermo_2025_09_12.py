"""PuzzleMadness Thermometer Sudoku — 2025-09-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)])
    puzzle.add_thermometer([(4, 2), (3, 2), (2, 2), (2, 3), (2, 4), (3, 4)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0), (4, 0), (4, 1), (3, 1)])
    puzzle.add_thermometer([(6, 0), (6, 1), (5, 1), (5, 2), (6, 2), (7, 2)])
    puzzle.add_thermometer([(7, 7), (6, 7), (6, 6), (7, 6), (7, 5), (6, 5)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(5, 3), (5, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(5, 8), (5, 7), (4, 7), (4, 6)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3), (8, 3)])
    puzzle.add_thermometer([(1, 4), (1, 3), (1, 2), (1, 1)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(3, 6), (3, 7), (3, 8)])
    puzzle.add_thermometer([(0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8)])

    return puzzle
