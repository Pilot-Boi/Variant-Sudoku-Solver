"""PuzzleMadness Thermometer Sudoku — 2026-10-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 8), (4, 7), (5, 7), (5, 6), (5, 5), (5, 4)])
    puzzle.add_thermometer([(6, 6), (7, 6), (8, 6), (8, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(1, 7), (2, 7), (2, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(2, 0), (2, 1), (3, 1), (4, 1), (4, 2)])
    puzzle.add_thermometer([(0, 4), (1, 4), (1, 5), (1, 6), (2, 6)])
    puzzle.add_thermometer([(8, 5), (8, 4), (7, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4), (4, 4)])
    puzzle.add_thermometer([(5, 3), (5, 2), (6, 2)])
    puzzle.add_thermometer([(0, 3), (1, 3), (2, 3)])
    puzzle.add_thermometer([(1, 0), (1, 1), (0, 1)])
    puzzle.add_thermometer([(3, 5), (4, 5), (4, 6)])
    puzzle.add_thermometer([(0, 6), (0, 7), (0, 8)])

    return puzzle
