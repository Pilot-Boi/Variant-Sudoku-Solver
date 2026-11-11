"""PuzzleMadness German Whispers Sudoku — 2025-05-29."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'German Whispers Sudoku — 2025-05-29'
SOURCE_URL = 'https://puzzlemadness.co.uk/germanwhisperlinesudoku/hard/2025/5/29'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_german_whispers([(0, 6), (1, 5), (2, 5), (2, 6), (1, 7), (1, 8)])
    puzzle.add_german_whispers([(6, 3), (7, 2), (7, 3), (6, 4), (6, 5)])
    puzzle.add_german_whispers([(3, 4), (4, 3), (4, 2), (5, 3), (5, 2)])
    puzzle.add_german_whispers([(3, 3), (2, 3), (1, 2), (0, 1), (0, 2)])
    puzzle.add_german_whispers([(5, 4), (5, 5), (4, 6), (4, 7), (3, 7)])
    puzzle.add_german_whispers([(6, 6), (7, 7), (8, 8), (8, 7)])
    puzzle.add_german_whispers([(5, 7), (5, 6), (6, 7), (7, 8)])
    puzzle.add_german_whispers([(4, 1), (4, 0), (5, 1), (6, 2)])
    puzzle.add_german_whispers([(2, 1), (3, 1), (2, 0), (3, 0)])
    puzzle.add_german_whispers([(7, 1), (8, 1), (8, 2)])
    puzzle.add_german_whispers([(7, 5), (8, 4), (7, 4)])

    return puzzle
