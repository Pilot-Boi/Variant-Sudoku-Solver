"""PuzzleMadness German Whispers Sudoku — 2025-05-10."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-10'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/10'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 1, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 8), (1, 8), (2, 7), (1, 7), (2, 6), (2, 5)])
    puzzle.add_german_whispers([(1, 3), (2, 3), (3, 2), (3, 3), (3, 4)])
    puzzle.add_german_whispers([(5, 2), (4, 1), (5, 1), (6, 2), (7, 3)])
    puzzle.add_german_whispers([(7, 4), (7, 5), (7, 6), (6, 7), (5, 7)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 1), (1, 2)])
    puzzle.add_german_whispers([(4, 6), (5, 6), (6, 6), (5, 5)])
    puzzle.add_german_whispers([(7, 7), (8, 7), (7, 8), (8, 8)])
    puzzle.add_german_whispers([(8, 0), (8, 1), (7, 0), (6, 0)])
    puzzle.add_german_whispers([(5, 3), (4, 4), (4, 3)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 8)])
    puzzle.add_german_whispers([(4, 0), (3, 1), (2, 2)])

    return puzzle
