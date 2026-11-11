"""PuzzleMadness German Whispers Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 6],
        [0, 0, 8, 4, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 4, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 7), (4, 6), (5, 5), (5, 4), (6, 4), (6, 3)])
    puzzle.add_german_whispers([(2, 7), (3, 6), (4, 5), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (1, 2), (2, 1), (1, 1)])
    puzzle.add_german_whispers([(8, 6), (7, 6), (7, 7), (6, 8), (5, 8)])
    puzzle.add_german_whispers([(5, 3), (6, 2), (5, 2), (6, 1), (6, 0)])
    puzzle.add_german_whispers([(3, 1), (4, 0), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(7, 3), (8, 3), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(2, 8), (3, 8), (4, 8), (4, 7)])

    return puzzle
