"""PuzzleMadness German Whispers Sudoku — 2025-11-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 4, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [1, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 2), (3, 2), (3, 3), (2, 2), (1, 2), (0, 3)])
    puzzle.add_german_whispers([(0, 1), (0, 0), (1, 0), (1, 1), (0, 2)])
    puzzle.add_german_whispers([(4, 8), (3, 7), (3, 8), (2, 8), (2, 7)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (4, 6), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (8, 2), (7, 1), (6, 0)])
    puzzle.add_german_whispers([(6, 6), (7, 6), (8, 6), (7, 7)])
    puzzle.add_german_whispers([(4, 0), (5, 0), (6, 1), (5, 2)])
    puzzle.add_german_whispers([(1, 7), (0, 8), (1, 8)])
    puzzle.add_german_whispers([(5, 3), (4, 3), (4, 4)])
    puzzle.add_german_whispers([(1, 4), (2, 4), (2, 3)])

    return puzzle
