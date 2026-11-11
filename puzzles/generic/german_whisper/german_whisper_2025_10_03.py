"""PuzzleMadness German Whispers Sudoku — 2025-10-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 7, 0, 5, 3, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 2), (2, 3), (1, 4), (0, 5), (1, 6), (2, 6)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (2, 1), (1, 0), (2, 0)])
    puzzle.add_german_whispers([(3, 7), (3, 6), (4, 5), (5, 5), (4, 6)])
    puzzle.add_german_whispers([(6, 5), (7, 4), (6, 3), (5, 3), (5, 4)])
    puzzle.add_german_whispers([(8, 1), (8, 2), (7, 2), (6, 2), (6, 1)])
    puzzle.add_german_whispers([(6, 7), (5, 7), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(4, 2), (4, 1), (3, 1)])

    return puzzle
