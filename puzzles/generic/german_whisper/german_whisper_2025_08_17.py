"""PuzzleMadness German Whispers Sudoku — 2025-08-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 2, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 0), (4, 1), (5, 0), (5, 1), (5, 2), (5, 3)])
    puzzle.add_german_whispers([(3, 6), (2, 7), (2, 6), (1, 6), (0, 5)])
    puzzle.add_german_whispers([(0, 1), (1, 1), (2, 0), (2, 1), (3, 2)])
    puzzle.add_german_whispers([(6, 5), (6, 4), (7, 3), (7, 2), (8, 2)])
    puzzle.add_german_whispers([(4, 4), (3, 5), (2, 4), (1, 3)])
    puzzle.add_german_whispers([(7, 7), (7, 6), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(3, 7), (4, 7), (3, 8)])
    puzzle.add_german_whispers([(0, 4), (1, 4), (0, 3)])
    puzzle.add_german_whispers([(2, 2), (3, 3), (3, 4)])
    puzzle.add_german_whispers([(6, 1), (7, 0), (6, 0)])

    return puzzle
