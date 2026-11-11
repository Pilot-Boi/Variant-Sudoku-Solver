"""PuzzleMadness Little Killer Sudoku — 2025-05-24."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-05-24'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/5/24'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 3, 0, 9, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 4, 0],
        [0, 7, 0, 1, 0, 0, 0, 0, 0],
        [0, 3, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 23, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 36, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 53, clue_position=(0, 0, 0))
    puzzle.add_little_killer([(1, 0), (0, 1)], 9, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 24, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 48, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 32, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 33, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 14, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 31, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 34, clue_position=(0, 2, 2))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 13, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 14, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(5, 8), (4, 7), (3, 6), (2, 5), (1, 4), (0, 3)], 31, clue_position=(1, 6, 1))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 19, clue_position=(0, 5, 3))

    return puzzle
