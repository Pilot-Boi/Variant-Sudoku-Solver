"""PuzzleMadness German Whispers Sudoku — 2025-04-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 3, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 6, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 7, 8, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 8), (1, 8), (2, 7), (3, 7), (3, 8), (4, 7)])
    puzzle.add_german_whispers([(6, 0), (6, 1), (7, 0), (7, 1), (8, 2)])
    puzzle.add_german_whispers([(0, 2), (1, 1), (1, 2), (2, 2), (1, 3)])
    puzzle.add_german_whispers([(6, 4), (7, 4), (6, 5), (6, 6), (6, 7)])
    puzzle.add_german_whispers([(5, 6), (5, 5), (4, 5), (5, 4), (4, 4)])
    puzzle.add_german_whispers([(3, 1), (3, 2), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(2, 5), (2, 6), (3, 6), (3, 5)])
    puzzle.add_german_whispers([(5, 8), (6, 8), (7, 7)])
    puzzle.add_german_whispers([(0, 4), (0, 5), (1, 4)])
    puzzle.add_german_whispers([(0, 8), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(6, 3), (7, 3), (8, 3)])

    return puzzle
