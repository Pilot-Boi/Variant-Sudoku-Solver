"""PuzzleMadness German Whispers Sudoku — 2025-03-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 3, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 6), (5, 7), (5, 8), (4, 7), (3, 7), (2, 6)])
    puzzle.add_german_whispers([(4, 0), (5, 1), (6, 2), (7, 1), (7, 2)])
    puzzle.add_german_whispers([(3, 2), (4, 3), (3, 4), (2, 4), (1, 5)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (7, 5), (6, 6), (7, 6)])
    puzzle.add_german_whispers([(2, 7), (2, 8), (1, 7), (0, 8), (0, 7)])
    puzzle.add_german_whispers([(1, 2), (0, 1), (1, 1), (1, 0)])
    puzzle.add_german_whispers([(3, 0), (3, 1), (2, 2), (3, 3)])
    puzzle.add_german_whispers([(4, 5), (5, 4), (6, 4)])
    puzzle.add_german_whispers([(8, 3), (7, 3), (8, 2)])
    puzzle.add_german_whispers([(6, 7), (6, 8), (7, 7)])

    return puzzle
