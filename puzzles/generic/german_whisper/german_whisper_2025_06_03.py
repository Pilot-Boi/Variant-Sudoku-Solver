"""PuzzleMadness German Whispers Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 6, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 5), (2, 5), (1, 6), (1, 7), (0, 6), (1, 5)])
    puzzle.add_german_whispers([(1, 2), (0, 1), (0, 2), (1, 3), (0, 4)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (8, 2), (7, 2), (7, 3)])
    puzzle.add_german_whispers([(6, 5), (5, 5), (6, 4), (7, 4), (7, 5)])
    puzzle.add_german_whispers([(3, 2), (3, 3), (2, 3), (3, 4)])
    puzzle.add_german_whispers([(6, 7), (7, 7), (6, 6), (5, 6)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (2, 7), (3, 6)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (6, 8)])
    puzzle.add_german_whispers([(6, 1), (5, 2), (5, 1)])
    puzzle.add_german_whispers([(5, 4), (4, 5), (4, 6)])

    return puzzle
