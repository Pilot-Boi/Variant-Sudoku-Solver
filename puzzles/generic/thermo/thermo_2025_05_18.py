"""PuzzleMadness Thermometer Sudoku — 2025-05-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 3, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(5, 2), (6, 2), (6, 3), (7, 3), (7, 4)])
    puzzle.add_thermometer([(1, 4), (0, 4), (0, 5), (1, 5), (2, 5)])
    puzzle.add_thermometer([(4, 7), (4, 8), (5, 8), (5, 7), (5, 6)])
    puzzle.add_thermometer([(1, 8), (2, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(4, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(5, 0), (5, 1), (6, 1)])
    puzzle.add_thermometer([(3, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(2, 3), (3, 3), (4, 3)])
    puzzle.add_thermometer([(6, 5), (6, 4), (5, 4)])

    return puzzle
