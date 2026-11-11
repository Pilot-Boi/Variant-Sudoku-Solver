"""PuzzleMadness German Whispers Sudoku — 2025-05-04."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-04'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/4'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 2, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 4],
        [3, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 2), (1, 1), (2, 0), (2, 1), (3, 2), (4, 2)])
    puzzle.add_german_whispers([(3, 4), (2, 3), (1, 3), (1, 4), (0, 4)])
    puzzle.add_german_whispers([(4, 6), (4, 5), (4, 4), (3, 5), (2, 6)])
    puzzle.add_german_whispers([(2, 8), (2, 7), (1, 6), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(8, 8), (7, 8), (6, 8), (5, 7), (5, 6)])
    puzzle.add_german_whispers([(6, 3), (7, 4), (7, 3), (6, 2)])
    puzzle.add_german_whispers([(7, 1), (6, 0), (6, 1), (5, 2)])
    puzzle.add_german_whispers([(6, 5), (5, 5), (6, 4)])

    return puzzle
