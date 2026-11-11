"""PuzzleMadness German Whispers Sudoku — 2025-10-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 9, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 4), (2, 5), (1, 4), (2, 4), (2, 3), (1, 3)])
    puzzle.add_german_whispers([(6, 1), (5, 1), (5, 2), (5, 3), (6, 4)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (1, 7), (0, 7), (1, 6)])
    puzzle.add_german_whispers([(0, 3), (0, 2), (0, 1), (0, 0), (1, 0)])
    puzzle.add_german_whispers([(7, 5), (6, 6), (6, 5), (5, 5), (4, 6)])
    puzzle.add_german_whispers([(2, 6), (3, 5), (3, 6), (4, 7)])
    puzzle.add_german_whispers([(3, 3), (4, 2), (4, 1), (4, 0)])
    puzzle.add_german_whispers([(7, 2), (8, 1), (7, 0), (7, 1)])
    puzzle.add_german_whispers([(7, 7), (8, 6), (8, 5)])

    return puzzle
