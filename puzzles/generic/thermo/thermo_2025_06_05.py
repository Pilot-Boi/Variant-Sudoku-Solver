"""PuzzleMadness Thermometer Sudoku — 2025-06-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [5, 0, 0, 0, 9, 0, 0, 0, 0],
        [8, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 4, 0, 0, 1, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(1, 5), (1, 6), (1, 7), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(4, 8), (5, 8), (5, 7), (5, 6), (4, 6), (4, 7)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (8, 6), (8, 5)])
    puzzle.add_thermometer([(2, 3), (3, 3), (4, 3), (4, 4), (5, 4)])
    puzzle.add_thermometer([(6, 4), (7, 4), (7, 5), (6, 5), (6, 6)])
    puzzle.add_thermometer([(4, 1), (4, 2), (3, 2), (3, 1)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(3, 5), (2, 5), (2, 4), (3, 4)])
    puzzle.add_thermometer([(1, 4), (1, 3), (1, 2), (2, 2)])
    puzzle.add_thermometer([(6, 2), (6, 1), (5, 1)])
    puzzle.add_thermometer([(7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 3)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])

    return puzzle
