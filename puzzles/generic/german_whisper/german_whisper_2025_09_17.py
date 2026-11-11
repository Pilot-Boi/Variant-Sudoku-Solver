"""PuzzleMadness German Whispers Sudoku — 2025-09-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 7, 0, 0, 9, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 9, 0, 8, 0, 2, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 8), (1, 7), (0, 6), (1, 5), (0, 5), (0, 4)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (4, 2), (3, 3), (4, 3)])
    puzzle.add_german_whispers([(4, 4), (5, 3), (6, 4), (6, 5), (5, 5)])
    puzzle.add_german_whispers([(0, 1), (1, 2), (1, 3), (2, 2), (2, 1)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (4, 7), (3, 6), (2, 6)])
    puzzle.add_german_whispers([(7, 5), (7, 4), (8, 5), (8, 4)])
    puzzle.add_german_whispers([(6, 1), (7, 2), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(1, 1), (1, 0), (2, 0), (3, 1)])
    puzzle.add_german_whispers([(2, 7), (3, 8), (3, 7)])

    return puzzle
