"""PuzzleMadness Thermometer Sudoku — 2025-05-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [8, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 0), (6, 1), (7, 1), (8, 1), (8, 2)])
    puzzle.add_thermometer([(7, 5), (6, 5), (5, 5), (5, 6), (6, 6)])
    puzzle.add_thermometer([(2, 8), (1, 8), (1, 7), (0, 7), (0, 6)])
    puzzle.add_thermometer([(5, 7), (6, 7), (7, 7), (7, 8), (6, 8)])
    puzzle.add_thermometer([(3, 3), (3, 4), (2, 4), (2, 3), (1, 3)])
    puzzle.add_thermometer([(0, 1), (1, 1), (1, 0), (2, 0), (2, 1)])
    puzzle.add_thermometer([(2, 6), (2, 5), (3, 5), (4, 5), (4, 4)])
    puzzle.add_thermometer([(4, 2), (4, 1), (5, 1), (5, 2)])
    puzzle.add_thermometer([(4, 6), (4, 7), (4, 8), (5, 8)])
    puzzle.add_thermometer([(5, 4), (6, 4), (7, 4)])
    puzzle.add_thermometer([(3, 2), (2, 2), (1, 2)])
    puzzle.add_thermometer([(7, 2), (7, 3), (6, 3)])
    puzzle.add_thermometer([(4, 0), (3, 0), (3, 1)])
    puzzle.add_thermometer([(8, 3), (8, 4), (8, 5)])

    return puzzle
