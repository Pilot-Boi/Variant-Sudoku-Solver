"""PuzzleMadness German Whispers Sudoku — 2025-06-17."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-06-17'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/6/17'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 0, 0, 4, 8, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(5, 0), (6, 0), (6, 1), (6, 2), (7, 3), (6, 3)])
    puzzle.add_german_whispers([(5, 5), (4, 6), (3, 6), (3, 5), (2, 5)])
    puzzle.add_german_whispers([(4, 1), (3, 0), (3, 1), (3, 2), (2, 2)])
    puzzle.add_german_whispers([(6, 8), (5, 7), (5, 6), (6, 6), (6, 5)])
    puzzle.add_german_whispers([(0, 1), (0, 2), (0, 3), (1, 4), (0, 5)])
    puzzle.add_german_whispers([(5, 3), (4, 3), (4, 4), (3, 4)])
    puzzle.add_german_whispers([(7, 5), (8, 5), (8, 4), (7, 4)])
    puzzle.add_german_whispers([(2, 8), (1, 7), (1, 8), (0, 7)])
    puzzle.add_german_whispers([(8, 7), (8, 8), (7, 7)])
    puzzle.add_german_whispers([(8, 1), (7, 1), (8, 0)])

    return puzzle
