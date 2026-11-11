"""PuzzleMadness Thermometer Sudoku — 2025-01-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-01-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/1/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 4), (3, 4), (2, 4), (2, 3), (2, 2), (3, 2)])
    puzzle.add_thermometer([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (5, 4)])
    puzzle.add_thermometer([(4, 2), (5, 2), (6, 2), (6, 1), (6, 0)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6), (2, 6), (3, 6)])
    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7), (4, 8)])
    puzzle.add_thermometer([(0, 5), (0, 4), (1, 4), (1, 3)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 4)])
    puzzle.add_thermometer([(3, 3), (4, 3), (5, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (7, 8)])
    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0)])
    puzzle.add_thermometer([(3, 8), (3, 7), (2, 7)])
    puzzle.add_thermometer([(6, 3), (7, 3), (7, 2)])
    puzzle.add_thermometer([(7, 6), (8, 6), (8, 7)])

    return puzzle
