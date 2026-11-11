"""PuzzleMadness Thermometer Sudoku — 2025-03-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 5, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (6, 4), (6, 3), (7, 3), (7, 4), (7, 5)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 7), (8, 7), (8, 8)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3), (1, 3), (1, 4)])
    puzzle.add_thermometer([(4, 2), (4, 1), (4, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(7, 1), (7, 0), (6, 0), (5, 0)])
    puzzle.add_thermometer([(1, 2), (2, 2), (2, 1), (1, 1)])
    puzzle.add_thermometer([(3, 5), (4, 5), (4, 6), (3, 6)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_thermometer([(1, 8), (0, 8), (0, 7)])
    puzzle.add_thermometer([(1, 6), (2, 6), (2, 5)])
    puzzle.add_thermometer([(8, 4), (8, 3), (8, 2)])
    puzzle.add_thermometer([(5, 3), (5, 4), (4, 4)])
    puzzle.add_thermometer([(5, 6), (5, 7), (4, 7)])
    puzzle.add_thermometer([(2, 0), (1, 0), (0, 0)])

    return puzzle
