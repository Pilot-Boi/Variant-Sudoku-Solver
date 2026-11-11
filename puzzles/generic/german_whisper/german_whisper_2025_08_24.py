"""PuzzleMadness German Whispers Sudoku — 2025-08-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 8), (6, 7), (5, 7), (4, 7)])
    puzzle.add_german_whispers([(1, 5), (1, 6), (0, 6), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (5, 1), (6, 1), (6, 0)])
    puzzle.add_german_whispers([(6, 6), (5, 5), (5, 4), (4, 5), (3, 4)])
    puzzle.add_german_whispers([(0, 1), (0, 2), (1, 3), (2, 3), (2, 2)])
    puzzle.add_german_whispers([(3, 5), (2, 6), (3, 7), (3, 6)])
    puzzle.add_german_whispers([(7, 5), (8, 4), (8, 3), (7, 3)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_german_whispers([(2, 0), (2, 1), (3, 0)])
    puzzle.add_german_whispers([(7, 6), (7, 7), (8, 7)])

    return puzzle
