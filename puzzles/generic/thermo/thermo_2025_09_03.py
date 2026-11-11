"""PuzzleMadness Thermometer Sudoku — 2025-09-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [2, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 8, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 4), (5, 4), (4, 4), (4, 5), (5, 5), (6, 5)])
    puzzle.add_thermometer([(2, 7), (2, 6), (1, 6), (1, 7), (0, 7)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7), (5, 7), (5, 8)])
    puzzle.add_thermometer([(8, 2), (8, 3), (7, 3), (7, 4)])
    puzzle.add_thermometer([(4, 3), (4, 2), (5, 2), (5, 3)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3), (1, 3)])
    puzzle.add_thermometer([(5, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(3, 3), (2, 3), (2, 2)])
    puzzle.add_thermometer([(7, 8), (7, 7), (7, 6)])
    puzzle.add_thermometer([(7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(3, 1), (2, 1), (2, 0)])
    puzzle.add_thermometer([(3, 8), (3, 7), (3, 6)])

    return puzzle
