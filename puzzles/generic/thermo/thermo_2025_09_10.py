"""PuzzleMadness Thermometer Sudoku — 2025-09-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 2, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 3), (3, 3), (3, 4), (4, 4), (5, 4)])
    puzzle.add_thermometer([(4, 1), (5, 1), (5, 2), (4, 2), (3, 2)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(6, 4), (6, 3), (7, 3), (8, 3)])
    puzzle.add_thermometer([(7, 2), (7, 1), (6, 1), (6, 2)])
    puzzle.add_thermometer([(4, 0), (3, 0), (3, 1), (2, 1)])
    puzzle.add_thermometer([(6, 6), (5, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(1, 2), (1, 1), (1, 0), (0, 0)])
    puzzle.add_thermometer([(2, 4), (1, 4), (1, 3), (2, 3)])
    puzzle.add_thermometer([(4, 7), (4, 8), (5, 8)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6)])
    puzzle.add_thermometer([(7, 0), (8, 0), (8, 1)])

    return puzzle
