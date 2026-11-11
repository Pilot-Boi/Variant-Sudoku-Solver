"""PuzzleMadness German Whispers Sudoku — 2025-06-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 3, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 8, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 7, 0, 1],
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 0), (1, 0), (2, 1), (3, 2), (3, 3), (4, 4)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 2), (7, 2), (6, 1)])
    puzzle.add_german_whispers([(4, 7), (5, 7), (5, 6), (5, 5), (6, 4)])
    puzzle.add_german_whispers([(8, 7), (7, 7), (6, 7), (6, 8), (5, 8)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(3, 4), (2, 5), (1, 6), (0, 6)])
    puzzle.add_german_whispers([(1, 2), (2, 2), (1, 3), (2, 4)])
    puzzle.add_german_whispers([(2, 0), (3, 0), (3, 1), (4, 1)])
    puzzle.add_german_whispers([(1, 8), (0, 7), (0, 8)])

    return puzzle
