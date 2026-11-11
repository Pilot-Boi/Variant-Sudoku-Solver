"""PuzzleMadness Thermometer Sudoku — 2025-10-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(5, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1)])
    puzzle.add_thermometer([(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5)])
    puzzle.add_thermometer([(7, 6), (6, 6), (6, 7), (5, 7), (5, 6)])
    puzzle.add_thermometer([(2, 2), (1, 2), (1, 1), (1, 0), (2, 0)])
    puzzle.add_thermometer([(6, 3), (6, 4), (5, 4), (5, 5), (4, 5)])
    puzzle.add_thermometer([(7, 1), (7, 0), (6, 0), (6, 1), (5, 1)])
    puzzle.add_thermometer([(3, 8), (2, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(0, 5), (1, 5), (2, 5)])
    puzzle.add_thermometer([(4, 4), (4, 3), (5, 3)])
    puzzle.add_thermometer([(4, 7), (4, 6), (3, 6)])
    puzzle.add_thermometer([(1, 6), (2, 6), (2, 7)])
    puzzle.add_thermometer([(0, 8), (0, 7), (0, 6)])
    puzzle.add_thermometer([(0, 1), (0, 2), (0, 3)])
    puzzle.add_thermometer([(7, 3), (7, 2), (6, 2)])

    return puzzle
