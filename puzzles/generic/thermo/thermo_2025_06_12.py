"""PuzzleMadness Thermometer Sudoku — 2025-06-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 6, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 4), (6, 3), (7, 3), (7, 2), (6, 2), (5, 2)])
    puzzle.add_thermometer([(5, 1), (4, 1), (4, 0), (5, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8), (2, 8), (3, 8)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4), (3, 5)])
    puzzle.add_thermometer([(2, 3), (2, 2), (2, 1), (3, 1)])
    puzzle.add_thermometer([(3, 6), (3, 7), (4, 7), (4, 6)])
    puzzle.add_thermometer([(8, 1), (8, 0), (7, 0), (7, 1)])
    puzzle.add_thermometer([(0, 5), (0, 4), (1, 4), (1, 5)])
    puzzle.add_thermometer([(8, 4), (8, 5), (7, 5), (7, 4)])
    puzzle.add_thermometer([(7, 8), (7, 7), (8, 7)])
    puzzle.add_thermometer([(5, 6), (5, 5), (5, 4)])
    puzzle.add_thermometer([(1, 0), (1, 1), (0, 1)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3)])
    puzzle.add_thermometer([(2, 5), (2, 6), (2, 7)])

    return puzzle
