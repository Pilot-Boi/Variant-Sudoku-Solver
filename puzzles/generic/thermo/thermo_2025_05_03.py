"""PuzzleMadness Thermometer Sudoku — 2025-05-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 5), (3, 5), (4, 5), (4, 4), (5, 4), (5, 5)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(4, 0), (4, 1), (5, 1), (5, 0), (6, 0)])
    puzzle.add_thermometer([(4, 3), (5, 3), (6, 3), (7, 3), (8, 3)])
    puzzle.add_thermometer([(1, 6), (1, 7), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(5, 6), (5, 7), (6, 7), (7, 7)])
    puzzle.add_thermometer([(1, 4), (2, 4), (2, 3)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8)])
    puzzle.add_thermometer([(6, 2), (6, 1), (7, 1)])
    puzzle.add_thermometer([(3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(8, 4), (7, 4), (6, 4)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])

    return puzzle
