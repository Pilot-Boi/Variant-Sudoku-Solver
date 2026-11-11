"""PuzzleMadness Thermometer Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 8, 0, 0, 0, 0],
        [5, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 3, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(7, 2), (6, 2), (6, 1), (7, 1), (8, 1), (8, 0)])
    puzzle.add_thermometer([(1, 6), (1, 5), (2, 5), (3, 5), (4, 5)])
    puzzle.add_thermometer([(5, 5), (6, 5), (7, 5), (7, 6), (6, 6)])
    puzzle.add_thermometer([(3, 0), (2, 0), (1, 0), (1, 1), (2, 1)])
    puzzle.add_thermometer([(0, 1), (0, 2), (0, 3), (0, 4), (1, 4)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 4), (6, 4)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(1, 3), (1, 2), (2, 2), (3, 2)])
    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7), (5, 7)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3)])
    puzzle.add_thermometer([(2, 6), (2, 7), (1, 7)])
    puzzle.add_thermometer([(4, 6), (4, 7), (4, 8)])

    return puzzle
