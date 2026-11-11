"""PuzzleMadness German Whispers Sudoku — 2025-02-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 3, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 5, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 5), (1, 4), (2, 5), (3, 4), (3, 5), (4, 5)])
    puzzle.add_german_whispers([(7, 4), (8, 3), (8, 4), (7, 5), (6, 4)])
    puzzle.add_german_whispers([(6, 3), (5, 3), (4, 4), (3, 3), (4, 2)])
    puzzle.add_german_whispers([(4, 1), (4, 0), (3, 1), (2, 1), (2, 2)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (5, 7), (4, 6)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 0), (7, 1)])
    puzzle.add_german_whispers([(1, 8), (2, 8), (3, 8)])
    puzzle.add_german_whispers([(1, 6), (1, 5), (0, 6)])

    return puzzle
