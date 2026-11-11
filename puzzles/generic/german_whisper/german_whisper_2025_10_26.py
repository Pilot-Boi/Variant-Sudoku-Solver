"""PuzzleMadness German Whispers Sudoku — 2025-10-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 2, 5, 0, 0, 0, 0],
        [8, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 8), (2, 7), (3, 7), (4, 6)])
    puzzle.add_german_whispers([(6, 4), (7, 3), (7, 4), (8, 3), (8, 4)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (1, 4), (0, 5), (1, 6)])
    puzzle.add_german_whispers([(5, 3), (4, 4), (4, 3), (5, 2), (6, 1)])
    puzzle.add_german_whispers([(5, 6), (6, 6), (5, 7), (4, 7)])
    puzzle.add_german_whispers([(4, 5), (3, 6), (2, 5), (1, 5)])
    puzzle.add_german_whispers([(7, 6), (6, 7), (7, 7), (8, 8)])
    puzzle.add_german_whispers([(1, 2), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(4, 2), (5, 1), (4, 0)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0)])

    return puzzle
