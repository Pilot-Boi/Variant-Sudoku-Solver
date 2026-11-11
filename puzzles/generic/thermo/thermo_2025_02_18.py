"""PuzzleMadness Thermometer Sudoku — 2025-02-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-02-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/2/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 1, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 2), (5, 2), (4, 2), (3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(4, 3), (3, 3), (2, 3), (2, 4), (2, 5)])
    puzzle.add_thermometer([(5, 7), (5, 6), (6, 6), (7, 6), (8, 6)])
    puzzle.add_thermometer([(6, 1), (7, 1), (8, 1), (8, 0), (7, 0)])
    puzzle.add_thermometer([(2, 1), (2, 0), (1, 0), (1, 1), (0, 1)])
    puzzle.add_thermometer([(5, 5), (6, 5), (7, 5), (7, 4), (6, 4)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 5), (0, 5)])
    puzzle.add_thermometer([(7, 7), (6, 7), (6, 8), (5, 8)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8), (0, 8)])
    puzzle.add_thermometer([(7, 2), (7, 3), (6, 3), (5, 3)])
    puzzle.add_thermometer([(3, 6), (4, 6), (4, 5)])
    puzzle.add_thermometer([(4, 0), (5, 0), (5, 1)])
    puzzle.add_thermometer([(2, 7), (3, 7), (4, 7)])

    return puzzle
