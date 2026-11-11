"""PuzzleMadness German Whispers Sudoku — 2025-09-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-09-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/9/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [7, 0, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 3, 0, 1, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 8), (5, 7), (6, 6), (7, 5), (7, 4), (6, 5)])
    puzzle.add_german_whispers([(3, 2), (4, 1), (4, 0), (3, 0), (2, 1)])
    puzzle.add_german_whispers([(0, 6), (1, 6), (1, 7), (2, 6), (1, 5)])
    puzzle.add_german_whispers([(1, 3), (2, 3), (3, 4), (3, 5), (3, 6)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (7, 1), (7, 0), (6, 1)])
    puzzle.add_german_whispers([(4, 4), (5, 5), (5, 4), (6, 3)])
    puzzle.add_german_whispers([(0, 2), (0, 1), (1, 1), (2, 2)])
    puzzle.add_german_whispers([(1, 4), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(8, 6), (8, 7), (8, 8)])

    return puzzle
