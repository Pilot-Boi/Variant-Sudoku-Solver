"""PuzzleMadness Thermometer Sudoku — 2025-03-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 8), (6, 8), (6, 7), (6, 6), (7, 6), (8, 6)])
    puzzle.add_thermometer([(5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0)])
    puzzle.add_thermometer([(4, 1), (4, 0), (3, 0), (3, 1), (2, 1), (1, 1)])
    puzzle.add_thermometer([(3, 7), (3, 8), (4, 8), (4, 7), (5, 7)])
    puzzle.add_thermometer([(2, 6), (2, 5), (2, 4), (3, 4)])
    puzzle.add_thermometer([(6, 3), (7, 3), (7, 4), (8, 4)])
    puzzle.add_thermometer([(0, 2), (1, 2), (1, 3), (0, 3)])
    puzzle.add_thermometer([(7, 7), (7, 8), (8, 8), (8, 7)])
    puzzle.add_thermometer([(8, 1), (8, 2), (7, 2)])
    puzzle.add_thermometer([(4, 4), (4, 5), (5, 5)])
    puzzle.add_thermometer([(7, 0), (7, 1), (6, 1)])

    return puzzle
