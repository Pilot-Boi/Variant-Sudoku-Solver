"""PuzzleMadness German Whispers Sudoku — 2025-05-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 9, 7, 0, 0, 0, 0, 2, 5],
        [3, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 5), (6, 4), (5, 5), (6, 5), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(4, 0), (3, 1), (3, 0), (2, 1), (1, 2)])
    puzzle.add_german_whispers([(3, 2), (2, 2), (1, 3), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(5, 8), (5, 7), (6, 7), (6, 8), (7, 8)])
    puzzle.add_german_whispers([(5, 2), (4, 3), (4, 4), (3, 3)])
    puzzle.add_german_whispers([(7, 4), (7, 3), (6, 3), (6, 2)])
    puzzle.add_german_whispers([(7, 1), (7, 0), (8, 1), (8, 0)])
    puzzle.add_german_whispers([(4, 8), (3, 7), (2, 7)])
    puzzle.add_german_whispers([(0, 0), (1, 0), (0, 1)])
    puzzle.add_german_whispers([(0, 6), (0, 7), (1, 6)])

    return puzzle
