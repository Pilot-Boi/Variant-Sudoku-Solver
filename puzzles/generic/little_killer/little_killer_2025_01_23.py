"""PuzzleMadness Little Killer Sudoku — 2025-01-23."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-01-23'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/1/23'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 2, 0, 0, 0, 0, 0, 0, 7],
        [0, 4, 9, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 0, 0, 0, 3, 0],
        [6, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 3, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 23, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(8, 6), (7, 7), (6, 8)], 10, clue_position=(0, 5, 2))
    puzzle.add_little_killer([(5, 8), (6, 7), (7, 6), (8, 5)], 23, clue_position=(0, 4, 1))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 23, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)], 42, clue_position=(1, 8, 0))
    puzzle.add_little_killer([(4, 0), (5, 1), (6, 2), (7, 3), (8, 4)], 27, clue_position=(0, 3, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 27, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 20, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)], 32, clue_position=(1, 5, 0))
    puzzle.add_little_killer([(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)], 29, clue_position=(1, 6, 0))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 57, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 13, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], 46, clue_position=(1, 9, 2))
    puzzle.add_little_killer([(7, 0), (8, 1)], 11, clue_position=(0, 6, 3))

    return puzzle
