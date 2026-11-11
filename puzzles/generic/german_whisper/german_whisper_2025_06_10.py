"""PuzzleMadness German Whispers Sudoku — 2025-06-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 1, 8, 0, 0],
        [0, 0, 9, 0, 0, 4, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 4), (5, 5), (4, 6), (3, 7), (4, 7), (4, 8)])
    puzzle.add_german_whispers([(3, 1), (4, 0), (5, 1), (5, 0), (6, 0)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (2, 2), (2, 1), (2, 0)])
    puzzle.add_german_whispers([(7, 5), (6, 5), (7, 4), (7, 3), (8, 2)])
    puzzle.add_german_whispers([(2, 3), (1, 4), (1, 3), (0, 4), (0, 3)])
    puzzle.add_german_whispers([(2, 5), (3, 5), (2, 6), (1, 6)])
    puzzle.add_german_whispers([(0, 7), (0, 8), (1, 8), (2, 8)])
    puzzle.add_german_whispers([(8, 7), (8, 6), (7, 7), (7, 8)])
    puzzle.add_german_whispers([(8, 0), (7, 1), (6, 2)])

    return puzzle
