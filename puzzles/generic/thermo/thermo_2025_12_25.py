"""PuzzleMadness Thermometer Sudoku — 2025-12-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (6, 6), (6, 7), (5, 7), (5, 8), (6, 8)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6), (1, 6), (1, 7), (0, 7)])
    puzzle.add_thermometer([(7, 0), (6, 0), (6, 1), (6, 2), (5, 2)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 2), (2, 3), (3, 3)])
    puzzle.add_thermometer([(4, 7), (4, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4), (4, 5)])
    puzzle.add_thermometer([(5, 3), (6, 3), (7, 3), (8, 3)])
    puzzle.add_thermometer([(8, 5), (7, 5), (7, 6), (8, 6)])
    puzzle.add_thermometer([(1, 3), (1, 4), (1, 5), (0, 5)])
    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4)])

    return puzzle
