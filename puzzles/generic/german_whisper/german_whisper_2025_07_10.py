"""PuzzleMadness German Whispers Sudoku — 2025-07-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 8, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 7, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 4), (2, 5), (3, 5), (3, 4), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(2, 8), (3, 8), (2, 7), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(4, 5), (5, 6), (6, 7), (5, 7), (6, 8)])
    puzzle.add_german_whispers([(5, 5), (6, 5), (7, 4), (8, 4), (7, 3)])
    puzzle.add_german_whispers([(0, 2), (1, 2), (1, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(4, 1), (4, 2), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(6, 3), (7, 2), (8, 2), (7, 1)])
    puzzle.add_german_whispers([(5, 1), (4, 0), (5, 0), (6, 1)])
    puzzle.add_german_whispers([(1, 6), (0, 7), (1, 8)])

    return puzzle
