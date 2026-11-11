"""PuzzleMadness German Whispers Sudoku — 2025-10-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 6), (4, 7), (3, 6), (3, 5), (2, 5), (3, 4)])
    puzzle.add_german_whispers([(5, 0), (6, 1), (7, 2), (8, 3), (7, 4)])
    puzzle.add_german_whispers([(6, 5), (6, 4), (6, 3), (6, 2), (5, 2)])
    puzzle.add_german_whispers([(3, 1), (4, 2), (5, 3), (4, 3), (5, 4)])
    puzzle.add_german_whispers([(7, 7), (6, 8), (7, 8), (8, 7), (7, 6)])
    puzzle.add_german_whispers([(3, 3), (2, 4), (1, 5), (0, 5)])
    puzzle.add_german_whispers([(0, 8), (1, 8), (1, 7), (0, 6)])
    puzzle.add_german_whispers([(2, 0), (1, 1), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(2, 2), (2, 3), (1, 4)])
    puzzle.add_german_whispers([(4, 0), (3, 0), (4, 1)])

    return puzzle
