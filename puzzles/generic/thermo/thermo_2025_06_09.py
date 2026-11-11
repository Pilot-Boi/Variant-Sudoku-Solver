"""PuzzleMadness Thermometer Sudoku — 2025-06-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 6), (5, 6), (4, 6), (4, 7), (3, 7), (3, 8)])
    puzzle.add_thermometer([(4, 5), (5, 5), (5, 4), (4, 4), (4, 3), (3, 3)])
    puzzle.add_thermometer([(0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3), (6, 3), (6, 4)])
    puzzle.add_thermometer([(8, 7), (8, 8), (7, 8), (7, 7), (7, 6)])
    puzzle.add_thermometer([(3, 1), (3, 2), (4, 2), (5, 2)])
    puzzle.add_thermometer([(1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_thermometer([(7, 0), (7, 1), (8, 1), (8, 0)])
    puzzle.add_thermometer([(0, 1), (1, 1), (1, 0), (0, 0)])
    puzzle.add_thermometer([(7, 4), (7, 5), (6, 5)])
    puzzle.add_thermometer([(5, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(3, 4), (2, 4), (2, 3)])

    return puzzle
