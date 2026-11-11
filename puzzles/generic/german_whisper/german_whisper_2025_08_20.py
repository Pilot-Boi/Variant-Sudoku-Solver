"""PuzzleMadness German Whispers Sudoku — 2025-08-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 6), (0, 7), (0, 8), (1, 8), (2, 7), (1, 6)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (3, 2), (3, 3), (2, 3)])
    puzzle.add_german_whispers([(7, 2), (8, 3), (8, 4), (7, 4), (6, 5)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (4, 2), (3, 1), (4, 0)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (6, 8), (7, 7)])
    puzzle.add_german_whispers([(5, 6), (5, 7), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (1, 2), (2, 2)])
    puzzle.add_german_whispers([(5, 0), (6, 0), (7, 0)])
    puzzle.add_german_whispers([(2, 8), (3, 7), (3, 6)])
    puzzle.add_german_whispers([(1, 4), (2, 5), (1, 5)])

    return puzzle
