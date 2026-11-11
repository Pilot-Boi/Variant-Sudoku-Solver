"""PuzzleMadness German Whispers Sudoku — 2025-09-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 0, 0, 0, 8, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 2), (5, 3), (6, 4), (6, 5), (5, 6), (4, 6)])
    puzzle.add_german_whispers([(0, 6), (0, 5), (0, 4), (1, 4), (2, 4)])
    puzzle.add_german_whispers([(2, 1), (2, 0), (1, 1), (1, 2), (2, 2)])
    puzzle.add_german_whispers([(1, 8), (2, 7), (3, 6), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (7, 8), (7, 7), (8, 6)])
    puzzle.add_german_whispers([(4, 1), (3, 0), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(7, 2), (6, 1), (7, 1), (8, 1)])
    puzzle.add_german_whispers([(3, 2), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(4, 5), (5, 4), (5, 5)])
    puzzle.add_german_whispers([(5, 2), (5, 1), (6, 0)])

    return puzzle
