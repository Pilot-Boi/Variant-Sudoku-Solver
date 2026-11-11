"""PuzzleMadness German Whispers Sudoku — 2025-02-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [6, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 3, 0, 0, 0, 0],
        [2, 0, 5, 0, 0, 8, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 1), (7, 1), (7, 2), (6, 3), (6, 4), (7, 3)])
    puzzle.add_german_whispers([(3, 3), (3, 2), (4, 2), (5, 2), (5, 1)])
    puzzle.add_german_whispers([(5, 5), (6, 6), (6, 7), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(4, 6), (3, 6), (3, 5), (2, 5), (1, 6)])
    puzzle.add_german_whispers([(2, 6), (2, 7), (2, 8), (1, 8)])
    puzzle.add_german_whispers([(1, 1), (0, 0), (1, 0), (2, 1)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(1, 5), (0, 4), (0, 3)])
    puzzle.add_german_whispers([(3, 4), (4, 4), (5, 3)])
    puzzle.add_german_whispers([(2, 3), (1, 2), (1, 3)])

    return puzzle
