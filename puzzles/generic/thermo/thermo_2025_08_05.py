"""PuzzleMadness Thermometer Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 5), (4, 6), (5, 6), (6, 6), (6, 5), (5, 5)])
    puzzle.add_thermometer([(7, 3), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3), (0, 2), (0, 1)])
    puzzle.add_thermometer([(2, 7), (1, 7), (1, 6), (1, 5), (1, 4)])
    puzzle.add_thermometer([(7, 0), (6, 0), (5, 0), (4, 0)])
    puzzle.add_thermometer([(7, 5), (7, 6), (7, 7), (8, 7)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2), (2, 2)])
    puzzle.add_thermometer([(5, 4), (4, 4), (3, 4), (3, 5)])
    puzzle.add_thermometer([(5, 2), (5, 1), (4, 1), (4, 2)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (7, 1)])
    puzzle.add_thermometer([(5, 7), (4, 7), (3, 7), (3, 8)])
    puzzle.add_thermometer([(2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(1, 2), (1, 1), (1, 0)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4)])

    return puzzle
