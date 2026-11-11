"""PuzzleMadness Thermometer Sudoku — 2025-05-25."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-25'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/25'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (6, 4), (7, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_thermometer([(2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (2, 4)])
    puzzle.add_thermometer([(3, 7), (3, 6), (3, 5), (4, 5), (4, 6), (4, 7)])
    puzzle.add_thermometer([(4, 2), (4, 1), (5, 1), (6, 1), (7, 1)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 7), (0, 7)])
    puzzle.add_thermometer([(4, 3), (3, 3), (3, 4), (4, 4)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1), (0, 0)])
    puzzle.add_thermometer([(7, 8), (7, 7), (8, 7), (8, 8)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 6), (2, 7)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 1)])
    puzzle.add_thermometer([(8, 3), (7, 3), (6, 3)])
    puzzle.add_thermometer([(5, 4), (5, 3), (5, 2)])
    puzzle.add_thermometer([(5, 6), (6, 6), (7, 6)])

    return puzzle
