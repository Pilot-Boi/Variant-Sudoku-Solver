"""PuzzleMadness Thermometer Sudoku — 2025-12-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 2, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 2, 0, 0, 5, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0), (4, 1), (4, 2), (3, 2)])
    puzzle.add_thermometer([(0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_thermometer([(6, 4), (6, 3), (6, 2), (7, 2), (7, 3), (7, 4)])
    puzzle.add_thermometer([(3, 5), (4, 5), (5, 5), (5, 6)])
    puzzle.add_thermometer([(2, 4), (3, 4), (3, 3), (2, 3)])
    puzzle.add_thermometer([(7, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_thermometer([(8, 6), (7, 6), (7, 5), (8, 5)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8), (6, 8)])
    puzzle.add_thermometer([(6, 0), (6, 1), (7, 1)])
    puzzle.add_thermometer([(1, 3), (1, 4), (0, 4)])
    puzzle.add_thermometer([(2, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(5, 7), (6, 7), (6, 6)])

    return puzzle
