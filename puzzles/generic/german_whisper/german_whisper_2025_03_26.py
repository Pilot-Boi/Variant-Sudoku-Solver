"""PuzzleMadness German Whispers Sudoku — 2025-03-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 6, 0, 0, 0, 9],
        [0, 0, 0, 0, 2, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 7), (6, 8), (5, 7), (4, 7), (3, 6), (2, 7)])
    puzzle.add_german_whispers([(3, 0), (2, 1), (2, 0), (1, 0), (0, 0)])
    puzzle.add_german_whispers([(6, 6), (7, 5), (8, 5), (7, 4), (7, 3)])
    puzzle.add_german_whispers([(1, 6), (1, 5), (1, 4), (0, 3), (1, 2)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (7, 2), (6, 3)])
    puzzle.add_german_whispers([(5, 6), (5, 5), (5, 4), (4, 4)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(5, 2), (4, 2), (4, 1), (5, 1)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (6, 1)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (1, 7)])
    puzzle.add_german_whispers([(3, 1), (3, 2), (2, 2)])

    return puzzle
