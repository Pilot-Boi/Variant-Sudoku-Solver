"""PuzzleMadness Thermometer Sudoku — 2025-11-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 6), (5, 5), (6, 5), (6, 4), (6, 3), (6, 2)])
    puzzle.add_thermometer([(4, 7), (4, 6), (4, 5), (4, 4), (4, 3), (5, 3)])
    puzzle.add_thermometer([(3, 5), (3, 6), (2, 6), (1, 6), (1, 5), (2, 5)])
    puzzle.add_thermometer([(7, 7), (6, 7), (6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(1, 4), (0, 4), (0, 3), (1, 3), (2, 3)])
    puzzle.add_thermometer([(8, 3), (7, 3), (7, 2), (8, 2)])
    puzzle.add_thermometer([(2, 2), (3, 2), (3, 3), (3, 4)])
    puzzle.add_thermometer([(6, 1), (7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(4, 0), (4, 1), (5, 1)])
    puzzle.add_thermometer([(1, 1), (1, 2), (0, 2)])
    puzzle.add_thermometer([(2, 8), (2, 7), (1, 7)])
    puzzle.add_thermometer([(7, 5), (7, 4), (8, 4)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])

    return puzzle
