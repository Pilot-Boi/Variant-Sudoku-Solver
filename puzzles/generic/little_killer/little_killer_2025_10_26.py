"""PuzzleMadness Little Killer Sudoku — 2025-10-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-10-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/10/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 5, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 5, 8, 0, 2, 0, 7, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 31, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 29, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 40, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 24, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 19, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 19, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 14, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 23, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)], 49, clue_position=(1, 9, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 11, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 31, clue_position=(0, 1, 1))

    return puzzle
