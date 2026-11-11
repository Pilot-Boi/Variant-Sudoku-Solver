"""PuzzleMadness German Whispers Sudoku — 2025-06-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 5, 0, 3, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 5, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 6],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 8), (6, 8), (7, 7), (8, 6), (7, 5), (6, 5)])
    puzzle.add_german_whispers([(3, 1), (2, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_german_whispers([(3, 7), (2, 7), (3, 8), (2, 8), (1, 7)])
    puzzle.add_german_whispers([(1, 0), (1, 1), (2, 2), (1, 2), (1, 3)])
    puzzle.add_german_whispers([(4, 6), (3, 6), (2, 5), (2, 6)])
    puzzle.add_german_whispers([(5, 3), (4, 4), (5, 4), (6, 3)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (8, 0), (7, 1)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (4, 2), (5, 2)])
    puzzle.add_german_whispers([(6, 2), (7, 2), (6, 1)])
    puzzle.add_german_whispers([(0, 5), (0, 4), (1, 4)])

    return puzzle
