"""PuzzleMadness Little Killer Sudoku — 2025-11-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-11-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/11/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 2, 0, 0, 3],
        [0, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 8, 5, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 2, 0, 3, 0, 0, 0, 0],
        [1, 4, 0, 0, 0, 6, 0, 0, 7],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 11, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8)], 44, clue_position=(0, 1, 0))
    puzzle.add_little_killer([(7, 0), (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)], 48, clue_position=(1, 8, 3))
    puzzle.add_little_killer([(3, 8), (2, 7), (1, 6), (0, 5)], 20, clue_position=(1, 4, 1))
    puzzle.add_little_killer([(7, 8), (6, 7), (5, 6), (4, 5), (3, 4), (2, 3), (1, 2), (0, 1)], 48, clue_position=(1, 8, 1))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 14, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 38, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(8, 2), (7, 1), (6, 0)], 19, clue_position=(1, 3, 2))
    puzzle.add_little_killer([(0, 1), (1, 0)], 12, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(2, 8), (1, 7), (0, 6)], 17, clue_position=(1, 3, 1))
    puzzle.add_little_killer([(3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3)], 31, clue_position=(0, 2, 1))

    return puzzle
