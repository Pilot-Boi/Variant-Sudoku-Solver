"""PuzzleMadness German Whispers Sudoku — 2025-02-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-02-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/2/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 8, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0, 8, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(7, 6), (8, 7), (8, 6), (7, 5), (7, 4), (6, 3)])
    puzzle.add_german_whispers([(3, 2), (3, 1), (4, 0), (4, 1), (5, 0)])
    puzzle.add_german_whispers([(6, 6), (5, 6), (5, 7), (4, 6), (4, 5)])
    puzzle.add_german_whispers([(8, 2), (7, 2), (7, 3), (6, 2), (5, 3)])
    puzzle.add_german_whispers([(3, 8), (2, 8), (3, 7), (3, 6), (2, 6)])
    puzzle.add_german_whispers([(2, 2), (3, 3), (3, 4), (4, 3)])
    puzzle.add_german_whispers([(2, 4), (1, 4), (0, 4), (1, 3)])
    puzzle.add_german_whispers([(1, 2), (1, 1), (2, 0), (1, 0)])
    puzzle.add_german_whispers([(4, 2), (5, 1), (6, 0)])
    puzzle.add_german_whispers([(0, 7), (0, 6), (0, 5)])

    return puzzle
