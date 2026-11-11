"""PuzzleMadness Little Killer Sudoku — 2025-03-28."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-03-28'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/3/28'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 5, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 5, 0, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 1],
        [0, 0, 3, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(7, 0), (8, 1)], 16, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 5), (7, 6), (6, 7), (5, 8)], 19, clue_position=(0, 4, 2))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 29, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(0, 7), (1, 8)], 13, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(2, 0), (3, 1), (4, 2), (5, 3), (6, 4), (7, 5), (8, 6)], 31, clue_position=(0, 1, 3))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 15, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(0, 2), (1, 1), (2, 0)], 14, clue_position=(1, 3, 0))
    puzzle.add_little_killer([(1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1)], 47, clue_position=(0, 0, 1))
    puzzle.add_little_killer([(8, 4), (7, 3), (6, 2), (5, 1), (4, 0)], 21, clue_position=(1, 5, 2))
    puzzle.add_little_killer([(1, 0), (0, 1)], 10, clue_position=(1, 2, 3))
    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 24, clue_position=(0, 3, 2))

    return puzzle
