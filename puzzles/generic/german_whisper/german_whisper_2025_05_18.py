"""PuzzleMadness German Whispers Sudoku — 2025-05-18."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-18'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/18'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 2, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 5), (1, 5), (0, 5), (0, 6), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (7, 5), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (2, 1), (2, 2), (3, 2)])
    puzzle.add_german_whispers([(2, 6), (3, 7), (3, 8), (2, 8), (1, 8)])
    puzzle.add_german_whispers([(6, 2), (6, 3), (5, 3), (4, 4), (5, 4)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (7, 1), (8, 1)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (1, 3), (1, 2)])
    puzzle.add_german_whispers([(5, 7), (4, 7), (5, 8), (4, 8)])
    puzzle.add_german_whispers([(8, 5), (7, 6), (6, 7)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(5, 5), (4, 5), (3, 6)])

    return puzzle
