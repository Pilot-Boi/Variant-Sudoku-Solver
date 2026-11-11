"""PuzzleMadness German Whispers Sudoku — 2025-09-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 4, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 1), (5, 2), (4, 1), (3, 0), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(6, 4), (5, 4), (4, 5), (3, 6), (3, 7)])
    puzzle.add_german_whispers([(7, 6), (8, 6), (8, 7), (7, 7), (7, 8)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 8), (2, 7), (2, 6)])
    puzzle.add_german_whispers([(1, 1), (0, 2), (1, 3), (2, 3)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (7, 2), (8, 3)])
    puzzle.add_german_whispers([(2, 4), (3, 5), (2, 5), (1, 4)])
    puzzle.add_german_whispers([(4, 6), (4, 7), (5, 6), (5, 7)])
    puzzle.add_german_whispers([(6, 3), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(0, 3), (0, 4), (1, 5)])

    return puzzle
