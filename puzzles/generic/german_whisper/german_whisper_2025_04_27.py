"""PuzzleMadness German Whispers Sudoku — 2025-04-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 8],
        [0, 0, 0, 0, 4, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 4, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 5), (4, 5), (5, 4), (5, 3), (5, 2), (4, 1)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (6, 7), (5, 8), (5, 7)])
    puzzle.add_german_whispers([(8, 4), (7, 4), (7, 5), (8, 5), (8, 6)])
    puzzle.add_german_whispers([(2, 0), (1, 0), (0, 0), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (2, 6), (1, 6)])
    puzzle.add_german_whispers([(3, 6), (2, 7), (3, 7), (3, 8)])
    puzzle.add_german_whispers([(1, 3), (2, 3), (1, 4), (0, 3)])
    puzzle.add_german_whispers([(8, 2), (7, 3), (8, 3)])
    puzzle.add_german_whispers([(3, 2), (4, 2), (3, 1)])
    puzzle.add_german_whispers([(6, 2), (7, 1), (6, 1)])

    return puzzle
