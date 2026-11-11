"""PuzzleMadness Thermometer Sudoku — 2025-03-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1)])
    puzzle.add_thermometer([(5, 4), (4, 4), (3, 4), (3, 3), (3, 2)])
    puzzle.add_thermometer([(5, 7), (5, 8), (4, 8), (4, 7), (3, 7)])
    puzzle.add_thermometer([(6, 2), (6, 1), (6, 0), (7, 0), (8, 0)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8), (8, 7), (8, 6)])
    puzzle.add_thermometer([(1, 3), (0, 3), (0, 4), (0, 5)])
    puzzle.add_thermometer([(4, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_thermometer([(2, 8), (2, 7), (1, 7), (0, 7)])
    puzzle.add_thermometer([(1, 1), (1, 2), (2, 2), (2, 3)])
    puzzle.add_thermometer([(4, 6), (5, 6), (5, 5), (4, 5)])
    puzzle.add_thermometer([(3, 5), (2, 5), (1, 5), (1, 4)])
    puzzle.add_thermometer([(6, 5), (7, 5), (7, 6), (6, 6)])
    puzzle.add_thermometer([(4, 2), (4, 1), (3, 1)])
    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4)])

    return puzzle
