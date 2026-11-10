"""PuzzleMadness Thermometer Sudoku — 2026-10-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2026-10-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2026/10/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 5],
        [8, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 0), (3, 0), (3, 1), (3, 2), (4, 2), (4, 1)])
    puzzle.add_thermometer([(0, 6), (1, 6), (1, 7), (1, 8), (2, 8), (2, 7)])
    puzzle.add_thermometer([(4, 5), (4, 4), (5, 4), (5, 5), (5, 6), (6, 6)])
    puzzle.add_thermometer([(5, 7), (4, 7), (4, 6), (3, 6), (3, 5)])
    puzzle.add_thermometer([(7, 5), (7, 6), (8, 6), (8, 7), (7, 7)])
    puzzle.add_thermometer([(2, 4), (1, 4), (0, 4), (0, 3), (1, 3)])
    puzzle.add_thermometer([(7, 2), (7, 3), (6, 3), (6, 2), (5, 2)])
    puzzle.add_thermometer([(5, 1), (5, 0), (6, 0), (7, 0)])
    puzzle.add_thermometer([(1, 0), (0, 0), (0, 1)])
    puzzle.add_thermometer([(6, 8), (5, 8), (4, 8)])
    puzzle.add_thermometer([(3, 3), (4, 3), (5, 3)])
    puzzle.add_thermometer([(2, 6), (2, 5), (1, 5)])

    return puzzle
