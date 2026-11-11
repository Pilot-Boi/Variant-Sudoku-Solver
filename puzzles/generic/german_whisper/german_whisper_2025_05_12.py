"""PuzzleMadness German Whispers Sudoku — 2025-05-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [8, 4, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 5), (4, 6), (5, 6), (6, 7), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(3, 2), (4, 3), (4, 4), (3, 3), (2, 4)])
    puzzle.add_german_whispers([(1, 6), (1, 7), (2, 8), (3, 8), (4, 8)])
    puzzle.add_german_whispers([(5, 7), (5, 8), (6, 8), (7, 7), (8, 6)])
    puzzle.add_german_whispers([(5, 3), (6, 3), (7, 4), (8, 3)])
    puzzle.add_german_whispers([(3, 1), (2, 1), (2, 0), (1, 0)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (8, 0), (7, 1)])
    puzzle.add_german_whispers([(5, 2), (5, 1), (6, 0)])
    puzzle.add_german_whispers([(1, 5), (1, 4), (0, 4)])
    puzzle.add_german_whispers([(1, 2), (0, 1), (1, 1)])

    return puzzle
