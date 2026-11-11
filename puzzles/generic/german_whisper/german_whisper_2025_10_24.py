"""PuzzleMadness German Whispers Sudoku — 2025-10-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 8, 0, 0, 2, 0],
        [4, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 2, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 7), (1, 6), (2, 6), (3, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(3, 5), (4, 4), (5, 4), (5, 3), (6, 3)])
    puzzle.add_german_whispers([(8, 2), (7, 2), (7, 3), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (2, 0), (3, 1), (4, 0)])
    puzzle.add_german_whispers([(6, 6), (6, 7), (7, 6), (7, 7)])
    puzzle.add_german_whispers([(0, 5), (0, 4), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(3, 2), (2, 2), (1, 2), (2, 3)])
    puzzle.add_german_whispers([(6, 2), (6, 1), (5, 1), (4, 2)])
    puzzle.add_german_whispers([(5, 5), (4, 6), (4, 7)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (7, 0)])

    return puzzle
