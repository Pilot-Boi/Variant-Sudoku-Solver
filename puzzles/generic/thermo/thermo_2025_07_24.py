"""PuzzleMadness Thermometer Sudoku — 2025-07-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-07-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/7/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 9, 0, 0, 0, 4, 0, 2],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 1, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 5), (4, 5), (4, 4), (5, 4), (5, 5), (6, 5)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0), (1, 0), (0, 0)])
    puzzle.add_thermometer([(2, 2), (2, 1), (3, 1), (3, 2), (3, 3)])
    puzzle.add_thermometer([(7, 2), (7, 1), (8, 1), (8, 0)])
    puzzle.add_thermometer([(8, 6), (8, 7), (8, 8), (7, 8)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_thermometer([(7, 4), (7, 5), (8, 5), (8, 4)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 2)])
    puzzle.add_thermometer([(3, 8), (3, 7), (3, 6)])
    puzzle.add_thermometer([(1, 1), (1, 2), (1, 3)])
    puzzle.add_thermometer([(6, 1), (5, 1), (4, 1)])
    puzzle.add_thermometer([(6, 7), (7, 7), (7, 6)])
    puzzle.add_thermometer([(0, 5), (0, 6), (0, 7)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])

    return puzzle
