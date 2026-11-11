"""PuzzleMadness Thermometer Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 3), (4, 4), (3, 4), (3, 5), (4, 5), (4, 6)])
    puzzle.add_thermometer([(5, 6), (5, 7), (4, 7), (3, 7), (2, 7), (2, 8)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0), (4, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(7, 4), (7, 5), (7, 6), (6, 6)])
    puzzle.add_thermometer([(2, 3), (1, 3), (1, 4), (2, 4)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(6, 5), (6, 4), (6, 3), (7, 3)])
    puzzle.add_thermometer([(3, 6), (2, 6), (2, 5), (1, 5)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(1, 2), (1, 1), (1, 0)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2)])
    puzzle.add_thermometer([(5, 2), (5, 3), (5, 4)])

    return puzzle
