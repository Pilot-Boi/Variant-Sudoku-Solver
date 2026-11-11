"""PuzzleMadness Thermometer Sudoku — 2025-05-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 4), (4, 4), (4, 3), (5, 3), (5, 2), (4, 2)])
    puzzle.add_thermometer([(6, 5), (7, 5), (8, 5), (8, 6), (7, 6), (7, 7)])
    puzzle.add_thermometer([(0, 1), (0, 2), (1, 2), (2, 2), (2, 3)])
    puzzle.add_thermometer([(2, 5), (2, 6), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(4, 1), (4, 0), (5, 0), (6, 0)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 5), (5, 5)])
    puzzle.add_thermometer([(7, 3), (7, 4), (6, 4), (6, 3)])
    puzzle.add_thermometer([(1, 6), (0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(0, 3), (1, 3), (1, 4), (1, 5)])
    puzzle.add_thermometer([(3, 8), (4, 8), (4, 7), (3, 7)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(5, 7), (6, 7), (6, 6)])
    puzzle.add_thermometer([(6, 2), (6, 1), (7, 1)])
    puzzle.add_thermometer([(2, 1), (2, 0), (3, 0)])

    return puzzle
