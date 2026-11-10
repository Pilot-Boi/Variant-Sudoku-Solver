"""PuzzleMadness Thermometer Sudoku — 2026-10-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 3, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 5), (2, 5), (2, 4), (2, 3), (3, 3), (4, 3)])
    puzzle.add_thermometer([(1, 3), (1, 2), (1, 1), (1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0), (3, 1), (3, 2)])
    puzzle.add_thermometer([(2, 7), (2, 8), (3, 8), (3, 7), (4, 7)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6), (1, 6), (2, 6)])
    puzzle.add_thermometer([(6, 4), (6, 3), (6, 2), (6, 1)])
    puzzle.add_thermometer([(5, 2), (5, 1), (4, 1), (4, 2)])
    puzzle.add_thermometer([(8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_thermometer([(7, 7), (8, 7), (8, 8)])
    puzzle.add_thermometer([(3, 4), (4, 4), (5, 4)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(4, 5), (4, 6), (5, 6)])
    puzzle.add_thermometer([(5, 7), (6, 7), (6, 8)])

    return puzzle
