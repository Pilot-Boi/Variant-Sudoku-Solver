"""PuzzleMadness Thermometer Sudoku — 2025-11-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-11-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/11/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 2), (7, 2), (8, 2), (8, 1), (7, 1), (6, 1)])
    puzzle.add_thermometer([(1, 6), (2, 6), (2, 7), (3, 7), (3, 6)])
    puzzle.add_thermometer([(4, 5), (5, 5), (5, 4), (4, 4), (4, 3)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(4, 0), (4, 1), (4, 2), (3, 2), (2, 2)])
    puzzle.add_thermometer([(7, 4), (6, 4), (6, 5), (6, 6)])
    puzzle.add_thermometer([(2, 3), (2, 4), (1, 4), (1, 5)])
    puzzle.add_thermometer([(6, 0), (5, 0), (5, 1), (5, 2)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 8)])
    puzzle.add_thermometer([(5, 6), (4, 6), (4, 7)])
    puzzle.add_thermometer([(3, 1), (2, 1), (2, 0)])

    return puzzle
