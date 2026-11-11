"""PuzzleMadness German Whispers Sudoku — 2025-11-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 5, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 3],
        [4, 8, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 4, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 3), (3, 3), (4, 4), (5, 5), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (2, 7), (2, 8), (3, 8)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (3, 0), (2, 0), (2, 1)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (8, 6), (8, 5), (7, 5)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (6, 2), (7, 2)])
    puzzle.add_german_whispers([(0, 3), (1, 4), (0, 5), (0, 6)])
    puzzle.add_german_whispers([(6, 4), (7, 4), (8, 4), (7, 3)])
    puzzle.add_german_whispers([(6, 8), (5, 7), (4, 8)])

    return puzzle
