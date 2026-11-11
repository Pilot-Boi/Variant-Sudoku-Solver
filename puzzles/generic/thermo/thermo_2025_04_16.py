"""PuzzleMadness Thermometer Sudoku — 2025-04-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 4, 0, 3],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 1), (8, 1), (8, 0)])
    puzzle.add_thermometer([(3, 4), (2, 4), (1, 4), (1, 5), (2, 5)])
    puzzle.add_thermometer([(5, 7), (5, 6), (5, 5), (5, 4)])
    puzzle.add_thermometer([(5, 1), (6, 1), (6, 0), (5, 0)])
    puzzle.add_thermometer([(7, 6), (7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(6, 4), (6, 3), (5, 3), (5, 2)])
    puzzle.add_thermometer([(3, 7), (4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(8, 8), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(1, 8), (2, 8), (2, 7), (1, 7)])
    puzzle.add_thermometer([(3, 0), (4, 0), (4, 1)])
    puzzle.add_thermometer([(4, 3), (4, 2), (3, 2)])
    puzzle.add_thermometer([(8, 4), (8, 3), (7, 3)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 4)])
    puzzle.add_thermometer([(4, 5), (4, 6), (3, 6)])
    puzzle.add_thermometer([(2, 6), (1, 6), (0, 6)])

    return puzzle
