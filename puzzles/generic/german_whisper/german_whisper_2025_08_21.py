"""PuzzleMadness German Whispers Sudoku — 2025-08-21."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-21'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/21'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [1, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 4, 0],
        [0, 4, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (7, 6), (7, 7), (6, 6), (5, 6), (6, 5)])
    puzzle.add_german_whispers([(1, 3), (2, 4), (1, 4), (1, 5), (2, 6)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (7, 1), (7, 2), (7, 3)])
    puzzle.add_german_whispers([(5, 3), (6, 4), (6, 3), (6, 2), (5, 2)])
    puzzle.add_german_whispers([(4, 8), (5, 7), (4, 7), (4, 6)])
    puzzle.add_german_whispers([(3, 6), (4, 5), (3, 4), (4, 3)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 1), (2, 1)])
    puzzle.add_german_whispers([(2, 8), (2, 7), (1, 6)])
    puzzle.add_german_whispers([(2, 2), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(5, 0), (4, 0), (5, 1)])

    return puzzle
