"""PuzzleMadness Thermometer Sudoku — 2026-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(6, 6), (5, 6), (5, 5), (4, 5), (3, 5), (3, 6)])
    puzzle.add_thermometer([(3, 0), (4, 0), (5, 0), (5, 1), (4, 1)])
    puzzle.add_thermometer([(3, 8), (3, 7), (4, 7), (5, 7), (6, 7)])
    puzzle.add_thermometer([(1, 5), (2, 5), (2, 6), (2, 7), (2, 8)])
    puzzle.add_thermometer([(7, 5), (7, 4), (6, 4), (6, 3), (7, 3)])
    puzzle.add_thermometer([(5, 8), (6, 8), (7, 8), (8, 8)])
    puzzle.add_thermometer([(6, 1), (6, 2), (7, 2), (8, 2)])
    puzzle.add_thermometer([(1, 7), (1, 6), (0, 6), (0, 5)])
    puzzle.add_thermometer([(7, 7), (8, 7), (8, 6), (7, 6)])
    puzzle.add_thermometer([(4, 3), (3, 3), (2, 3), (1, 3)])
    puzzle.add_thermometer([(2, 2), (2, 1), (3, 1), (3, 2)])
    puzzle.add_thermometer([(5, 3), (5, 4), (4, 4)])
    puzzle.add_thermometer([(0, 2), (0, 1), (0, 0)])

    return puzzle
