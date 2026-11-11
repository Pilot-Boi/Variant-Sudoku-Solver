"""PuzzleMadness German Whispers Sudoku — 2025-03-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 5, 0],
        [0, 0, 0, 7, 0, 0, 0, 1, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (1, 5), (1, 6), (2, 7), (2, 6), (3, 6)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (5, 8), (4, 7), (5, 6)])
    puzzle.add_german_whispers([(3, 0), (2, 1), (1, 1), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(3, 5), (4, 4), (5, 4), (5, 3), (6, 4)])
    puzzle.add_german_whispers([(8, 1), (8, 0), (7, 1), (6, 0), (6, 1)])
    puzzle.add_german_whispers([(2, 3), (2, 2), (1, 3), (0, 4)])
    puzzle.add_german_whispers([(7, 8), (8, 7), (7, 6), (8, 6)])
    puzzle.add_german_whispers([(8, 3), (7, 3), (6, 3), (5, 2)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (4, 6)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 8)])

    return puzzle
