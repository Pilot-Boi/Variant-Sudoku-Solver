"""PuzzleMadness Little Killer Sudoku — 2025-01-05."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-05'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/5'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [6, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 4, 0, 3, 6, 0, 0],
        [0, 4, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 9, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
        [0, 3, 0, 0, 0, 0, 7, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 8, 7, 0],
        [0, 0, 0, 0, 0, 0, 3, 1, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 51, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 14, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 43, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(1, 0), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6), (8, 7)], 42, clue_position=(0, 0, 3))
    puzzle.add_little_killer([(8, 3), (7, 2), (6, 1), (5, 0)], 15, clue_position=(1, 4, 2))
    puzzle.add_little_killer([(1, 8), (0, 7)], 14, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 33, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 28, clue_position=(1, 7, 2))

    return puzzle
