"""PuzzleMadness German Whispers Sudoku — 2025-10-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-10-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/10/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 7, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 8, 0, 0, 0, 0, 0, 7, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 2), (1, 1), (0, 2), (0, 3), (0, 4), (1, 5)])
    puzzle.add_german_whispers([(4, 0), (5, 0), (6, 1), (6, 2), (5, 2)])
    puzzle.add_german_whispers([(1, 8), (2, 7), (2, 8), (3, 7), (4, 8)])
    puzzle.add_german_whispers([(6, 3), (6, 4), (6, 5), (7, 4), (8, 5)])
    puzzle.add_german_whispers([(3, 2), (3, 3), (4, 2), (4, 3), (5, 3)])
    puzzle.add_german_whispers([(5, 7), (4, 6), (5, 6), (5, 5)])
    puzzle.add_german_whispers([(7, 8), (8, 7), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(4, 4), (3, 4), (2, 3), (1, 3)])
    puzzle.add_german_whispers([(7, 2), (7, 1), (8, 1), (7, 0)])
    puzzle.add_german_whispers([(1, 7), (2, 6), (1, 6)])

    return puzzle
