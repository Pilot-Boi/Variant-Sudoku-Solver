"""PuzzleMadness Thermometer Sudoku — 2025-10-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 8), (3, 7), (2, 7), (2, 6), (3, 6), (3, 5)])
    puzzle.add_thermometer([(5, 4), (5, 5), (6, 5), (6, 6), (7, 6), (7, 5)])
    puzzle.add_thermometer([(2, 2), (2, 3), (2, 4), (1, 4), (0, 4), (0, 3)])
    puzzle.add_thermometer([(6, 2), (6, 1), (7, 1), (7, 2), (8, 2)])
    puzzle.add_thermometer([(7, 7), (8, 7), (8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(4, 8), (5, 8), (5, 7), (6, 7), (6, 8)])
    puzzle.add_thermometer([(4, 1), (4, 2), (4, 3), (4, 4)])
    puzzle.add_thermometer([(7, 4), (7, 3), (6, 3), (6, 4)])
    puzzle.add_thermometer([(6, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_thermometer([(1, 5), (1, 6), (1, 7)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4)])
    puzzle.add_thermometer([(0, 8), (1, 8), (2, 8)])
    puzzle.add_thermometer([(4, 5), (4, 6), (4, 7)])

    return puzzle
