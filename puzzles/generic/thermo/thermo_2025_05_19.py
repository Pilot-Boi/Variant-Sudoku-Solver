"""PuzzleMadness Thermometer Sudoku — 2025-05-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 6), (5, 7), (5, 8), (4, 8), (4, 7), (4, 6)])
    puzzle.add_thermometer([(3, 5), (3, 4), (4, 4), (4, 3), (5, 3), (5, 4)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (8, 2), (8, 1), (8, 0)])
    puzzle.add_thermometer([(1, 0), (2, 0), (3, 0), (3, 1), (4, 1), (5, 1)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8), (1, 7), (2, 7), (2, 8)])
    puzzle.add_thermometer([(1, 5), (1, 6), (0, 6), (0, 5), (0, 4)])
    puzzle.add_thermometer([(2, 3), (2, 4), (1, 4), (1, 3), (1, 2)])
    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1), (0, 2)])
    puzzle.add_thermometer([(7, 4), (7, 3), (6, 3), (6, 4)])
    puzzle.add_thermometer([(8, 6), (8, 5), (8, 4), (8, 3)])
    puzzle.add_thermometer([(5, 5), (6, 5), (7, 5)])
    puzzle.add_thermometer([(7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(4, 2), (3, 2), (2, 2)])
    puzzle.add_thermometer([(8, 8), (7, 8), (7, 7)])

    return puzzle
