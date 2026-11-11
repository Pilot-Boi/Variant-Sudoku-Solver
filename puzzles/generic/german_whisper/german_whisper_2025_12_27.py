"""PuzzleMadness German Whispers Sudoku — 2025-12-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 3, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 8],
        [5, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(4, 8), (3, 8), (3, 7), (2, 8), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(7, 1), (8, 2), (8, 3), (7, 4), (8, 5)])
    puzzle.add_german_whispers([(4, 2), (3, 1), (3, 0), (4, 0), (5, 0)])
    puzzle.add_german_whispers([(1, 1), (2, 1), (1, 2), (2, 2), (1, 3)])
    puzzle.add_german_whispers([(7, 7), (7, 8), (6, 8), (5, 7)])
    puzzle.add_german_whispers([(4, 4), (5, 4), (4, 3), (5, 3)])
    puzzle.add_german_whispers([(6, 7), (6, 6), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(3, 5), (2, 4), (1, 5)])
    puzzle.add_german_whispers([(1, 4), (0, 4), (0, 5)])
    puzzle.add_german_whispers([(5, 2), (6, 2), (6, 1)])

    return puzzle
