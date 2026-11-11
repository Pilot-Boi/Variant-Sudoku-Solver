"""PuzzleMadness Thermometer Sudoku — 2025-04-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 5), (1, 5), (1, 6), (2, 6), (2, 7), (3, 7)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(7, 3), (7, 4), (8, 4), (8, 3), (8, 2)])
    puzzle.add_thermometer([(5, 8), (5, 7), (5, 6), (5, 5), (5, 4)])
    puzzle.add_thermometer([(3, 4), (3, 3), (4, 3), (5, 3), (6, 3)])
    puzzle.add_thermometer([(0, 2), (0, 3), (0, 4), (0, 5)])
    puzzle.add_thermometer([(2, 0), (1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(4, 6), (4, 5), (3, 5), (3, 6)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(2, 2), (2, 1), (1, 1), (1, 2)])
    puzzle.add_thermometer([(7, 7), (7, 6), (7, 5)])
    puzzle.add_thermometer([(1, 4), (1, 3), (2, 3)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6)])

    return puzzle
