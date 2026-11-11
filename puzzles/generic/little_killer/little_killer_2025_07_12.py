"""PuzzleMadness Little Killer Sudoku — 2025-07-12."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Little Killer Sudoku — 2025-07-12'
SOURCE_URL = 'https://puzzlemadness.co.uk/littlekillersudoku/hard/2025/7/12'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 9, 0, 0, 8, 0, 0, 2],
        [0, 0, 0, 0, 9, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 5, 0, 0, 2, 0, 1],
        [9, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 9, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_little_killer([(8, 4), (7, 5), (6, 6), (5, 7), (4, 8)], 34, clue_position=(0, 3, 2))
    puzzle.add_little_killer([(8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8)], 49, clue_position=(0, 1, 2))
    puzzle.add_little_killer([(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)], 33, clue_position=(0, 3, 0))
    puzzle.add_little_killer([(6, 0), (7, 1), (8, 2)], 15, clue_position=(0, 5, 3))
    puzzle.add_little_killer([(3, 0), (2, 1), (1, 2), (0, 3)], 11, clue_position=(1, 4, 3))
    puzzle.add_little_killer([(8, 1), (7, 0)], 13, clue_position=(1, 2, 2))
    puzzle.add_little_killer([(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8)], 32, clue_position=(0, 2, 0))
    puzzle.add_little_killer([(8, 7), (7, 8)], 4, clue_position=(0, 6, 2))
    puzzle.add_little_killer([(8, 0), (7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6), (1, 7), (0, 8)], 46, clue_position=(0, -1, 2))
    puzzle.add_little_killer([(8, 7), (7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1), (1, 0)], 38, clue_position=(1, 8, 2))

    return puzzle
