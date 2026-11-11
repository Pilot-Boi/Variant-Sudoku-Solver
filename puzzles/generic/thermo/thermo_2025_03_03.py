"""PuzzleMadness Thermometer Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 3), (5, 3), (5, 4), (6, 4), (6, 5), (5, 5)])
    puzzle.add_thermometer([(0, 6), (0, 7), (1, 7), (2, 7), (2, 8)])
    puzzle.add_thermometer([(7, 2), (6, 2), (6, 1), (7, 1), (7, 0)])
    puzzle.add_thermometer([(3, 1), (3, 0), (2, 0), (2, 1), (1, 1)])
    puzzle.add_thermometer([(3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_thermometer([(4, 5), (4, 4), (4, 3), (4, 2)])
    puzzle.add_thermometer([(2, 6), (2, 5), (2, 4), (3, 4)])
    puzzle.add_thermometer([(7, 4), (7, 5), (7, 6), (8, 6)])
    puzzle.add_thermometer([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2)])
    puzzle.add_thermometer([(6, 0), (5, 0), (4, 0)])
    puzzle.add_thermometer([(3, 8), (4, 8), (5, 8)])
    puzzle.add_thermometer([(2, 3), (3, 3), (3, 2)])
    puzzle.add_thermometer([(5, 6), (4, 6), (3, 6)])

    return puzzle
