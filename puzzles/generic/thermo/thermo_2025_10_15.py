"""PuzzleMadness Thermometer Sudoku — 2025-10-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 5],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0)])
    puzzle.add_thermometer([(0, 2), (0, 3), (0, 4), (0, 5), (0, 6)])
    puzzle.add_thermometer([(8, 2), (8, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 4)])
    puzzle.add_thermometer([(4, 6), (4, 5), (3, 5), (2, 5)])
    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(7, 4), (7, 5), (8, 5), (8, 4)])
    puzzle.add_thermometer([(5, 3), (5, 2), (5, 1), (4, 1)])
    puzzle.add_thermometer([(3, 3), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(4, 4), (5, 4), (5, 5), (5, 6)])
    puzzle.add_thermometer([(7, 6), (7, 7), (7, 8)])

    return puzzle
