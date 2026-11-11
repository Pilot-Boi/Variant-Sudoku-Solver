"""PuzzleMadness German Whispers Sudoku — 2025-04-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 3, 1, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 4, 0, 6, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 7), (5, 6), (4, 5), (5, 5), (5, 4), (4, 3)])
    puzzle.add_german_whispers([(2, 5), (1, 4), (1, 5), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(3, 0), (4, 0), (5, 0), (6, 0), (7, 1)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 3), (6, 3), (7, 2)])
    puzzle.add_german_whispers([(6, 4), (6, 5), (7, 6), (6, 6)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (2, 1), (2, 2)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(1, 1), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(3, 7), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(4, 1), (4, 2), (5, 3)])

    return puzzle
