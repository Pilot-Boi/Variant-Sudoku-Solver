"""PuzzleMadness German Whispers Sudoku — 2025-09-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 0, 8, 0, 4],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 7],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(6, 0), (5, 0), (5, 1), (4, 0), (3, 1), (2, 2)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (8, 7), (7, 6), (6, 6)])
    puzzle.add_german_whispers([(4, 4), (5, 3), (6, 3), (6, 4), (5, 5)])
    puzzle.add_german_whispers([(1, 7), (2, 6), (3, 6), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(3, 4), (2, 5), (1, 4), (2, 4), (2, 3)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (6, 8), (7, 7)])
    puzzle.add_german_whispers([(1, 2), (1, 1), (0, 2), (0, 1)])
    puzzle.add_german_whispers([(7, 0), (8, 0), (8, 1), (8, 2)])
    puzzle.add_german_whispers([(1, 6), (0, 6), (0, 5)])

    return puzzle
