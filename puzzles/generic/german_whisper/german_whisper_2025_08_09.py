"""PuzzleMadness German Whispers Sudoku — 2025-08-09."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-08-09'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/8/9'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [1, 0, 0, 0, 0, 0, 7, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 9, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 4), (0, 5), (0, 6), (1, 7), (2, 6), (1, 6)])
    puzzle.add_german_whispers([(3, 7), (3, 6), (3, 5), (4, 6), (5, 5)])
    puzzle.add_german_whispers([(6, 0), (5, 1), (4, 1), (3, 0), (4, 0)])
    puzzle.add_german_whispers([(8, 5), (8, 4), (7, 3), (8, 2), (8, 3)])
    puzzle.add_german_whispers([(5, 7), (6, 7), (7, 6), (6, 5)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (1, 2), (2, 3)])
    puzzle.add_german_whispers([(5, 3), (6, 4), (6, 3), (7, 2)])
    puzzle.add_german_whispers([(2, 0), (3, 1), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(0, 3), (1, 4), (2, 4)])
    puzzle.add_german_whispers([(7, 7), (8, 8), (7, 8)])
    puzzle.add_german_whispers([(6, 1), (7, 1), (7, 0)])

    return puzzle
