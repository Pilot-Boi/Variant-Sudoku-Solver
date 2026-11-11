"""PuzzleMadness German Whispers Sudoku — 2025-05-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 4],
        [0, 8, 4, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 4), (2, 4), (2, 5), (3, 4), (4, 5), (4, 6)])
    puzzle.add_german_whispers([(5, 3), (6, 3), (6, 2), (5, 1), (6, 0)])
    puzzle.add_german_whispers([(1, 8), (0, 8), (1, 7), (1, 6), (0, 5)])
    puzzle.add_german_whispers([(2, 3), (2, 2), (2, 1), (1, 1), (1, 2)])
    puzzle.add_german_whispers([(3, 6), (4, 7), (5, 6), (6, 7)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(7, 7), (6, 6), (7, 5), (7, 4)])
    puzzle.add_german_whispers([(5, 0), (4, 0), (3, 0), (3, 1)])
    puzzle.add_german_whispers([(7, 6), (8, 5), (8, 6)])
    puzzle.add_german_whispers([(5, 8), (6, 8), (5, 7)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1)])
    puzzle.add_german_whispers([(3, 3), (3, 2), (4, 2)])

    return puzzle
