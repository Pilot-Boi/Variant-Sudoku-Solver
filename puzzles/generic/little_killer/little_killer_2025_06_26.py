"""PuzzleMadness Little Killer Sudoku — 2025-06-26."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-06-26'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/6/26'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 9, 0, 6, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 8, 0, 0],
        [7, 1, 3, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 1],
        [0, 0, 0, 0, 4, 0, 0, 0, 7],
        [0, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 14, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(0, 7), (1, 8)], 11, clue_position=(0, 6, 0))
    puzzle.add_little_killer([(7, 0), (8, 1)], 9, clue_position=(0, 6, 3))
    puzzle.add_little_killer([(8, 6), (7, 5), (6, 4), (5, 3), (4, 2), (3, 1), (2, 0)], 36, clue_position=(1, 7, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 33, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(2, 0), (1, 1), (0, 2)], 14, clue_position=(1, 3, 3))
    puzzle.add_little_killer([(0, 6), (1, 7), (2, 8)], 8, clue_position=(0, 5, 0))
    puzzle.add_little_killer([(0, 5), (1, 6), (2, 7), (3, 8)], 17, clue_position=(0, 4, 0))
    puzzle.add_little_killer([(2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2)], 32, clue_position=(0, 1, 1))
    puzzle.add_little_killer([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)], 45, clue_position=(0, 0, 0))

    return puzzle
