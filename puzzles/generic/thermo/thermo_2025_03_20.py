"""PuzzleMadness Thermometer Sudoku — 2025-03-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 8), (8, 7), (8, 6), (8, 5), (7, 5), (7, 6)])
    puzzle.add_thermometer([(3, 6), (4, 6), (5, 6), (5, 7), (4, 7)])
    puzzle.add_thermometer([(4, 3), (4, 4), (3, 4), (2, 4), (1, 4)])
    puzzle.add_thermometer([(7, 4), (8, 4), (8, 3), (8, 2), (8, 1)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2), (1, 2)])
    puzzle.add_thermometer([(2, 5), (1, 5), (1, 6), (2, 6)])
    puzzle.add_thermometer([(5, 0), (5, 1), (5, 2), (4, 2)])
    puzzle.add_thermometer([(3, 0), (2, 0), (2, 1), (3, 1)])
    puzzle.add_thermometer([(2, 2), (3, 2), (3, 3), (2, 3)])
    puzzle.add_thermometer([(5, 3), (5, 4), (6, 4)])
    puzzle.add_thermometer([(7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(6, 2), (6, 3), (7, 3)])
    puzzle.add_thermometer([(4, 8), (5, 8), (6, 8)])

    return puzzle
