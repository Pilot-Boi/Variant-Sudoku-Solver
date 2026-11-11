"""PuzzleMadness Thermometer Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 6, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7), (5, 7), (4, 7), (3, 7)])
    puzzle.add_thermometer([(4, 2), (5, 2), (5, 1), (5, 0), (4, 0)])
    puzzle.add_thermometer([(0, 3), (1, 3), (2, 3), (2, 2), (3, 2)])
    puzzle.add_thermometer([(8, 4), (8, 5), (7, 5), (6, 5), (6, 6)])
    puzzle.add_thermometer([(6, 2), (7, 2), (7, 3), (7, 4)])
    puzzle.add_thermometer([(3, 1), (2, 1), (1, 1), (0, 1)])
    puzzle.add_thermometer([(4, 4), (5, 4), (5, 3)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(2, 4), (3, 4), (3, 3)])
    puzzle.add_thermometer([(7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8)])

    return puzzle
