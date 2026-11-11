"""PuzzleMadness Thermometer Sudoku — 2025-08-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-08-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/8/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 4), (4, 4), (4, 3), (4, 2), (3, 2), (2, 2)])
    puzzle.add_thermometer([(5, 2), (5, 1), (5, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(6, 8), (6, 7), (6, 6), (7, 6), (7, 7)])
    puzzle.add_thermometer([(3, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_thermometer([(7, 1), (7, 2), (8, 2), (8, 1)])
    puzzle.add_thermometer([(2, 3), (2, 4), (1, 4), (1, 5)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4), (8, 4)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1)])
    puzzle.add_thermometer([(2, 6), (1, 6), (1, 7), (1, 8)])
    puzzle.add_thermometer([(4, 8), (5, 8), (5, 7), (4, 7)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])

    return puzzle
