"""PuzzleMadness German Whispers Sudoku — 2025-11-16."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-11-16'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/11/16'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 3, 0, 0],
        [0, 0, 4, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(1, 3), (0, 3), (0, 4), (1, 4), (2, 3), (3, 3)])
    puzzle.add_german_whispers([(0, 8), (0, 7), (1, 7), (2, 6), (3, 5)])
    puzzle.add_german_whispers([(4, 7), (5, 6), (6, 6), (6, 7), (5, 8)])
    puzzle.add_german_whispers([(7, 1), (7, 2), (6, 3), (5, 4), (6, 5)])
    puzzle.add_german_whispers([(8, 5), (7, 5), (8, 6), (7, 7), (8, 7)])
    puzzle.add_german_whispers([(0, 0), (1, 1), (2, 2), (3, 2)])
    puzzle.add_german_whispers([(5, 1), (4, 1), (3, 1), (2, 0)])
    puzzle.add_german_whispers([(3, 8), (4, 8), (5, 7)])
    puzzle.add_german_whispers([(1, 8), (2, 8), (2, 7)])
    puzzle.add_german_whispers([(4, 6), (4, 5), (5, 5)])

    return puzzle
