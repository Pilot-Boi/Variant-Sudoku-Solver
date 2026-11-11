"""PuzzleMadness Thermometer Sudoku — 2025-05-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 4, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 4), (4, 4), (4, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(2, 0), (2, 1), (1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(6, 8), (6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(6, 4), (7, 4), (8, 4), (8, 5)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 4), (1, 4)])
    puzzle.add_thermometer([(5, 0), (5, 1), (4, 1), (4, 0)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 3), (6, 3)])
    puzzle.add_thermometer([(4, 8), (3, 8), (3, 7), (3, 6)])
    puzzle.add_thermometer([(3, 1), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(4, 6), (5, 6), (5, 7), (5, 8)])
    puzzle.add_thermometer([(7, 0), (6, 0), (6, 1), (7, 1)])
    puzzle.add_thermometer([(8, 8), (8, 7), (7, 7)])
    puzzle.add_thermometer([(5, 3), (5, 2), (4, 2)])
    puzzle.add_thermometer([(0, 3), (1, 3), (2, 3)])

    return puzzle
