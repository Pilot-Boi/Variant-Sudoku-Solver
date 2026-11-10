"""PuzzleMadness Thermometer Sudoku — 2026-10-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (5, 2)])
    puzzle.add_thermometer([(1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6)])
    puzzle.add_thermometer([(7, 8), (7, 7), (6, 7), (6, 6), (7, 6)])
    puzzle.add_thermometer([(0, 2), (0, 3), (1, 3), (1, 2), (2, 2)])
    puzzle.add_thermometer([(8, 3), (8, 2), (7, 2), (7, 3), (7, 4)])
    puzzle.add_thermometer([(6, 5), (5, 5), (5, 4), (6, 4)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6), (3, 6)])
    puzzle.add_thermometer([(2, 7), (3, 7), (4, 7), (5, 7)])
    puzzle.add_thermometer([(6, 0), (7, 0), (8, 0), (8, 1)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])
    puzzle.add_thermometer([(4, 8), (5, 8), (6, 8)])
    puzzle.add_thermometer([(0, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(4, 2), (4, 3), (3, 3)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0)])

    return puzzle
