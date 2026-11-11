"""PuzzleMadness Thermometer Sudoku — 2025-12-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 3), (3, 2), (3, 1), (2, 1), (2, 0), (3, 0)])
    puzzle.add_thermometer([(6, 4), (7, 4), (8, 4), (8, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(2, 5), (1, 5), (0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(5, 0), (6, 0), (6, 1), (7, 1), (8, 1)])
    puzzle.add_thermometer([(1, 8), (1, 7), (2, 7), (3, 7), (3, 8)])
    puzzle.add_thermometer([(5, 3), (4, 3), (4, 2), (5, 2), (6, 2)])
    puzzle.add_thermometer([(7, 8), (7, 7), (7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(6, 6), (6, 7), (5, 7), (4, 7)])
    puzzle.add_thermometer([(2, 4), (3, 4), (4, 4), (5, 4)])
    puzzle.add_thermometer([(5, 5), (4, 5), (3, 5)])
    puzzle.add_thermometer([(1, 1), (1, 0), (0, 0)])
    puzzle.add_thermometer([(1, 4), (1, 3), (1, 2)])
    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6)])
    puzzle.add_thermometer([(4, 8), (5, 8), (6, 8)])

    return puzzle
