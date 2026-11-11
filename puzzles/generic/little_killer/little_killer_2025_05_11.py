"""PuzzleMadness Little Killer Sudoku — 2025-05-11."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-11'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/11'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [2, 0, 0, 9, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 3, 0, 9, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 5, 0, 0, 0],
        [5, 0, 0, 1, 0, 0, 0, 2, 7],
        [6, 9, 0, 0, 7, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 41, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 45, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 28, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 52, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1), (6, 0)], 33, clue_position=(1, 7, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 12, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 29, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 43, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)], 24, clue_position=(1, 5, 3))

    return puzzle
