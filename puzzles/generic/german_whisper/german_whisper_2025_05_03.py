"""PuzzleMadness German Whispers Sudoku — 2025-05-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (1, 5), (2, 4), (1, 3), (1, 2), (0, 2)])
    puzzle.add_german_whispers([(6, 3), (6, 4), (5, 4), (4, 5), (3, 5)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (6, 6), (6, 7), (5, 7)])
    puzzle.add_german_whispers([(4, 4), (3, 4), (2, 5), (3, 6), (3, 7)])
    puzzle.add_german_whispers([(0, 1), (0, 0), (1, 1), (2, 2)])
    puzzle.add_german_whispers([(5, 0), (4, 1), (5, 2), (4, 2)])
    puzzle.add_german_whispers([(4, 3), (3, 3), (3, 2), (3, 1)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (4, 7)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (8, 0)])
    puzzle.add_german_whispers([(6, 1), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(1, 6), (0, 7), (1, 8)])

    return puzzle
