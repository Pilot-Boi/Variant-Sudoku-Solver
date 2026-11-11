"""PuzzleMadness German Whispers Sudoku — 2025-12-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-12-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/12/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [9, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 8), (0, 7), (0, 6), (1, 5), (2, 5), (2, 6)])
    puzzle.add_german_whispers([(1, 1), (1, 2), (0, 3), (0, 4), (1, 4)])
    puzzle.add_german_whispers([(7, 4), (8, 3), (8, 2), (7, 2), (7, 1)])
    puzzle.add_german_whispers([(3, 2), (4, 2), (4, 1), (3, 1), (2, 2)])
    puzzle.add_german_whispers([(6, 5), (6, 6), (6, 7), (7, 6)])
    puzzle.add_german_whispers([(4, 6), (4, 5), (3, 5), (2, 4)])
    puzzle.add_german_whispers([(6, 4), (5, 5), (5, 6), (4, 7)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (1, 8), (2, 7)])
    puzzle.add_german_whispers([(0, 0), (0, 1), (1, 0)])
    puzzle.add_german_whispers([(5, 8), (4, 8), (5, 7)])
    puzzle.add_german_whispers([(6, 0), (7, 0), (6, 1)])

    return puzzle
