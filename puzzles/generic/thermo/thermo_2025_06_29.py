"""PuzzleMadness Thermometer Sudoku — 2025-06-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-06-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/6/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(0, 1), (0, 0), (1, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_thermometer([(8, 1), (8, 2), (7, 2), (7, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(1, 7), (1, 6), (2, 6), (2, 7), (3, 7)])
    puzzle.add_thermometer([(4, 6), (3, 6), (3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(6, 5), (7, 5), (8, 5), (8, 6), (7, 6)])
    puzzle.add_thermometer([(5, 3), (6, 3), (6, 4), (7, 4), (7, 3)])
    puzzle.add_thermometer([(3, 2), (4, 2), (5, 2), (5, 1)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0)])
    puzzle.add_thermometer([(8, 8), (7, 8), (6, 8)])
    puzzle.add_thermometer([(5, 5), (5, 6), (5, 7)])
    puzzle.add_thermometer([(2, 8), (3, 8), (4, 8)])
    puzzle.add_thermometer([(2, 4), (2, 3), (1, 3)])

    return puzzle
