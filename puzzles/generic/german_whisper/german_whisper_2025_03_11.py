"""PuzzleMadness German Whispers Sudoku — 2025-03-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 7, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 8],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 2],
        [0, 4, 0, 9, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 1), (5, 2), (4, 2), (3, 2), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (2, 7), (1, 6), (2, 5)])
    puzzle.add_german_whispers([(6, 8), (7, 7), (6, 6), (7, 5), (8, 6)])
    puzzle.add_german_whispers([(5, 5), (6, 4), (7, 3), (8, 4), (8, 5)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (6, 2), (6, 1)])
    puzzle.add_german_whispers([(1, 2), (2, 2), (1, 1), (0, 1)])
    puzzle.add_german_whispers([(3, 5), (4, 4), (3, 3)])
    puzzle.add_german_whispers([(3, 6), (3, 7), (2, 8)])
    puzzle.add_german_whispers([(1, 5), (0, 5), (0, 4)])

    return puzzle
