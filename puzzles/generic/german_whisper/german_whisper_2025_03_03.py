"""PuzzleMadness German Whispers Sudoku — 2025-03-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 8, 0, 3, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 7, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 7), (6, 7), (6, 6), (7, 5), (8, 6), (7, 6)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (2, 2), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(4, 7), (4, 8), (3, 8), (2, 7), (1, 8)])
    puzzle.add_german_whispers([(3, 3), (4, 3), (4, 4), (5, 4), (5, 3)])
    puzzle.add_german_whispers([(1, 4), (0, 5), (1, 6), (1, 5)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(6, 1), (7, 1), (6, 0)])

    return puzzle
