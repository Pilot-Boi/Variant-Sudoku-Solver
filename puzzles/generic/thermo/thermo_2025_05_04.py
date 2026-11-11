"""PuzzleMadness Thermometer Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 6), (5, 7), (4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (7, 7), (6, 7)])
    puzzle.add_thermometer([(7, 4), (7, 3), (7, 2), (7, 1), (7, 0)])
    puzzle.add_thermometer([(7, 6), (7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4), (5, 4)])
    puzzle.add_thermometer([(4, 1), (3, 1), (2, 1), (1, 1)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3), (1, 4)])
    puzzle.add_thermometer([(1, 6), (1, 5), (2, 5), (2, 6)])
    puzzle.add_thermometer([(5, 3), (6, 3), (6, 4)])
    puzzle.add_thermometer([(1, 2), (0, 2), (0, 1)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(3, 7), (2, 7), (1, 7)])
    puzzle.add_thermometer([(4, 6), (4, 5), (5, 5)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(0, 7), (0, 6), (0, 5)])

    return puzzle
