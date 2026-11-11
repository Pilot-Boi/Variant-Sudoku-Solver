"""PuzzleMadness Little Killer Sudoku — 2025-01-14."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-14'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/14'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 6, 0, 9, 0, 0],
        [0, 0, 8, 0, 0, 7, 1, 0, 0],
        [0, 0, 0, 8, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 3, 8, 0, 6, 1, 0],
        [0, 8, 0, 6, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 44, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 21, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 18, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 25, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 15, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(1, 0), (0, 1)], 11, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)], 26, clue_position=(1, 6, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 34, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 31, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 30, clue_position=(0, 2, 1))
    puzzle.add_little_killer([(6, 8), (5, 7), (4, 6), (3, 5), (2, 4), (1, 3), (0, 2)], 30, clue_position=(1, 7, 1))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 35, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 38, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 24, clue_position=(1, 3, 1))

    return puzzle
