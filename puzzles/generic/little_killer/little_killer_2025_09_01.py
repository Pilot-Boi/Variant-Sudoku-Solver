"""PuzzleMadness Little Killer Sudoku — 2025-09-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-09-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/9/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 6, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 2, 0],
        [6, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [8, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 6, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 3],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 24, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 19, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 31, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 45, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 23, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 24, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 25, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 45, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 26, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 7), (7, 8)], 13, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 28, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 1), (7, 0)], 11, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 12, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 55, clue_position=(1, 7, 3))

    return puzzle
