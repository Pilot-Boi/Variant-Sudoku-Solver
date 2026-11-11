"""PuzzleMadness German Whispers Sudoku — 2025-03-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-03-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/3/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, 0, 0, 0, 7, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(3, 1), (4, 1), (4, 0), (5, 1), (6, 1), (7, 0)])
    puzzle.add_german_whispers([(8, 4), (8, 5), (7, 6), (7, 7), (6, 8)])
    puzzle.add_german_whispers([(5, 7), (6, 7), (5, 6), (5, 5), (6, 5)])
    puzzle.add_german_whispers([(1, 2), (2, 2), (1, 3), (1, 4), (0, 3)])
    puzzle.add_german_whispers([(1, 6), (1, 5), (0, 6), (0, 7), (0, 8)])
    puzzle.add_german_whispers([(7, 3), (8, 2), (8, 1), (7, 2)])
    puzzle.add_german_whispers([(3, 6), (3, 7), (4, 8), (3, 8)])
    puzzle.add_german_whispers([(4, 3), (4, 4), (3, 3), (3, 4)])
    puzzle.add_german_whispers([(5, 4), (6, 4), (7, 5)])

    return puzzle
