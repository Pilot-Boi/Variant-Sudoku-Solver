"""PuzzleMadness Thermometer Sudoku — 2025-12-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 2)])
    puzzle.add_thermometer([(3, 6), (2, 6), (1, 6), (1, 7), (1, 8), (2, 8)])
    puzzle.add_thermometer([(8, 3), (8, 4), (8, 5), (8, 6), (7, 6)])
    puzzle.add_thermometer([(6, 7), (6, 6), (6, 5), (6, 4), (6, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_thermometer([(4, 1), (3, 1), (2, 1), (1, 1)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0)])
    puzzle.add_thermometer([(4, 5), (3, 5), (3, 4)])
    puzzle.add_thermometer([(5, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(0, 5), (1, 5), (2, 5)])
    puzzle.add_thermometer([(5, 4), (5, 3), (5, 2)])
    puzzle.add_thermometer([(4, 7), (5, 7), (5, 6)])

    return puzzle
