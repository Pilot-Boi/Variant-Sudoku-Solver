"""PuzzleMadness German Whispers Sudoku — 2025-08-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 7), (1, 6), (0, 5), (1, 4), (1, 5), (2, 4)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (2, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(4, 7), (4, 8), (5, 8), (6, 8), (7, 7)])
    puzzle.add_german_whispers([(7, 2), (7, 1), (8, 0), (7, 0), (6, 1)])
    puzzle.add_german_whispers([(7, 6), (6, 7), (5, 6), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(3, 5), (3, 6), (4, 5), (5, 4)])
    puzzle.add_german_whispers([(7, 5), (8, 4), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(5, 2), (6, 2), (6, 3), (6, 4)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 2), (2, 2)])
    puzzle.add_german_whispers([(1, 3), (0, 3), (0, 4)])
    puzzle.add_german_whispers([(3, 3), (4, 3), (5, 3)])

    return puzzle
