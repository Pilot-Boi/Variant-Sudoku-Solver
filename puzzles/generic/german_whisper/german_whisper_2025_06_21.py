"""PuzzleMadness German Whispers Sudoku — 2025-06-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 6, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 2), (6, 3), (7, 2), (8, 2), (8, 3), (7, 3)])
    puzzle.add_german_whispers([(3, 3), (4, 3), (4, 4), (5, 5), (5, 4)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (4, 8), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (1, 0), (2, 1), (3, 2)])
    puzzle.add_german_whispers([(6, 6), (7, 7), (7, 6), (8, 6), (8, 5)])
    puzzle.add_german_whispers([(1, 4), (1, 5), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 0), (7, 1)])
    puzzle.add_german_whispers([(1, 7), (2, 8), (2, 7), (3, 7)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(1, 3), (1, 2), (2, 2)])

    return puzzle
