"""PuzzleMadness Little Killer Sudoku — 2025-07-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 4, 0, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 9, 0],
        [4, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 4, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 42, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(1, 8), (0, 7)], 5, clue_position=(1, 2, 1))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 46, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 49, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 18, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 28, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(7, 0), (8, 1)], 12, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 43, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 25, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 19, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 20, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 27, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 46, clue_position=(0, 1, 2))

    return puzzle
