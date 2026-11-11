"""PuzzleMadness German Whispers Sudoku — 2025-01-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-01-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/1/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 9, 6, 0],
        [0, 0, 0, 2, 0, 0, 0, 3, 0],
        [2, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 3],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 0), (3, 1), (2, 2), (1, 3), (2, 4), (2, 5)])
    puzzle.add_german_whispers([(3, 4), (4, 5), (3, 5), (2, 6), (1, 5)])
    puzzle.add_german_whispers([(7, 8), (6, 7), (5, 6), (4, 6), (3, 7)])
    puzzle.add_german_whispers([(3, 3), (3, 2), (4, 1), (5, 0), (5, 1)])
    puzzle.add_german_whispers([(5, 4), (6, 5), (7, 5), (8, 5), (8, 4)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (6, 1), (6, 2)])
    puzzle.add_german_whispers([(1, 8), (2, 8), (1, 7), (0, 8)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1), (1, 2)])
    puzzle.add_german_whispers([(7, 6), (8, 6), (8, 7)])

    return puzzle
