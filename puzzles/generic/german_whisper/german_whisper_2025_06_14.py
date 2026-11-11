"""PuzzleMadness German Whispers Sudoku — 2025-06-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 9, 3, 0],
        [0, 0, 8, 4, 0, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 9, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 1), (5, 1), (4, 1), (3, 2), (4, 2), (4, 3)])
    puzzle.add_german_whispers([(4, 6), (3, 5), (3, 6), (2, 7), (1, 6)])
    puzzle.add_german_whispers([(7, 4), (8, 3), (7, 3), (7, 2), (8, 1)])
    puzzle.add_german_whispers([(6, 7), (5, 8), (5, 7), (6, 6), (5, 5)])
    puzzle.add_german_whispers([(2, 3), (3, 4), (3, 3), (2, 2)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (7, 8), (7, 7)])
    puzzle.add_german_whispers([(0, 3), (1, 4), (0, 5), (1, 5)])
    puzzle.add_german_whispers([(1, 1), (1, 0), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(6, 5), (7, 5), (6, 4)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 8)])

    return puzzle
