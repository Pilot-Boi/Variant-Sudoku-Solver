"""PuzzleMadness German Whispers Sudoku — 2025-11-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 9],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 6, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [8, 0, 0, 7, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 7), (3, 6), (3, 5), (4, 5), (5, 5), (6, 4)])
    puzzle.add_german_whispers([(4, 4), (3, 3), (2, 2), (1, 1), (0, 1)])
    puzzle.add_german_whispers([(4, 1), (5, 1), (6, 2), (7, 3), (7, 2)])
    puzzle.add_german_whispers([(1, 4), (1, 5), (2, 5), (2, 4), (2, 3)])
    puzzle.add_german_whispers([(6, 5), (7, 4), (7, 5), (8, 6)])
    puzzle.add_german_whispers([(5, 8), (4, 8), (3, 7), (4, 7)])
    puzzle.add_german_whispers([(1, 2), (1, 3), (0, 4)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (4, 2)])
    puzzle.add_german_whispers([(3, 1), (4, 0), (5, 0)])

    return puzzle
