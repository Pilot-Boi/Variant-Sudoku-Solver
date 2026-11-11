"""PuzzleMadness Thermometer Sudoku — 2025-03-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 4), (5, 4), (6, 4), (6, 5), (7, 5), (8, 5)])
    puzzle.add_thermometer([(2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (3, 3)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 7), (1, 7), (1, 8), (0, 8)])
    puzzle.add_thermometer([(8, 2), (8, 1), (7, 1), (7, 2), (6, 2), (6, 1)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8), (5, 7), (4, 7)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 4), (1, 4)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1)])
    puzzle.add_thermometer([(4, 0), (4, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(6, 3), (7, 3), (8, 3)])
    puzzle.add_thermometer([(7, 6), (7, 7), (7, 8)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 5)])

    return puzzle
