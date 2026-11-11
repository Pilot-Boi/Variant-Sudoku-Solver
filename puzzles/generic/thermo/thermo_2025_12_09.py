"""PuzzleMadness Thermometer Sudoku — 2025-12-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 5, 0, 0, 3, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 2), (5, 2), (6, 2), (7, 2), (8, 2)])
    puzzle.add_thermometer([(5, 3), (4, 3), (4, 4), (5, 4), (6, 4)])
    puzzle.add_thermometer([(0, 7), (1, 7), (2, 7), (2, 6), (2, 5)])
    puzzle.add_thermometer([(5, 5), (5, 6), (4, 6), (4, 7), (3, 7)])
    puzzle.add_thermometer([(6, 6), (6, 7), (6, 8), (5, 8), (5, 7)])
    puzzle.add_thermometer([(7, 5), (7, 4), (8, 4), (8, 5), (8, 6)])
    puzzle.add_thermometer([(4, 1), (5, 1), (5, 0), (4, 0)])
    puzzle.add_thermometer([(8, 0), (8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(0, 2), (0, 1), (1, 1), (1, 2)])
    puzzle.add_thermometer([(3, 2), (3, 3), (3, 4)])
    puzzle.add_thermometer([(0, 5), (0, 4), (0, 3)])
    puzzle.add_thermometer([(3, 6), (3, 5), (4, 5)])
    puzzle.add_thermometer([(0, 0), (1, 0), (2, 0)])

    return puzzle
