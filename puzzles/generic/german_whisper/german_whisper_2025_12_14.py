"""PuzzleMadness German Whispers Sudoku — 2025-12-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 7, 0, 0, 3, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 6, 3, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 7), (4, 6), (5, 5), (6, 4), (6, 3), (5, 3)])
    puzzle.add_german_whispers([(3, 3), (2, 2), (1, 1), (1, 0), (0, 1)])
    puzzle.add_german_whispers([(8, 2), (7, 1), (6, 0), (5, 0), (5, 1)])
    puzzle.add_german_whispers([(7, 4), (7, 5), (7, 6), (8, 7), (7, 8)])
    puzzle.add_german_whispers([(3, 6), (2, 5), (2, 6), (1, 6), (0, 7)])
    puzzle.add_german_whispers([(4, 5), (3, 4), (2, 3), (1, 3)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (7, 7), (6, 7)])
    puzzle.add_german_whispers([(2, 0), (3, 1), (3, 0), (4, 1)])
    puzzle.add_german_whispers([(1, 7), (1, 8), (2, 8)])
    puzzle.add_german_whispers([(1, 2), (0, 2), (0, 3)])
    puzzle.add_german_whispers([(8, 4), (7, 3), (6, 2)])

    return puzzle
