"""PuzzleMadness German Whispers Sudoku — 2025-08-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 7), (1, 7), (1, 6), (2, 6), (3, 5), (4, 5)])
    puzzle.add_german_whispers([(1, 1), (0, 0), (0, 1), (0, 2), (1, 2)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 2), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(4, 3), (4, 4), (5, 5), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (4, 8), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(7, 8), (7, 7), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(1, 5), (0, 5), (1, 4), (2, 3)])
    puzzle.add_german_whispers([(7, 1), (8, 0), (7, 0)])
    puzzle.add_german_whispers([(4, 0), (3, 1), (2, 0)])

    return puzzle
