"""PuzzleMadness Thermometer Sudoku — 2025-04-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 0, 0, 0, 0, 0, 0, 6, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 1), (4, 2), (3, 2), (3, 3), (4, 3), (4, 4)])
    puzzle.add_thermometer([(3, 7), (3, 6), (4, 6), (4, 7), (5, 7), (5, 6)])
    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4), (7, 5), (7, 6)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(0, 0), (0, 1), (1, 1), (1, 2), (0, 2)])
    puzzle.add_thermometer([(2, 5), (2, 4), (1, 4), (1, 5)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8), (8, 7)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(7, 7), (6, 7), (6, 6), (6, 5)])
    puzzle.add_thermometer([(7, 2), (6, 2), (6, 3), (7, 3)])
    puzzle.add_thermometer([(1, 6), (1, 7), (0, 7), (0, 6)])
    puzzle.add_thermometer([(1, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1)])

    return puzzle
