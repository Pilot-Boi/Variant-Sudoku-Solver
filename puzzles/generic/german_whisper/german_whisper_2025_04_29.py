"""PuzzleMadness German Whispers Sudoku — 2025-04-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-04-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/4/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(8, 5), (7, 5), (7, 6), (6, 5), (5, 4), (4, 4)])
    puzzle.add_german_whispers([(3, 7), (2, 8), (2, 7), (1, 7), (0, 7)])
    puzzle.add_german_whispers([(0, 2), (0, 3), (1, 4), (2, 3), (3, 2)])
    puzzle.add_german_whispers([(5, 0), (4, 0), (4, 1), (3, 1), (4, 2)])
    puzzle.add_german_whispers([(8, 0), (7, 0), (6, 1), (7, 1), (8, 2)])
    puzzle.add_german_whispers([(5, 7), (5, 6), (5, 5), (6, 6)])
    puzzle.add_german_whispers([(2, 6), (3, 6), (4, 6), (3, 5)])
    puzzle.add_german_whispers([(4, 8), (5, 8), (6, 8), (6, 7)])
    puzzle.add_german_whispers([(7, 8), (8, 7), (8, 6)])
    puzzle.add_german_whispers([(6, 3), (7, 4), (8, 4)])

    return puzzle
