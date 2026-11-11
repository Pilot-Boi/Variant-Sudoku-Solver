"""PuzzleMadness Little Killer Sudoku — 2025-08-08."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-08'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/8'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 1, 0, 0, 0, 0, 0, 3],
        [0, 9, 0, 0, 4, 6, 0, 0, 7],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 2, 3, 0, 0, 7, 0],
        [2, 5, 0, 0, 0, 0, 8, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 44, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 18, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 29, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 12, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 24, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 16, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 23, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 20, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 43, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 21, clue_position=(0, 4, 2))

    return puzzle
