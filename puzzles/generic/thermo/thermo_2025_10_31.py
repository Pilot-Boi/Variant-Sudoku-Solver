"""PuzzleMadness Thermometer Sudoku — 2025-10-31."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-31'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/31'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 8, 0, 0],
        [0, 7, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 7), (3, 6), (4, 6), (4, 5), (4, 4), (5, 4)])
    puzzle.add_thermometer([(1, 6), (1, 5), (1, 4), (2, 4), (2, 5), (3, 5)])
    puzzle.add_thermometer([(6, 6), (6, 7), (5, 7), (4, 7), (4, 8)])
    puzzle.add_thermometer([(4, 0), (4, 1), (3, 1), (3, 0), (2, 0)])
    puzzle.add_thermometer([(5, 5), (6, 5), (7, 5), (7, 6), (8, 6)])
    puzzle.add_thermometer([(7, 1), (7, 2), (8, 2), (8, 1)])
    puzzle.add_thermometer([(8, 0), (7, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(5, 3), (6, 3), (6, 2), (5, 2)])
    puzzle.add_thermometer([(0, 3), (0, 2), (1, 2), (1, 1)])
    puzzle.add_thermometer([(3, 4), (3, 3), (4, 3)])
    puzzle.add_thermometer([(2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(2, 1), (2, 2), (2, 3)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])

    return puzzle
