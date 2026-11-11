"""PuzzleMadness German Whispers Sudoku — 2025-09-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 9, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 5, 0, 1, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 4, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 0), (7, 1), (6, 2), (5, 3), (4, 3), (3, 2)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (7, 4), (8, 5), (7, 6)])
    puzzle.add_german_whispers([(3, 6), (4, 6), (3, 7), (4, 8), (4, 7)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (1, 1), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(1, 6), (1, 7), (0, 8), (1, 8), (2, 7)])
    puzzle.add_german_whispers([(1, 5), (2, 4), (2, 5), (3, 5)])
    puzzle.add_german_whispers([(6, 6), (5, 7), (6, 7)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (3, 0)])

    return puzzle
