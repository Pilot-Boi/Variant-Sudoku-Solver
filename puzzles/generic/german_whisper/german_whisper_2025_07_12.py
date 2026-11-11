"""PuzzleMadness German Whispers Sudoku — 2025-07-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-07-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/7/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 4), (6, 3), (5, 3), (6, 2)])
    puzzle.add_german_whispers([(5, 2), (6, 1), (6, 0), (5, 0), (4, 0)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (2, 0), (1, 1), (0, 2)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (2, 6), (3, 5), (2, 5)])
    puzzle.add_german_whispers([(3, 8), (4, 7), (3, 6), (4, 6)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(2, 2), (3, 3), (4, 4), (5, 4)])
    puzzle.add_german_whispers([(8, 8), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (8, 0)])
    puzzle.add_german_whispers([(3, 1), (3, 2), (4, 3)])
    puzzle.add_german_whispers([(1, 5), (0, 4), (0, 3)])

    return puzzle
