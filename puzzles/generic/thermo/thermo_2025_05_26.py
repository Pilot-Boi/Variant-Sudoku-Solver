"""PuzzleMadness Thermometer Sudoku — 2025-05-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 2), (6, 3), (7, 3), (8, 3), (8, 4), (8, 5)])
    puzzle.add_thermometer([(3, 1), (4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_thermometer([(4, 3), (5, 3), (5, 4), (5, 5), (6, 5)])
    puzzle.add_thermometer([(0, 3), (0, 4), (1, 4), (1, 3), (2, 3)])
    puzzle.add_thermometer([(3, 5), (4, 5), (4, 6), (3, 6), (3, 7)])
    puzzle.add_thermometer([(8, 6), (8, 7), (7, 7), (7, 6)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0), (1, 0)])
    puzzle.add_thermometer([(1, 2), (1, 1), (0, 1), (0, 2)])
    puzzle.add_thermometer([(2, 7), (2, 6), (2, 5), (2, 4)])
    puzzle.add_thermometer([(8, 0), (7, 0), (6, 0), (5, 0)])
    puzzle.add_thermometer([(1, 8), (0, 8), (0, 7)])
    puzzle.add_thermometer([(3, 2), (4, 2), (5, 2)])
    puzzle.add_thermometer([(6, 4), (7, 4), (7, 5)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 1)])

    return puzzle
