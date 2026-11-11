"""PuzzleMadness Thermometer Sudoku — 2025-06-19."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-19'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/19'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 1],
        [0, 0, 0, 5, 0, 0, 0, 6, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 3, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 0), (4, 0), (3, 0), (3, 1), (4, 1), (5, 1)])
    puzzle.add_thermometer([(3, 2), (3, 3), (4, 3), (4, 4), (5, 4)])
    puzzle.add_thermometer([(4, 6), (4, 7), (4, 8), (3, 8), (3, 7)])
    puzzle.add_thermometer([(8, 0), (8, 1), (7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(0, 6), (0, 7), (1, 7), (1, 6)])
    puzzle.add_thermometer([(6, 8), (5, 8), (5, 7), (6, 7)])
    puzzle.add_thermometer([(7, 5), (6, 5), (6, 6), (5, 6)])
    puzzle.add_thermometer([(1, 5), (1, 4), (1, 3), (2, 3)])
    puzzle.add_thermometer([(2, 6), (2, 7), (2, 8), (1, 8)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2)])
    puzzle.add_thermometer([(6, 4), (7, 4), (8, 4)])
    puzzle.add_thermometer([(0, 3), (0, 4), (0, 5)])

    return puzzle
