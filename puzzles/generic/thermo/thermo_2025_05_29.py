"""PuzzleMadness Thermometer Sudoku — 2025-05-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 4), (4, 4), (4, 3), (3, 3), (3, 2), (4, 2)])
    puzzle.add_thermometer([(8, 2), (7, 2), (7, 3), (6, 3), (5, 3), (5, 2)])
    puzzle.add_thermometer([(3, 1), (4, 1), (5, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(2, 8), (2, 7), (3, 7), (3, 8), (4, 8)])
    puzzle.add_thermometer([(3, 6), (4, 6), (4, 5), (3, 5), (3, 4)])
    puzzle.add_thermometer([(1, 5), (1, 6), (2, 6), (2, 5)])
    puzzle.add_thermometer([(2, 2), (1, 2), (1, 3), (2, 3)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(6, 5), (6, 6), (7, 6)])
    puzzle.add_thermometer([(8, 1), (7, 1), (7, 0)])
    puzzle.add_thermometer([(8, 3), (8, 4), (7, 4)])
    puzzle.add_thermometer([(5, 6), (5, 7), (5, 8)])
    puzzle.add_thermometer([(0, 3), (0, 2), (0, 1)])

    return puzzle
