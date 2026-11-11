"""PuzzleMadness Thermometer Sudoku — 2025-03-07."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-07'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/7'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 7, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 3), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4)])
    puzzle.add_thermometer([(2, 5), (3, 5), (3, 6), (3, 7), (3, 8), (2, 8)])
    puzzle.add_thermometer([(6, 2), (6, 1), (7, 1), (8, 1), (8, 2), (7, 2)])
    puzzle.add_thermometer([(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_thermometer([(7, 6), (7, 7), (6, 7), (5, 7), (4, 7)])
    puzzle.add_thermometer([(7, 4), (6, 4), (5, 4), (5, 5)])
    puzzle.add_thermometer([(0, 7), (1, 7), (1, 6), (2, 6)])
    puzzle.add_thermometer([(1, 4), (1, 3), (0, 3)])
    puzzle.add_thermometer([(5, 3), (6, 3), (7, 3)])
    puzzle.add_thermometer([(4, 0), (3, 0), (2, 0)])
    puzzle.add_thermometer([(5, 1), (4, 1), (3, 1)])
    puzzle.add_thermometer([(8, 5), (8, 6), (8, 7)])
    puzzle.add_thermometer([(4, 6), (5, 6), (6, 6)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8)])

    return puzzle
