"""PuzzleMadness German Whispers Sudoku — 2025-09-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 4, 0, 0, 0, 6, 0],
        [5, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (3, 1), (3, 0), (2, 0), (1, 1), (1, 2)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (2, 7), (3, 7), (4, 6)])
    puzzle.add_german_whispers([(4, 5), (5, 4), (6, 3), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(7, 8), (6, 7), (5, 7), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(1, 5), (1, 4), (2, 3), (1, 3), (0, 4)])
    puzzle.add_german_whispers([(3, 4), (3, 5), (3, 6), (2, 5)])
    puzzle.add_german_whispers([(7, 4), (6, 5), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(4, 4), (5, 3), (5, 2), (4, 2)])
    puzzle.add_german_whispers([(5, 1), (4, 0), (5, 0)])

    return puzzle
