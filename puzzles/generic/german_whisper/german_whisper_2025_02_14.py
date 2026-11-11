"""PuzzleMadness German Whispers Sudoku — 2025-02-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 9, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 8, 0, 6, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 4), (5, 4), (6, 5), (7, 4), (7, 5), (6, 6)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (5, 1), (4, 1), (5, 2)])
    puzzle.add_german_whispers([(7, 6), (7, 7), (6, 8), (5, 7), (4, 7)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (2, 1), (1, 2), (1, 1)])
    puzzle.add_german_whispers([(4, 8), (3, 8), (3, 7), (2, 6), (1, 6)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (0, 4), (1, 5)])
    puzzle.add_german_whispers([(4, 3), (3, 4), (4, 5), (3, 5)])
    puzzle.add_german_whispers([(2, 8), (1, 8), (0, 8), (1, 7)])
    puzzle.add_german_whispers([(0, 3), (1, 3), (2, 3)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(7, 3), (8, 3), (7, 2)])

    return puzzle
