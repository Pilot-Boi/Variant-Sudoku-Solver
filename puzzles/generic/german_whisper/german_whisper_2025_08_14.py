"""PuzzleMadness German Whispers Sudoku — 2025-08-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [7, 0, 0, 0, 0, 0, 3, 0, 0],
        [1, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 9, 0, 0, 0, 0, 1],
        [0, 6, 0, 0, 0, 0, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (8, 4), (7, 3), (7, 4), (6, 3), (6, 2)])
    puzzle.add_german_whispers([(6, 8), (7, 8), (8, 7), (7, 7), (6, 6)])
    puzzle.add_german_whispers([(6, 5), (5, 4), (5, 5), (4, 5), (3, 6)])
    puzzle.add_german_whispers([(3, 2), (4, 3), (4, 2), (5, 1), (4, 1)])
    puzzle.add_german_whispers([(1, 6), (2, 7), (3, 7), (2, 6), (1, 5)])
    puzzle.add_german_whispers([(1, 0), (2, 1), (3, 1), (3, 0)])
    puzzle.add_german_whispers([(0, 5), (0, 4), (1, 4), (2, 5)])
    puzzle.add_german_whispers([(3, 3), (2, 2), (1, 2)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (5, 8)])

    return puzzle
