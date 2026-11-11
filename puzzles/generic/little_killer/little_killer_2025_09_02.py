"""PuzzleMadness Little Killer Sudoku — 2025-09-02."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-02'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/2'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 3, 4, 0],
        [0, 0, 0, 0, 6, 2, 0, 0, 0],
        [0, 0, 6, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 24, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 29, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(4, 8), (5, 7), (6, 6), (7, 5), (8, 4)], 24, clue_position=(0, 3, 1))
    puzzle.add_little_killer([(1, 0), (0, 1)], 13, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 38, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 7, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(7, 8), (8, 7)], 9, clue_position=(0, 6, 1))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 33, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 21, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 28, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 30, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 14, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 42, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 12, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 19, clue_position=(0, 4, 2))

    return puzzle
