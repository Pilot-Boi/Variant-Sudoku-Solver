"""PuzzleMadness German Whispers Sudoku — 2025-12-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 9, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [7, 4, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 6), (7, 5), (6, 4), (5, 3), (6, 2), (7, 2)])
    puzzle.add_german_whispers([(0, 5), (1, 6), (1, 5), (2, 5), (3, 6)])
    puzzle.add_german_whispers([(3, 3), (4, 3), (3, 2), (2, 1), (3, 1)])
    puzzle.add_german_whispers([(8, 7), (7, 8), (6, 8), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(6, 5), (5, 5), (4, 6), (3, 7)])
    puzzle.add_german_whispers([(6, 1), (6, 0), (5, 0), (5, 1)])
    puzzle.add_german_whispers([(8, 4), (8, 3), (8, 2), (8, 1)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (0, 0)])

    return puzzle
