"""PuzzleMadness German Whispers Sudoku — 2025-04-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 0, 0, 3, 0, 0, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 1), (5, 0), (5, 1), (6, 1), (7, 0), (8, 0)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (0, 4), (0, 5), (1, 6)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (7, 7), (8, 7), (7, 6)])
    puzzle.add_german_whispers([(6, 5), (5, 5), (5, 4), (6, 3), (7, 3)])
    puzzle.add_german_whispers([(3, 3), (3, 2), (4, 2), (3, 1), (2, 0)])
    puzzle.add_german_whispers([(2, 1), (1, 1), (2, 2), (2, 3)])
    puzzle.add_german_whispers([(4, 5), (3, 4), (3, 5), (4, 6)])
    puzzle.add_german_whispers([(4, 7), (5, 6), (5, 7), (4, 8)])
    puzzle.add_german_whispers([(2, 7), (3, 8), (2, 8)])
    puzzle.add_german_whispers([(0, 6), (1, 7), (2, 6)])

    return puzzle
