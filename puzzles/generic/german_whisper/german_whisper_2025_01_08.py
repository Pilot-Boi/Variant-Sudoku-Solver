"""PuzzleMadness German Whispers Sudoku — 2025-01-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 3), (6, 3), (6, 4), (7, 4)])
    puzzle.add_german_whispers([(2, 5), (2, 6), (1, 7), (0, 7), (0, 6)])
    puzzle.add_german_whispers([(7, 6), (8, 7), (7, 7), (6, 8), (5, 8)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)])
    puzzle.add_german_whispers([(4, 5), (4, 4), (4, 3), (3, 4)])
    puzzle.add_german_whispers([(5, 0), (5, 1), (4, 2), (3, 3)])
    puzzle.add_german_whispers([(4, 8), (3, 8), (3, 7), (2, 8)])
    puzzle.add_german_whispers([(4, 1), (3, 2), (3, 1)])
    puzzle.add_german_whispers([(0, 3), (1, 2), (2, 3)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (8, 0)])

    return puzzle
