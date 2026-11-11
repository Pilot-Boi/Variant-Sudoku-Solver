"""PuzzleMadness Thermometer Sudoku — 2025-06-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 6), (5, 6), (5, 5), (5, 4), (4, 4), (4, 5)])
    puzzle.add_thermometer([(1, 4), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(8, 2), (8, 1), (8, 0), (7, 0), (6, 0)])
    puzzle.add_thermometer([(3, 5), (3, 6), (3, 7), (2, 7)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 7), (0, 7)])
    puzzle.add_thermometer([(6, 4), (6, 3), (7, 3), (7, 4)])
    puzzle.add_thermometer([(6, 7), (7, 7), (7, 8), (8, 8)])
    puzzle.add_thermometer([(4, 7), (4, 8), (3, 8)])
    puzzle.add_thermometer([(5, 1), (6, 1), (6, 2)])
    puzzle.add_thermometer([(7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(2, 4), (2, 5), (2, 6)])
    puzzle.add_thermometer([(4, 2), (4, 3), (5, 3)])

    return puzzle
