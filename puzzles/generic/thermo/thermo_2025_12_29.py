"""PuzzleMadness Thermometer Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 6, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 3), (3, 3), (3, 2), (4, 2), (4, 3), (4, 4)])
    puzzle.add_thermometer([(6, 4), (6, 5), (6, 6), (6, 7), (7, 7), (7, 8)])
    puzzle.add_thermometer([(5, 1), (6, 1), (7, 1), (7, 0), (6, 0)])
    puzzle.add_thermometer([(4, 5), (5, 5), (5, 4), (5, 3), (5, 2)])
    puzzle.add_thermometer([(4, 7), (4, 8), (3, 8), (3, 7), (2, 7)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 6), (0, 5)])
    puzzle.add_thermometer([(7, 4), (7, 3), (8, 3), (8, 2)])
    puzzle.add_thermometer([(8, 7), (8, 6), (8, 5)])
    puzzle.add_thermometer([(1, 0), (2, 0), (2, 1)])
    puzzle.add_thermometer([(2, 5), (2, 4), (1, 4)])
    puzzle.add_thermometer([(3, 6), (4, 6), (5, 6)])
    puzzle.add_thermometer([(7, 2), (6, 2), (6, 3)])

    return puzzle
