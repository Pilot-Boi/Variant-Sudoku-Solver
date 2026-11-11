"""PuzzleMadness Thermometer Sudoku — 2025-09-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 9, 4, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 0), (7, 1), (7, 2), (8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(0, 2), (1, 2), (1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(8, 7), (8, 6), (7, 6), (7, 5), (7, 4)])
    puzzle.add_thermometer([(1, 7), (2, 7), (2, 6), (1, 6), (1, 5)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(6, 8), (5, 8), (5, 7), (6, 7)])
    puzzle.add_thermometer([(6, 0), (6, 1), (6, 2)])
    puzzle.add_thermometer([(6, 4), (5, 4), (5, 3)])
    puzzle.add_thermometer([(8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(0, 6), (0, 5), (0, 4)])

    return puzzle
