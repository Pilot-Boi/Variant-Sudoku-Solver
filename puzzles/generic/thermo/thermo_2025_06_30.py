"""PuzzleMadness Thermometer Sudoku — 2025-06-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 6), (3, 7), (4, 7), (5, 7), (5, 6), (6, 6)])
    puzzle.add_thermometer([(5, 4), (6, 4), (6, 5), (7, 5), (7, 4), (7, 3)])
    puzzle.add_thermometer([(5, 1), (4, 1), (4, 0), (5, 0), (6, 0), (6, 1)])
    puzzle.add_thermometer([(1, 3), (2, 3), (3, 3), (3, 2)])
    puzzle.add_thermometer([(0, 0), (1, 0), (1, 1), (2, 1)])
    puzzle.add_thermometer([(8, 3), (8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(0, 6), (1, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(0, 4), (0, 5), (1, 5)])
    puzzle.add_thermometer([(1, 8), (2, 8), (3, 8)])
    puzzle.add_thermometer([(6, 7), (6, 8), (5, 8)])
    puzzle.add_thermometer([(7, 6), (8, 6), (8, 7)])
    puzzle.add_thermometer([(7, 2), (6, 2), (5, 2)])
    puzzle.add_thermometer([(3, 4), (4, 4), (4, 3)])

    return puzzle
