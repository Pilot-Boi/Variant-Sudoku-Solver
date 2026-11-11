"""PuzzleMadness Thermometer Sudoku — 2025-03-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-03-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/3/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [4, 0, 0, 6, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(3, 6), (4, 6), (4, 5), (3, 5), (3, 4), (3, 3)])
    puzzle.add_thermometer([(0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (2, 6)])
    puzzle.add_thermometer([(6, 1), (5, 1), (5, 2), (5, 3), (6, 3)])
    puzzle.add_thermometer([(8, 7), (7, 7), (6, 7), (5, 7), (4, 7)])
    puzzle.add_thermometer([(2, 1), (1, 1), (0, 1), (0, 2), (1, 2)])
    puzzle.add_thermometer([(7, 2), (7, 3), (8, 3), (8, 4)])
    puzzle.add_thermometer([(7, 4), (6, 4), (6, 5), (7, 5)])
    puzzle.add_thermometer([(3, 2), (2, 2), (2, 3), (2, 4)])
    puzzle.add_thermometer([(8, 5), (8, 6), (7, 6), (6, 6)])
    puzzle.add_thermometer([(5, 0), (6, 0), (7, 0)])
    puzzle.add_thermometer([(1, 7), (0, 7), (0, 8)])
    puzzle.add_thermometer([(4, 4), (4, 3), (4, 2)])
    puzzle.add_thermometer([(3, 0), (2, 0), (1, 0)])
    puzzle.add_thermometer([(6, 8), (7, 8), (8, 8)])

    return puzzle
