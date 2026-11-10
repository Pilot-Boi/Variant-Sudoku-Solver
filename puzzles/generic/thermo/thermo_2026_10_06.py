"""PuzzleMadness Thermometer Sudoku — 2026-10-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (6, 3)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8), (7, 7), (7, 6)])
    puzzle.add_thermometer([(3, 5), (3, 6), (2, 6), (2, 7), (3, 7)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(5, 2), (6, 2), (6, 1), (6, 0)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 2), (2, 3)])
    puzzle.add_thermometer([(4, 7), (4, 8), (5, 8), (5, 7)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 3), (8, 4)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(3, 3), (3, 2), (4, 2)])
    puzzle.add_thermometer([(2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0)])
    puzzle.add_thermometer([(6, 8), (6, 7), (6, 6)])

    return puzzle
