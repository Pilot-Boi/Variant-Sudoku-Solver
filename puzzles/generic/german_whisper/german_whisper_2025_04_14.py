"""PuzzleMadness German Whispers Sudoku — 2025-04-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 3), (0, 4), (1, 4), (1, 5), (2, 5), (3, 5)])
    puzzle.add_german_whispers([(4, 5), (5, 6), (6, 5), (7, 6), (7, 5)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 2), (5, 2), (6, 3)])
    puzzle.add_german_whispers([(6, 1), (5, 0), (4, 0), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(3, 2), (2, 2), (2, 1), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (4, 7), (3, 6)])
    puzzle.add_german_whispers([(2, 7), (1, 6), (0, 7), (0, 6)])
    puzzle.add_german_whispers([(7, 8), (6, 7), (7, 7), (8, 6)])
    puzzle.add_german_whispers([(8, 2), (8, 3), (7, 2)])
    puzzle.add_german_whispers([(7, 0), (8, 1), (8, 0)])

    return puzzle
