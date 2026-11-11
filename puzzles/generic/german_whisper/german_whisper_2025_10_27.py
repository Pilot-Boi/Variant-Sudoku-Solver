"""PuzzleMadness German Whispers Sudoku — 2025-10-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 4, 5, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 1, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 1), (1, 0), (1, 1), (2, 2), (2, 3), (1, 3)])
    puzzle.add_german_whispers([(5, 6), (6, 6), (7, 5), (6, 4), (5, 4)])
    puzzle.add_german_whispers([(4, 1), (4, 2), (5, 2), (5, 3), (4, 3)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (2, 8), (3, 8), (3, 7)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(4, 4), (5, 5), (4, 6), (3, 6)])
    puzzle.add_german_whispers([(5, 7), (6, 7), (5, 8)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (1, 5)])
    puzzle.add_german_whispers([(0, 4), (0, 3), (1, 4)])
    puzzle.add_german_whispers([(4, 5), (3, 4), (3, 5)])

    return puzzle
