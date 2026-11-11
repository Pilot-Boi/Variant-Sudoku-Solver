"""PuzzleMadness German Whispers Sudoku — 2025-01-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 3],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 0), (7, 1), (8, 2), (7, 2), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (6, 5), (7, 4), (6, 4)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (2, 0), (2, 1), (2, 2)])
    puzzle.add_german_whispers([(6, 6), (5, 7), (4, 6), (4, 7), (4, 8)])
    puzzle.add_german_whispers([(2, 5), (1, 4), (0, 5), (1, 5), (0, 6)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (1, 2), (0, 2)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (2, 7), (3, 7)])
    puzzle.add_german_whispers([(7, 6), (6, 7), (6, 8), (5, 8)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(3, 5), (4, 5), (3, 4)])

    return puzzle
