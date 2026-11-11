"""PuzzleMadness Thermometer Sudoku — 2025-09-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-09-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/9/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 8, 0, 0, 0, 7, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 4],
        [2, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(2, 4), (2, 3), (2, 2), (1, 2), (1, 3)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)])
    puzzle.add_thermometer([(8, 1), (8, 2), (8, 3), (8, 4), (7, 4)])
    puzzle.add_thermometer([(7, 5), (6, 5), (6, 6), (6, 7)])
    puzzle.add_thermometer([(1, 6), (1, 5), (0, 5), (0, 4)])
    puzzle.add_thermometer([(3, 6), (3, 7), (3, 8), (2, 8)])
    puzzle.add_thermometer([(5, 0), (5, 1), (6, 1), (6, 0)])
    puzzle.add_thermometer([(4, 7), (5, 7), (5, 6)])
    puzzle.add_thermometer([(8, 0), (7, 0), (7, 1)])
    puzzle.add_thermometer([(4, 4), (3, 4), (3, 3)])
    puzzle.add_thermometer([(3, 5), (2, 5), (2, 6)])

    return puzzle
