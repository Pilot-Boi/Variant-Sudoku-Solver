"""PuzzleMadness Thermometer Sudoku — 2026-10-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 5), (6, 6), (6, 7), (5, 7), (5, 8), (6, 8)])
    puzzle.add_thermometer([(3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 1)])
    puzzle.add_thermometer([(2, 7), (3, 7), (3, 8), (2, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(4, 6), (3, 6), (2, 6), (1, 6), (1, 5), (2, 5)])
    puzzle.add_thermometer([(8, 1), (7, 1), (6, 1), (5, 1), (5, 0)])
    puzzle.add_thermometer([(6, 3), (5, 3), (5, 4), (4, 4), (3, 4)])
    puzzle.add_thermometer([(1, 2), (1, 1), (1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(7, 4), (8, 4), (8, 3), (7, 3)])
    puzzle.add_thermometer([(2, 4), (2, 3), (3, 3), (4, 3)])
    puzzle.add_thermometer([(7, 8), (8, 8), (8, 7), (8, 6)])
    puzzle.add_thermometer([(0, 2), (0, 3), (1, 3)])
    puzzle.add_thermometer([(5, 5), (4, 5), (3, 5)])

    return puzzle
