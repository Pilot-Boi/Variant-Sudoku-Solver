"""PuzzleMadness Thermometer Sudoku — 2025-02-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 4), (4, 3), (5, 3), (6, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(2, 3), (2, 4), (2, 5), (1, 5), (1, 4), (1, 3)])
    puzzle.add_thermometer([(3, 6), (2, 6), (2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (2, 1), (2, 0)])
    puzzle.add_thermometer([(1, 7), (1, 8), (0, 8), (0, 7), (0, 6)])
    puzzle.add_thermometer([(4, 0), (5, 0), (5, 1), (4, 1)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_thermometer([(3, 1), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(8, 6), (7, 6), (6, 6)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(6, 0), (6, 1), (7, 1)])
    puzzle.add_thermometer([(7, 5), (8, 5), (8, 4)])

    return puzzle
