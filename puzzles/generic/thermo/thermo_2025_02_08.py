"""PuzzleMadness Thermometer Sudoku — 2025-02-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [3, 0, 2, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)])
    puzzle.add_thermometer([(7, 1), (7, 2), (6, 2), (6, 3), (7, 3)])
    puzzle.add_thermometer([(2, 7), (2, 6), (2, 5), (1, 5), (1, 6)])
    puzzle.add_thermometer([(7, 8), (6, 8), (6, 7), (7, 7), (7, 6)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1), (1, 2)])
    puzzle.add_thermometer([(8, 4), (8, 5), (7, 5), (7, 4), (6, 4)])
    puzzle.add_thermometer([(6, 5), (6, 6), (5, 6), (4, 6)])
    puzzle.add_thermometer([(3, 6), (3, 7), (4, 7), (4, 8)])
    puzzle.add_thermometer([(5, 0), (5, 1), (6, 1)])
    puzzle.add_thermometer([(4, 1), (4, 0), (3, 0)])
    puzzle.add_thermometer([(5, 2), (4, 2), (3, 2)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])

    return puzzle
