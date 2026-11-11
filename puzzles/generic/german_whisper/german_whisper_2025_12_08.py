"""PuzzleMadness German Whispers Sudoku — 2025-12-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 9, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 4, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 0), (3, 0), (3, 1), (2, 2), (3, 2), (4, 1)])
    puzzle.add_german_whispers([(5, 8), (4, 7), (5, 7), (6, 6), (7, 7)])
    puzzle.add_german_whispers([(6, 0), (5, 0), (5, 1), (6, 2), (7, 2)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (1, 3), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(8, 1), (8, 0), (7, 0), (7, 1)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (0, 6), (1, 5)])
    puzzle.add_german_whispers([(8, 3), (7, 4), (6, 4), (5, 3)])
    puzzle.add_german_whispers([(4, 8), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (7, 6)])
    puzzle.add_german_whispers([(5, 4), (4, 4), (4, 3)])

    return puzzle
