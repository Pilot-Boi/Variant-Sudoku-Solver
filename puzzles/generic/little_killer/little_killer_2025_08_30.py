"""PuzzleMadness Little Killer Sudoku — 2025-08-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-08-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/8/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 4, 0, 3, 1, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 9, 0, 0, 0, 0, 6, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 2, 0, 0, 0, 1, 0, 0, 3],
        [0, 0, 6, 0, 0, 0, 0, 8, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(0, 1), (1, 0)], 10, clue_position=(1, 2, 0))
    puzzle.add_little_killer([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], 49, clue_position=(0, -1, 0))
    puzzle.add_little_killer([(8, 5), (7, 4), (6, 3), (5, 2), (4, 1), (3, 0)], 32, clue_position=(1, 6, 2))
    puzzle.add_little_killer([(5, 0), (6, 1), (7, 2), (8, 3)], 27, clue_position=(0, 4, 3))
    puzzle.add_little_killer([(6, 0), (5, 1), (4, 2), (3, 3), (2, 4), (1, 5), (0, 6)], 37, clue_position=(1, 7, 3))
    puzzle.add_little_killer([(7, 0), (8, 1)], 6, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(0, 3), (1, 2), (2, 1), (3, 0)], 11, clue_position=(1, 4, 0))
    puzzle.add_little_killer([(8, 3), (7, 4), (6, 5), (5, 6), (4, 7), (3, 8)], 25, clue_position=(0, 2, 2))

    return puzzle
