"""PuzzleMadness German Whispers Sudoku — 2025-05-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 3, 0, 9, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 4), (5, 5), (6, 6), (5, 6), (5, 7), (4, 7)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (6, 1), (5, 1), (5, 0)])
    puzzle.add_german_whispers([(1, 1), (1, 0), (2, 1), (3, 2), (3, 3)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (7, 2), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(4, 4), (4, 5), (3, 5), (2, 4)])
    puzzle.add_german_whispers([(1, 5), (0, 6), (0, 7), (1, 6)])
    puzzle.add_german_whispers([(3, 7), (4, 8), (3, 8), (2, 7)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (8, 8)])

    return puzzle
