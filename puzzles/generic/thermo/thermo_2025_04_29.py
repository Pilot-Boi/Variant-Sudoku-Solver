"""PuzzleMadness Thermometer Sudoku — 2025-04-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-04-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/4/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 1), (6, 1), (6, 2), (6, 3), (6, 4), (5, 4)])
    puzzle.add_thermometer([(7, 2), (8, 2), (8, 1), (7, 1), (7, 0), (8, 0)])
    puzzle.add_thermometer([(4, 5), (3, 5), (3, 4), (3, 3), (2, 3)])
    puzzle.add_thermometer([(8, 7), (8, 6), (7, 6), (7, 7), (7, 8)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0), (4, 1), (3, 1)])
    puzzle.add_thermometer([(0, 4), (0, 5), (1, 5), (1, 6)])
    puzzle.add_thermometer([(2, 6), (2, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(4, 6), (5, 6), (5, 7), (4, 7)])
    puzzle.add_thermometer([(5, 3), (5, 2), (4, 2)])
    puzzle.add_thermometer([(7, 5), (6, 5), (5, 5)])
    puzzle.add_thermometer([(8, 4), (7, 4), (7, 3)])
    puzzle.add_thermometer([(1, 1), (2, 1), (2, 2)])
    puzzle.add_thermometer([(1, 3), (1, 4), (2, 4)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2)])

    return puzzle
