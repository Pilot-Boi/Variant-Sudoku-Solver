"""PuzzleMadness German Whispers Sudoku — 2025-08-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(2, 1), (2, 0), (1, 1), (1, 2), (1, 3), (2, 3)])
    puzzle.add_german_whispers([(3, 4), (4, 4), (5, 3), (5, 4), (6, 4)])
    puzzle.add_german_whispers([(2, 6), (2, 5), (1, 6), (2, 7), (2, 8)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (7, 1), (8, 1), (7, 0)])
    puzzle.add_german_whispers([(6, 5), (5, 5), (4, 6), (4, 7), (3, 7)])
    puzzle.add_german_whispers([(7, 8), (8, 8), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(6, 1), (5, 0), (4, 0), (4, 1)])
    puzzle.add_german_whispers([(0, 4), (0, 3), (0, 2)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (3, 2)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (1, 7)])

    return puzzle
