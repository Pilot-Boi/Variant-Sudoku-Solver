"""PuzzleMadness German Whispers Sudoku — 2025-06-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 0), (2, 1), (1, 2), (2, 3), (1, 3), (0, 2)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (3, 6), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (4, 2), (5, 2), (6, 2)])
    puzzle.add_german_whispers([(8, 3), (7, 3), (7, 4), (6, 5), (6, 4)])
    puzzle.add_german_whispers([(3, 4), (2, 4), (1, 5), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (8, 1), (8, 0)])
    puzzle.add_german_whispers([(4, 5), (5, 6), (5, 7), (6, 7)])
    puzzle.add_german_whispers([(7, 6), (8, 5), (8, 6), (8, 7)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 7), (1, 7)])
    puzzle.add_german_whispers([(3, 2), (3, 3), (4, 4)])

    return puzzle
