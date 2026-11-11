"""PuzzleMadness Thermometer Sudoku — 2025-10-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Thermometer Sudoku — 2025-10-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/thermosudoku/hard/2025/10/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 2, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_thermometer([(4, 6), (4, 5), (4, 4), (5, 4), (5, 5), (6, 5)])
    puzzle.add_thermometer([(6, 3), (7, 3), (8, 3), (8, 4), (7, 4), (7, 5)])
    puzzle.add_thermometer([(5, 8), (5, 7), (6, 7), (6, 6), (5, 6)])
    puzzle.add_thermometer([(2, 0), (3, 0), (4, 0), (4, 1), (5, 1)])
    puzzle.add_thermometer([(5, 0), (6, 0), (6, 1), (7, 1), (7, 0)])
    puzzle.add_thermometer([(2, 7), (2, 6), (2, 5), (2, 4), (2, 3)])
    puzzle.add_thermometer([(0, 7), (0, 8), (1, 8), (1, 7)])
    puzzle.add_thermometer([(3, 3), (3, 2), (4, 2), (4, 3)])
    puzzle.add_thermometer([(1, 1), (0, 1), (0, 0), (1, 0)])
    puzzle.add_thermometer([(7, 8), (7, 7), (8, 7)])
    puzzle.add_thermometer([(0, 4), (0, 3), (0, 2)])
    puzzle.add_thermometer([(3, 5), (3, 6), (3, 7)])
    puzzle.add_thermometer([(1, 5), (0, 5), (0, 6)])
    puzzle.add_thermometer([(2, 2), (2, 1), (3, 1)])

    return puzzle
