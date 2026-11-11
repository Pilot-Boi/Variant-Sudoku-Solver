"""PuzzleMadness German Whispers Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 5, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 3), (7, 3), (7, 2), (6, 1), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(3, 5), (2, 5), (1, 5), (1, 4), (0, 4)])
    puzzle.add_german_whispers([(4, 4), (4, 5), (3, 6), (2, 7), (2, 8)])
    puzzle.add_german_whispers([(1, 3), (0, 2), (1, 1), (2, 2), (3, 1)])
    puzzle.add_german_whispers([(7, 5), (6, 5), (5, 6), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(6, 2), (5, 1), (4, 1), (4, 0)])
    puzzle.add_german_whispers([(6, 6), (7, 6), (8, 7), (8, 8)])
    puzzle.add_german_whispers([(1, 8), (0, 8), (0, 7), (1, 6)])
    puzzle.add_german_whispers([(3, 4), (3, 3), (2, 3)])

    return puzzle
