"""PuzzleMadness Thermometer Sudoku — 2025-12-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 6, 0, 0, 0, 0],
        [0, 5, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 8, 0, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3), (6, 3), (6, 4), (6, 5)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7), (1, 6), (0, 6)])
    puzzle.add_thermometer([(3, 3), (4, 3), (4, 2), (4, 1), (4, 0)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (7, 1), (8, 1)])
    puzzle.add_thermometer([(4, 7), (4, 8), (5, 8), (6, 8), (7, 8)])
    puzzle.add_thermometer([(1, 5), (1, 4), (2, 4), (2, 3)])
    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1), (0, 0)])
    puzzle.add_thermometer([(6, 6), (5, 6), (5, 5), (5, 4)])
    puzzle.add_thermometer([(4, 4), (4, 5), (3, 5), (2, 5)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8)])
    puzzle.add_thermometer([(8, 5), (8, 6), (7, 6)])
    puzzle.add_thermometer([(7, 7), (6, 7), (5, 7)])
    puzzle.add_thermometer([(3, 0), (3, 1), (3, 2)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])

    return puzzle
