"""PuzzleMadness Thermometer Sudoku — 2025-05-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 6, 0, 0],
        [0, 3, 0, 0, 0, 6, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 5), (6, 5), (6, 6), (5, 6), (5, 7), (4, 7)])
    puzzle.add_thermometer([(8, 3), (7, 3), (7, 2), (6, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(1, 4), (2, 4), (2, 3), (3, 3), (3, 4), (3, 5)])
    puzzle.add_thermometer([(6, 1), (6, 0), (5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3), (4, 2)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(1, 2), (1, 1), (2, 1), (2, 2)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8)])
    puzzle.add_thermometer([(2, 5), (2, 6), (1, 6)])
    puzzle.add_thermometer([(7, 1), (8, 1), (8, 2)])
    puzzle.add_thermometer([(7, 6), (8, 6), (8, 5)])
    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7)])

    return puzzle
